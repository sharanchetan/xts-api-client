import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""""""""
|List of Instrument Id for Future Contracts|
"""""""""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_future_instrument_list
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
        exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO] # Works for BSE as well.
        )

    fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

    future_instrument_list = fo_master_df_to_xts_future_instrument_list(fo_master_df[0],
        series_list_to_include = ["FUTIDX","FUTSTK","IF"] # "FUTIDX","FUTSTK" are for NSE & "IF" is for BSE.
        )

    print(future_instrument_list)
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""