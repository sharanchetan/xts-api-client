
"""
Order Socket - Continuous streaming with auto-reconnection
"""

import asyncio
import json
from typing import Any
from dotenv import load_dotenv
from xts_api_client.interactive_socket import OrderSocket_io
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.interactive_socket_client import InteractiveSocketClient
import os

load_dotenv()


class SimpleOrderClient(InteractiveSocketClient):
    """Handles order socket events"""

    async def on_connect(self) -> None:
        print("[OK] Order Socket Connected")

    async def on_disconnect(self) -> None:
        print("[DISCONNECTED] Order Socket Disconnected")

    async def on_error(self, data: Any) -> None:
        print(f"[ERROR] Order Error: {data}")

    async def on_joined(self, data: Any) -> None:
        print(f"[OK] Joined Order Socket room: {data}")
    
    async def on_message(self, data: Any = None) -> None:
        pass

    async def on_order(self, data: Any) -> None:
        self._print_order_update(data)

    async def on_position(self, data: Any) -> None:
        self._print_position_update(data)

    async def on_trade(self, data: Any) -> None:
        self._print_trade_update(data)

    def _print_order_update(self, data: Any) -> None:
        try:
            if isinstance(data, str):
                data = json.loads(data)
            if isinstance(data, dict):
                order_id = data.get("appOrderID") or data.get("AppOrderID") or data.get("orderId") or data.get("OrderID")
                status = data.get("orderStatus") or data.get("OrderStatus")
                qty = data.get("orderQty") or data.get("OrderQty") or data.get("OrderQuantity") or data.get("OrderQty")
                filled = data.get("filledQty") or data.get("FilledQty") or data.get("CumulativeQuantity")
                price = data.get("orderPrice") or data.get("OrderPrice") or data.get("OrderAverageTradedPrice")
                if order_id:
                    print(f"[ORDER] ID: {order_id} | Status: {status} | Qty: {qty} | Filled: {filled} | Price: {price}")
        except:
            pass

    def _print_position_update(self, data: Any) -> None:
        try:
            if isinstance(data, str):
                data = json.loads(data)
            if isinstance(data, dict):
                instrument_id = data.get("exchangeInstrumentID") or data.get("ExchangeInstrumentID")
                net_qty = data.get("netQty") or data.get("NetPosition") or data.get("Quantity")
                if instrument_id:
                    print(f"[POSITION] Instrument: {instrument_id} | Net Qty: {net_qty}")
        except:
            pass

    def _print_trade_update(self, data: Any) -> None:
        try:
            if isinstance(data, str):
                data = json.loads(data)
            if isinstance(data, dict):
                order_id = data.get("appOrderID") or data.get("AppOrderID") or data.get("orderId") or data.get("OrderID")
                qty = data.get("tradeQty") or data.get("LastTradedQuantity") or data.get("Quantity")
                price = data.get("tradePrice") or data.get("LastTradedPrice") or data.get("Price")
                if order_id:
                    print(f"[TRADE] Order: {order_id} | Qty: {qty} | Price: {price}")
        except:
            pass


async def main():
    """Connect and stream order data"""

    api_key = os.getenv("XTS_INTERACTIVE_API_KEY", "").strip() or os.getenv("XTS_ORDER_API_KEY", "").strip()
    secret_key = os.getenv("XTS_INTERACTIVE_SECRET_KEY", "").strip() or os.getenv("XTS_ORDER_SECRET_KEY", "").strip()
    api_url = os.getenv("XTS_API_URL", "").strip()
    source = os.getenv("XTS_SOURCE", "WEBAPI").strip()

    if not all([api_key, secret_key, api_url]):
        print("[FAILED] Missing credentials in .env")
        print("Required: XTS_INTERACTIVE_API_KEY, XTS_INTERACTIVE_SECRET_KEY, XTS_API_URL")
        return

    print("Order Socket - Starting Connection")
    print(f"API URL: {api_url}\n")

    attempt = 0
    max_attempts = 10
    retry_delay = 3

    while attempt < max_attempts:
        order_socket = None

        try:
            if attempt == 0:
                print("[STEP 1/4] Logging in to Order API...")

            xtc = XTSConnect(
                apiKey=api_key,
                secretKey=secret_key,
                source=source,
                root=api_url
            )

            login_resp = await xtc.interactive_login()
            if login_resp.get("type") != "success":
                print(f"[FAILED] Login error: {login_resp}")
                attempt += 1
                await asyncio.sleep(retry_delay)
                continue

            if attempt == 0:
                print("[OK] Logged in successfully")
                print(f"    User ID: {xtc.userID}\n")
                print("[STEP 2/4] Creating WebSocket...")

            callback = SimpleOrderClient()

            order_socket = OrderSocket_io(
                token=xtc.token,
                userID=xtc.userID,
                root_url=xtc.root,
                reconnection=False,
                interativeSocketClient=callback
            )

            if attempt == 0:
                print("[STEP 3/4] Connecting WebSocket...")

            await order_socket.connect()
            await asyncio.sleep(1)

            if not order_socket.connected:
                print(f"[FAILED] Socket did not connect properly")
                attempt += 1
                if attempt < max_attempts:
                    print(f"[RETRY] Attempt {attempt}/{max_attempts} in {retry_delay}s...\n")
                    await asyncio.sleep(retry_delay)
                continue

            if attempt == 0:
                print("[OK] WebSocket connected\n")
                print("[STEP 4/4] Streaming order/trade/position updates...")
                print("=" * 60)
                print("[RUNNING] Order Socket is RUNNING")
                print("Press Ctrl+C to stop\n")

            attempt = 0

            # Stream data until disconnected
            while order_socket and order_socket.connected:
                await asyncio.sleep(1)

            print("[DISCONNECTED] Connection lost - attempting reconnect...")
            attempt = 1

        except KeyboardInterrupt:
            print("\n\n[STOP] User stopped connection")
            break

        except Exception as e:
            print(f"[ERROR] {str(e)[:100]}")
            attempt += 1
            if attempt < max_attempts:
                print(f"[RETRY] Attempt {attempt}/{max_attempts} in {retry_delay}s...\n")
                await asyncio.sleep(retry_delay)

        finally:
            if order_socket:
                try:
                    await order_socket.disconnect()
                except:
                    pass

    if attempt >= max_attempts:
        print(f"[FAILED] Reached max reconnection attempts ({max_attempts})")

    print("[OK] Order Socket stopped")


if __name__ == "__main__":
    asyncio.run(main())