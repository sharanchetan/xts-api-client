import asyncio
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import async_squareoff_all_positions_
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")


xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)


async def main():
    response_marketdata_login = await xt_market_data.interactive_login()

    cancel = await async_squareoff_all_positions_(xt_market_data, exchangeSegment = 1,xt = xt_market_data )


if __name__ == "__main__":
    asyncio.run(main())