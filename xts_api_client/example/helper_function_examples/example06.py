import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""
        |OHLC for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import ohlc_to_df

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()

marget_data_get_ohlc = xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM, # Also Works for BSECM
    exchangeInstrumentID = 22, # When using BSECM, Use BSE instrument Id like "526530"
    startTime = "Dec 02 2024 091500", #Time in IST
    endTime = "Dec 02 2024 133000", #Time in IST, 24 hour clock.
    compressionValue = 60) # 60 represents 1 minute. Check Documentation for different values.

# Change the values oh OHLC parameters as required.

ohlc_df = ohlc_to_df(marget_data_get_ohlc)
print(ohlc_df)
""""""""""""""""""""""""""""""""""""""""""