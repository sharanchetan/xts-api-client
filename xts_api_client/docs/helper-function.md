# Helper Functions/Methods available in package.
* Helper function are written inside the package to serve as an example to end user on how to use the package.
## __XTS_Helper__

### __cm_master_string_to_df__:  
Converts the response of cm_master API to a pandas DataFrame. This function takes a string response from the cm_master API, which contains data separated by the '|' character, and converts it into a pandas DataFrame.  The DataFrame will have predefined column headers.
___

Parameters: __cm_master_result__ of string type : The string response from the cm_master API.

Returns: __pd.DataFrame__: A pandas DataFrame containing the parsed data from the cm_master_result string.
___
```
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df

xt_market_data = XTSConnect(
apiKey = "apiKey",
secretKey = "secretKey",
source = "source",
root = "root"
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM]
)

print(cm_master_string_to_df(market_data_get_master['result']))
```

### __fo_master_string_to_df__:
Converts the response of master API to pandas DataFrame for fo segment. This function takes a string response from the fo_master API, splits it into lines, and then categorizes each line into futures or options based on the number of columns. It then converts these categorized lines into pandas DataFrames with appropriate column headers.
___       

Parameters: __fo_master_result__ of string type : The string response from the fo_master API.

Returns: __tuple__: A tuple containing two pandas DataFrames:

__fut_master_df__: DataFrame containing futures data.

__opt_master_df__: DataFrame containing options data.

___
```
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df

xt_market_data = XTSConnect(
apiKey = "apiKey",
secretKey = "secretKey",
source = "source",
root = "root"
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO]
    )
#User can swap NSEFO with BSEFO if needed.

print(fo_master_string_to_df(market_data_get_master['result']))
```
### __cm_master_df_to_xts_cm_instrument_list__:
Converts the pandas DataFrame of cm_master API to list of xts_cm_Instrument objects.
___

Parameters: __cm_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List ["EQ","BE","BZ","SM","A","B"].

Returns: __list__ of XTS Cash Market Instruments.
___
```
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df, cm_master_df_to_xts_cm_instrument_list

xt_market_data = XTSConnect(
apiKey = "apiKey",
secretKey = "secretKey",
source = "source",
root = "root"
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM]
)
#User can swap NSEFO with BSEFO if needed.
cm_master_df  = cm_master_string_to_df(market_data_get_master['result'])

cm_instrument_list=cm_master_df_to_xts_cm_instrument_list(
    cm_master_df = cm_master_df,
    series_list_to_include = ["EQ","BE","BZ","SM","A","B"]
    )
print(cm_instrument_list)
```
### __fo_master_df_to_xts_future_instrument_list__:
Converts the pandas DataFrame of fo_master API to list of xts_future_Instrument objects.
___   

Parameters: __fo_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List ["FUTIDX","FUTSTK","IF"].

Returns: __list__ of XTS Futures Instruments.
___
```
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_future_instrument_list

xt_market_data = XTSConnect(
apiKey = "apiKey",
secretKey = "secretKey",
source = "source",
root = "root"
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO]
    )
#User can swap NSEFO with BSEFO if needed.

fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

future_instrument_list = fo_master_df_to_xts_future_instrument_list(fo_master_df[0],
    series_list_to_include = ["FUTIDX","FUTSTK","IF"]
    )

print(future_instrument_list)
```
### __fo_master_df_to_xts_options_instrument_list__:
Converts the pandas DataFrame of fo_master API to list of xts_optoins_Instrument objects
___ 
Parameters: __fo_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List : ["OPTIDX","OPTSTK","IO"].

Returns: __list__ of XTS Options Instruments.
___
```
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_options_instrument_list

xt_market_data = XTSConnect(
apiKey = "apiKey",
secretKey = "secretKey",
source = "source",
root = "root"
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO]
    )
#User can swap NSEFO with BSEFO if needed.

fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

options_instrument_list = fo_master_df_to_xts_options_instrument_list(fo_master_df[1],
    series_list_to_include = ["OPTIDX","OPTSTK","IF"]
    )

print(options_instrument_list)
```
