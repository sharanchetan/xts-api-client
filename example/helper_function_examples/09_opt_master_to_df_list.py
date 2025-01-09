import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""""""""
|List of Instrument Id for Options Contracts|
"""""""""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_options_instrument_list

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO] # Works for BSE as well.
    )
#User can swap NSEFO with BSEFO if needed.

fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

options_instrument_list = fo_master_df_to_xts_options_instrument_list(fo_master_df[1],
    series_list_to_include = ["OPTIDX","OPTSTK","IO"] # "OPTIDX","OPTSTK" are for NSE & "IO" is for BSE.
    )

print(options_instrument_list)
""""""""""""""""""""""""""""""""""""""""""