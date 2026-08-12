import os
import asyncio
from dotenv import load_dotenv
from xts_api_client.xts_connect_async import XTSConnect

load_dotenv()

API_key = os.getenv("XTS_Interactive_API_KEY")
API_secret = os.getenv("XTS_Interactive_SECRET_KEY")
API_source = os.getenv("XTS_SOURCE")
API_root = os.getenv("XTS_API_URL")


async def main():
    xt_interactive_data = XTSConnect(
        apiKey=API_key,
        secretKey=API_secret,
        source=API_source,
        root=API_root
    )

    # Login
    login_response = await xt_interactive_data.interactive_login()
    brokerage_payload = [
            {
                "exchangeSegment": 2,
                "exchangeInstrumentID": 47664,
                "productType": "NRML",
                "orderSide": "BUY",
                "orderQty": 75,
                "orderPrice": 123
            }
        ]
    brokerage_response = await xt_interactive_data.calculate_brokerage(
        brokerage_payload
    )

    print("Brokerage Response:")
    print(brokerage_response)


if __name__ == "__main__":
    asyncio.run(main())