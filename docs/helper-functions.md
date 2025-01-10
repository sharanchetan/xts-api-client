# Helper Functions/Methods available in package.
* Helper function are written inside the package to serve as an example to end user on how to use the package.
* Examples for both synchronous & asynchronous versions are shown.
## __XTS_Helper__

### __cm_master_string_to_df__:  
Converts the response of cm_master API to a pandas DataFrame. This function takes a string response from the cm_master API, which contains data separated by the '|' character, and converts it into a pandas DataFrame.  The DataFrame will have predefined column headers.
___

Parameters: __cm_master_result__ of string type : The string response from the cm_master API.

Returns: __pd.DataFrame__: A pandas DataFrame containing the parsed data from the cm_master_result string.
___
```
"""""""""""""""""""""""""""""""""""""""
      |DataFrame for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df
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
      exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSECM as well.
      )

      print((cm_master_string_to_df(market_data_get_master['result'])))
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""
```
```
"""""""""""""""""""""""""""""""""""""""
      |DataFrame for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSECM as well
)

print(cm_master_string_to_df(market_data_get_master['result']))
""""""""""""""""""""""""""""""""""""""""""
```

### __fo_master_string_to_df__:
Converts the response of master API to pandas DataFrame for fo segment. This function takes a string response from the fo_master API, splits it into lines, and then categorizes each line into futures or options based on the number of columns. It then converts these categorized lines into pandas DataFrames with appropriate column headers.
___       

Parameters: __fo_master_result__ of string type : The string response from the fo_master API.

Returns: __tuple__: A tuple containing three pandas DataFrames:

__fut_master_df__: DataFrame containing futures data.

__opt_master_df__: DataFrame containing options data.

__fut_spread_df__: DataFrame Containing future spread data.

___
```
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
```
```
"""""""""""""""""""""""""""""""""""""""
   |Tuple of DataFrame for FO Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSEFO] # Works for BSECM as well.
    )

"""
future_master_df = fo_master_string_to_df(market_data_get_master['result'])
print(future_master_df[0]) # This will give DataFrame for Future.

options_master_df = fo_master_string_to_df(market_data_get_master['result'])
print(options_master_df[1]) # This will give DataFrame for Options.

fut_spread_df = fo_master_string_to_df(market_data_get_master['result'])
print(fut_spread_df[2]) # This will give DataFrame for Options.
"""

print(fo_master_string_to_df(market_data_get_master['result'])) 

""""""""""""""""""""""""""""""""""""""""""
```
### __cm_master_df_to_xts_cm_instrument_list__:
Converts the pandas DataFrame of cm_master API to list of xts_cm_Instrument objects.
___

Parameters: __cm_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List ["EQ","BE","BZ","SM","A","B"].

Returns: __list__ of XTS Cash Market Instruments.
___
```
"""""""""""""""""""""""""""""""""""""""
|List of InstrumentID for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df, cm_master_df_to_xts_cm_instrument_list
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
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSE as well.
    )
    #User can swap NSEFO with BSEFO if needed.
    cm_master_df  = cm_master_string_to_df(market_data_get_master['result'])

    cm_instrument_list=cm_master_df_to_xts_cm_instrument_list(
        cm_master_df = cm_master_df,
        series_list_to_include = ["EQ","BE","BZ","SM","A","B"] # "EQ","BE","BZ" Are for NSE & "SM","A","B" are for BSE.
    )
    print(cm_instrument_list)
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""
```
```
"""""""""""""""""""""""""""""""""""""""
|List of InstrumentID for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df, cm_master_df_to_xts_cm_instrument_list

xt_market_data = XTSConnect(
apiKey = API_key,
secretKey = API_secret,
source = API_source,
root = API_root
)
response_marketdata_login = xt_market_data.marketdata_login()

market_data_get_master = xt_market_data.get_master(
exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSE as well.
)
#User can swap NSEFO with BSEFO if needed.
cm_master_df  = cm_master_string_to_df(market_data_get_master['result'])

cm_instrument_list=cm_master_df_to_xts_cm_instrument_list(
    cm_master_df = cm_master_df,
    series_list_to_include = ["EQ","BE","BZ","SM","A","B"] # "EQ","BE","BZ" Are for NSE & "SM","A","B" are for BSE.
)
print(cm_instrument_list)
""""""""""""""""""""""""""""""""""""""""""
```
### __fo_master_df_to_xts_future_instrument_list__:
Converts the pandas DataFrame of fo_master API to list of xts_future_Instrument objects.
___   

Parameters: __fo_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List ["FUTIDX","FUTSTK","IF"].

Returns: __list__ of XTS Futures Instruments.
___
```
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
```
```
"""""""""""""""""""""""""""""""""""""""""""""
|List of Instrument Id for Future Contracts|
"""""""""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_future_instrument_list

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

fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

future_instrument_list = fo_master_df_to_xts_future_instrument_list(fo_master_df[0],
    series_list_to_include = ["FUTIDX","FUTSTK","IF"] # "FUTIDX","FUTSTK" are for NSE & "IF" is for BSE.
    )

print(future_instrument_list)
""""""""""""""""""""""""""""""""""""""""""
```
### __fo_master_df_to_xts_options_instrument_list__:
Converts the pandas DataFrame of fo_master API to list of xts_optoins_Instrument objects
___ 
Parameters: __fo_master_df__ with pd.DataFrame type & __series_list_to_include__ with list type. Example of List : ["OPTIDX","OPTSTK","IO"].

Returns: __list__ of XTS Options Instruments.
___
```
"""""""""""""""""""""""""""""""""""""""""""""
|List of Instrument Id for Options Contracts|
"""""""""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import fo_master_string_to_df, fo_master_df_to_xts_options_instrument_list
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
    #User can swap NSEFO with BSEFO if needed.

    fo_master_df = fo_master_string_to_df(market_data_get_master['result'])

    options_instrument_list = fo_master_df_to_xts_options_instrument_list(fo_master_df[1],
        series_list_to_include = ["OPTIDX","OPTSTK","IO"] # "OPTIDX","OPTSTK" are for NSE & "IO" is for BSE.
        )

    print(options_instrument_list)
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""
```
```
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
```
### __ohlc_to_df__:
Converts XTS-API(from XTS.Connect.get_ohlc()) generated OHLC data to pandas DataFrame.
___
Parameters: The return of __XTS.Connect.get_ohlc()__ method with dictionary type. Example of dict : {'type': 'success', 'code': 's-instrument-0002', 'description': 'Data found', 'result': {'exchangeSegment': 'NSECM', 'exchangeInstrumentID': '22', 'dataReponse': 'data removed'}}
Returns: A __pd.DataFrame__ from the OHLC values.
___
```
"""""""""""""""""""""""""""""""""""""""
        |OHLC for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import ohlc_to_df
import asyncio

async def main():
    xt_market_data = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )
    response_marketdata_login = await xt_market_data.marketdata_login()

    marget_data_get_ohlc = await xt_market_data.get_ohlc(
        exchangeSegment = xt_market_data.EXCHANGE_NSECM, # Also Works for BSECM
        exchangeInstrumentID = 22, # When using BSECM, Use BSE instrument Id like "526530"
        startTime = "Dec 02 2024 091500", #Time in IST
        endTime = "Dec 02 2024 133000", #Time in IST, 24 hour clock.
        compressionValue = 60) # 60 represents 1 minute. Check Documentation for different values.

    # Change the values oh OHLC parameters as required.

    ohlc_df = ohlc_to_df(marget_data_get_ohlc)
    print(ohlc_df)
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""
```
```
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

market_data_get_ohlc = xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM, # Also Works for BSECM
    exchangeInstrumentID = 22, # When using BSECM, Use BSE instrument Id like "526530"
    startTime = "Dec 02 2024 091500", #Time in IST
    endTime = "Dec 02 2024 133000", #Time in IST, 24 hour clock.
    compressionValue = 60) # 60 represents 1 minute. Check Documentation for different values.

# Change the values oh OHLC parameters as required.

ohlc_df = ohlc_to_df(market_data_get_ohlc)
print(ohlc_df)
""""""""""""""""""""""""""""""""""""""""""
```

### __equityticker_exchangeInstrumentId_dict__:
Converts XTS-API DataFrame (generated from XTS.Connect.get_master() with helper functoin __cm_master_string_to_df/fo_master_string_to_df__) to a dictionary. So that user can search Instrument Id with ticker symbol. IT ONLY WORKS FOR CASH MARKET.
___
Parameters: The return of __cm_master_string_to_df/fo_master_string_to_df__ methods with the pd.DataFrame type.
Returns: A __Dictionary__ containing Ticker Symbol as keys & Exchange Instrument Id as values. 
___

```
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
```

### __dostime_secomds_to_unixtime__:
Converts the MS DOS time that is used by NSE & BSE to Unix epoch time.
    * The MS-DOS time/date format uses midnight on January 1, 1980 as a sentinel value, or epoch.
    * Unix epoch starts from  midnight on January 1, 1970.
The function also allowes to add timezone info to the converted time. by default it will add the timezone info of Asia/Kolkata.
_IMPORTANT: Adding timezone info makes the time aware about time zone. but the value of Uniux will remain UNCHNAGED!_
___
Parameters: ms dos time in seconds.
Returns: Time in unix epoch. 
___
```
from xts_api_client.helper.helper import dostime_secomds_to_unixtime

print(dostime_secomds_to_unixtime(1420378549, "UTC"))
```