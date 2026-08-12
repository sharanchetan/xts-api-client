import os
from dotenv import load_dotenv
load_dotenv()
from xts_api_client.xts_connect_async import XTSConnect
import asyncio

API_key = os.getenv("XTS_MARKETDATA_API_KEY")
API_secret = os.getenv("XTS_MARKETDATA_SECRET_KEY")
API_source = os.getenv("XTS_SOURCE")
API_root = os.getenv("XTS_API_URL")

async def main():
    xt_market_data = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )

    response_marketdata_login = await xt_market_data.marketdata_login()
    print(response_marketdata_login)
    resp = await xt_market_data.get_ohlc(exchangeSegment=1,exchangeInstrumentID=22,startTime="Jan 01 2026 091500",endTime="Jan 10 2026 153000", compressionValue=60)
    print(resp)
if __name__ == "__main__":
    asyncio.run(main())   