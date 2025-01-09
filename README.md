# Introduction

* This package is written to be used as a XTS API Client in Python.
* With the correct API credentials, User can access XTS interactive & market data.

# Reference
*  This is a python client package for XTS API. XTS is product from [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/). The original documentation for XTS Clinet is [___linked here___](https://symphonyfintech.com/xts-market-data-front-end-api-v2/).

*  This package is a __derivative work__ of the original package written by [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/).
*  [Link for original GitHub Repository](https://github.com/symphonyfintech/xts-pythonclient-api-sdk). It takes inspirations from the original, however it differs in the implimentation.

# Package Structure
* To better consume the package, the user should have a clear understanding of the architecture of the package.

Here is the folder structure of the project:

```
└───xts_api_client
    │   interactive_socket.py
    │   interactive_socket_client.py
    │   market_data_socket.py
    │   market_data_socket_client.py
    │   py.typed
    │   xts_connect.py
    │   xts_connect_async.py
    │   xts_exception.py
    │   __init__.py
    │   
    ├───helper
        helper.py
        helper_classes.py
        __init__.py
```

There are two version of xts_connect. A synchronous version & an asynchronous version.

## xts_connect.py
* This module is written for simple test cases & basic understanding of the API, however in practical cases, user will have to use asynchronous methods.
## xts_connect_async.py
* For all intensive purposes, this module will be used only because of the nature of application.

# Getting Started
* The user should have ___API Key___, ___API Secret Key___ & the ___URL___ with ___Port___ details for using this package.
* XTS API is a [REST](https://en.wikipedia.org/wiki/REST) based Trading API with [___Socket IO___](https://en.wikipedia.org/wiki/Socket.IO) streaming component. This client makes it easier to consume the data from API into Python.
* In XTS, there are two types of API, one for __trading (interactive sessions)__ & one for __market data__.

## [Trading API](https://symphonyfintech.com/xts-trading-front-end-api-v2/)
* Trading APIs allows to integrate trading system with XTS Platform for placing orders, monitor your positions, manage your portfolio and much more.
## [Market Data API](https://symphonyfintech.com/xts-market-data-front-end-api-v2/#section/Authentication)
* Market Data API is a mixed HTTP REST and HTTP streaming API. It provides access to live quotes data on a wide range of symbols.

## __Steps to use the Package__

* Here's an example code block that loads API credentials from environment variables and uses them to log in to a MarketData API. It has been explained in subsequest steps.

```
import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")

"""""""""""""""""""""""""""""""""""""""
      |DataDrame for Cash Market|
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
## ___Step 1. Instantiate XTS class into object before login.___
* Import _class_ 'XTSConnect' & then instantiate it as shown.
* Write your apikey, secretkey, source & root. Root is the URL with port included.

```

from xts_api_client.xts_connect_async import XTSConnect

xt_market_data = XTSConnect(
      apiKey = API_key,
      secretKey = API_secret,
      source = API_source,
      root = API_root
      )

```
## ___Step 2. Logging in.___
* As mentioned earlier, there are two types of API in XTS. The below example is for market data API.
* After instantiating XTSConnect. Use the method marketdata login to log in & access data.

```
response_marketdata_login = await xt_market_data.marketdata_login()
```

If the credentials are correct, printing 'response_marketdata_login' will five a JSON like following.
```
{'type': 'success', 'code': 'e-response-0010', 'description': 'Provided Valid Credentials', 'result': {'token': data removed, 'userID': data removed, 'appVersion': data removed, 'application_expiry_date': data removed}}
```
## ___Step 3. Getting Configuration.___
* Once you have logged in through market_data_API, you can get the configuration for the market data.
```
market_data_get_config = await xt_market_data.get_config()
```

Printing the 'market_data_get_config' will give JSON like following.

```
{'type': 'success', 'code': 's-response-0001', 'description': 'Fetched configurations successfully', 'result': __{'exchangeSegments': {'NSECM': 1, 'NSEFO': 2, 'NSECD': 3, 'NSECO': 4, 'SLBM': 5, 'NIFSC': 7, 'BSECM': 11, 'BSEFO': 12, 'BSECD': 13, 'BSECO': 14, 'NCDEX': 21, 'MSECM': 41, 'MSEFO': 42, 'MSECD': 43, 'MCXFO': 51}__, 'xtsMessageCode': {'touchlineEvent': 1501, 'marketDepthEvent': 1502, 'indexDataEvent': 1504, 'candleDataEvent': 1505, 'openInterestEvent': 1510, 'instrumentPropertyChangeEvent': 1105, 'ltpEvent': 1512}, 'publishFormat': ['Binary', 'JSON'], 'broadCastMode': ['Full', 'Partial'], 'instrumentType': {'1': 'Futures', '2': 'Options', '4': 'Spread', '8': 'Equity', '16': 'Spot', '32': 'PreferenceShares', '64': 'Debentures', '128': 'Warrants', 
'256': 'Miscellaneous', '512': 'MutualFund', 'Futures': 1, 'Options': 2, 'Spread': 4, 'Equity': 8, 'Spot': 16, 'PreferenceShares': 32, 'Debentures': 64, 'Warrants': 128, 'Miscellaneous': 256, 'MutualFund': 512}}}
```
## ___Step 4. Getting the Master Data.___
* XTS provides API Call to fetch all tradable as well as some additional Instrument/contract masters in a single structure. 
* This call can be made once in a day and the response can be persisted in local storage or file as per you application design and you can fetch instrumented or Symbols from this dataset throughout the day.
* The type of _master_ is a dictionary, that contains all the data sepearted by "|".
* The parameter 'exchangeSegmentList' takes a list of exchange segments. In XTS, NSE has few segments as shown in the cofig output above.

```
market_data_get_master = await xt_market_data.get_master(
      exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSECM as well.
      )
```
* Both above & below code will give same result. 
```
market_data_get_master = await xt_market_data.get_master(
      exchangeSegmentList = ['NSECM']
      )
```

A snippet of print of market_data_get_master.
```
...nNSECM|11369|8|TTKHLTCARE|TTKHLTCARE-EQ|EQ|TTKHLTCARE-EQ|1100100011369|1798.7|1199.2|66709|0.05|1|1|TTKHLTCARE|INE910C01018|1|1|TTK HEALTHCARE LIMITED-EQ|0|-1|-1\nNSECM|20364|8|771KL43|771KL43-SG|SG|771KL43-SG|1100100020364|102.37|92.62|1025599|0.01|100|1|771KL43|IN2020230172|1|1|SDL KL 7.71% 2043-SG|0|-1|-1\nNSECM|21711|8|68PN26|68PN26-SG|SG|68PN26-SG|1100100021711|108.7|98.35|965899|0.01|100|1|68PN26|IN2820200052|1|1|SDL PN 6.8% 2026-SG|0|-1|-1'}
```
## ___Step 5. Getting the OHLC Data.___
* The data is available in the form of a candle timestamp with epoch from 1970, Open, High, Low, Close, Volume, OI.
* The least compression available is 60(1 minute) for both event stream and long polling (GET at 1 Request Per Second).
* Other supported intervals for GET (long polling ) Request are 2 minute, 3 minutes, 5 minutes, 15 minutes, 30 minutes , hourly and daily.
* Format of startTime & endTime is "MMM DD YYYY HHMMSS". In the example given below 091500 means morning nine fifteen in IST. Market open time :-) .

```
marget_data_get_ohlc = await xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM,
    exchangeInstrumentID = 22,
    startTime = "Dec 02 2024 091500",
    endTime = "Dec 02 2024 093000",
    compressionValue = 60)
```

Printing market_data_get_ohlc will give a dictionary, as shown below.

```
{'type': 'success', 'code': 's-instrument-0002', 'description': 'Data found', 'result': {'exchangeSegment': 'NSECM', 'exchangeInstrumentID': '22', 'dataReponse': DELETED FOR DATA PRIVACY}}
```
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
      |DataDrame for Cash Market|
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
      |DataDrame for Cash Market|
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
   |Tuple of DataDrame for FO Market|
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