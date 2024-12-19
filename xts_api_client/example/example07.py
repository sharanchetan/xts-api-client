import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""""""""""""""
|Ticker:ExchangeInstrumentId Dict for Cash Market|
"""""""""""""""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df
from xts_api_client.helper.helper import ticker_exchangeInstrumentId_dict

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()
market_data_get_master = xt_market_data.get_master(exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM]) # Works for BSECM as well.

cm_master_df = cm_master_string_to_df(market_data_get_master['result'])
ticker_exchInstrumentID_dict = ticker_exchangeInstrumentId_dict(cm_master_df)
print(ticker_exchInstrumentID_dict.get('RELIANCE')) # Reliance is kept here as an example. User can print "ticker_exchInstrumentID_dict" for full data.

""""""""""""""""""""""""""""""""""""""""""