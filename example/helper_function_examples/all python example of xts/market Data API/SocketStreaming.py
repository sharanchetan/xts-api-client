
"""
Market Data Socket - Continuous streaming with auto-reconnection
"""

import asyncio
import json
from typing import Any
from dotenv import load_dotenv
from xts_api_client.market_data_socket import MDSocket_io
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.market_data_socket_client import MarketDataSocketClient
import os

load_dotenv()


class SimpleMarketDataClient(MarketDataSocketClient):
    """Handles market data socket events"""

    async def on_connect(self) -> None:
        print("[OK] Market Data Socket Connected")

    async def on_disconnect(self) -> None:
        print("[DISCONNECTED] Market Data Socket Disconnected")

    async def on_error(self, data: Any) -> None:
        print(f"[ERROR] Market Data Error: {data}")

    async def on_message(self, data: Any = None) -> None:
        pass

    async def on_event_last_traded_price_full(self, data: Any) -> None:
        self._print_ltp(data)

    async def on_event_last_traded_price_partial(self, data: Any) -> None:
        self._print_ltp(data)

    async def on_event_touchline_full(self, data: Any) -> None:
        self._print_ltp(data)

    async def on_event_touchline_partial(self, data: Any) -> None:
        self._print_ltp(data)

    async def on_event_market_data_full(self, data: Any) -> None:
        pass

    async def on_event_market_data_partial(self, data: Any) -> None:
        pass

    async def on_event_candle_data_full(self, data: Any) -> None:
        pass

    async def on_event_candle_data_partial(self, data: Any) -> None:
        pass

    async def on_event_market_status_full(self, data: Any) -> None:
        pass

    async def on_event_openinterest_full(self, data: Any) -> None:
        pass

    async def on_event_openinterest_partial(self, data: Any) -> None:
        pass

    async def on_event_instrument_change_full(self, data: Any) -> None:
        pass

    async def on_event_instrument_change_partial(self, data: Any) -> None:
        pass

    def _print_ltp(self, data: Any) -> None:
        try:
            if isinstance(data, str):
                data = json.loads(data)
            if isinstance(data, dict):
                touchline = data.get("Touchline", {}) if isinstance(data.get("Touchline"), dict) else {}
                instrument_id = (
                    data.get("exchangeInstrumentID")
                    or data.get("ExchangeInstrumentID")
                    or touchline.get("exchangeInstrumentID")
                    or touchline.get("ExchangeInstrumentID")
                )
                ltp = (
                    data.get("ltp")
                    or data.get("LastTradedPrice")
                    or touchline.get("ltp")
                    or touchline.get("LastTradedPrice")
                )
                if ltp and instrument_id:
                    print(f"[LTP] Instrument: {instrument_id} | LTP: {ltp}")
        except:
            pass


async def main():
    """Connect and stream market data"""

    api_key = os.getenv("XTS_MARKETDATA_API_KEY", "").strip()
    secret_key = os.getenv("XTS_MARKETDATA_SECRET_KEY", "").strip()
    api_url = os.getenv("XTS_API_URL", "").strip()
    source = os.getenv("XTS_SOURCE", "WEBAPI").strip()

    if not all([api_key, secret_key, api_url]):
        print("[FAILED] Missing credentials in .env")
        print("Required: XTS_MARKETDATA_API_KEY, XTS_MARKETDATA_SECRET_KEY, XTS_API_URL")
        return

    print("Market Data Socket - Starting Connection")
    print(f"API URL: {api_url}\n")

    attempt = 0
    max_attempts = 10
    retry_delay = 3

    while attempt < max_attempts:
        md_socket = None

        try:
            if attempt == 0:
                print("[STEP 1/5] Logging in to Market Data API...")

            xtc = XTSConnect(
                apiKey=api_key,
                secretKey=secret_key,
                source=source,
                root=api_url
            )

            login_resp = await xtc.marketdata_login()
            if login_resp.get("type") != "success":
                print(f"[FAILED] Login error: {login_resp}")
                attempt += 1
                await asyncio.sleep(retry_delay)
                continue

            if attempt == 0:
                print("[OK] Logged in successfully")
                print(f"    User ID: {xtc.userID}\n")
                print("[STEP 2/5] Creating WebSocket...")

            callback = SimpleMarketDataClient()

            md_socket = MDSocket_io(
                token=xtc.token,
                userID=xtc.userID,
                root_url=xtc.root,
                reconnection=False,
                marketdatasocketclient=callback
            )

            if attempt == 0:
                print("[STEP 3/5] Connecting WebSocket...")

            await md_socket.connect()
            await asyncio.sleep(1)

            if not md_socket.connected:
                print(f"[FAILED] Socket did not connect properly")
                attempt += 1
                if attempt < max_attempts:
                    print(f"[RETRY] Attempt {attempt}/{max_attempts} in {retry_delay}s...\n")
                    await asyncio.sleep(retry_delay)
                continue

            if attempt == 0:
                print("[OK] WebSocket connected\n")
                print("[STEP 4/5] Subscribing to instruments...")

            # Using RELIANCE (2885) cash equity on Segment 1 (NSECM) as default
            instruments = [{"exchangeSegment": 1, "exchangeInstrumentID": 2029}]

            sub_resp = await xtc.send_subscription(
                Instruments=instruments,
                xtsMessageCode=1501
            )

            if sub_resp.get("type") != "success":
                print(f"[FAILED] Subscription error: {sub_resp}")
                attempt += 1
                await asyncio.sleep(retry_delay)
                continue

            if attempt == 0:
                print("[OK] Subscribed to instruments\n")
                print("[STEP 5/5] Streaming data...")
                print("=" * 60)
                print("[RUNNING] Market Data Socket is RUNNING")
                print("Press Ctrl+C to stop\n")

            attempt = 0

            # Stream data until disconnected
            while md_socket and md_socket.connected:
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
            if md_socket:
                try:
                    await md_socket.disconnect()
                except:
                    pass

    if attempt >= max_attempts:
        print(f"[FAILED] Reached max reconnection attempts ({max_attempts})")

    print("[OK] Market Data Socket stopped")


if __name__ == "__main__":
    asyncio.run(main()) 