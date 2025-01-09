import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""
   |Tuple of DataDrame for FO Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df
import asyncio
async def main():
    xt_market_data = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )
    response_marketdata_login = await xt_market_data.marketdata_login()

    market_data_get_master = await xt_market_data.get_master(
        exchangeSegmentList = [xt_market_data.EXCHANGE_BSEFO] # Works for BSECM as well.
        )

    """
    future_master_df = fo_master_string_to_df(market_data_get_master['result'])
    print(future_master_df[0]) # This will give DataFrame for Future.

    options_master_df = fo_master_string_to_df(market_data_get_master['result'])
    print(options_master_df[1]) # This will give DataFrame for Options.

    future_master_df = fo_master_string_to_df(market_data_get_master['result'])
    print(future_master_df[2]) # This will give DataFrame for Spread.
    """
    print((fo_master_string_to_df(market_data_get_master['result'])))
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""