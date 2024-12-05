# Installation
Currently, the package is not been hosted on the [Python Package Index](https://pypi.org/). So other workarounds are mentioned here to make use of the package.
## Direct Use
The package can be used directly, as in downloading the complete source code & then importing it. As shown below.
```
from xts_api_client.src.xts_api_client.xts_connect import XTSConnect
```

## Local Installation
* To install the package locally, download the complete zip of the package.
* As per user discretion, use [virtual envirnment](https://docs.python.org/3/library/venv.html) or [uv package manager](https://docs.astral.sh/uv/). Activate the envirnment. ___This is an optional step___ .
* Navigate the __PowerShell/Command prompt__ to the directory (xts_api_client\dist) where __xts_api_client-0.1.0-py3-none-any.whl__ file exists.
* Use "pip install xts_api_client-0.1.0-py3-none-any.whl"
* Use "pip list" or "uv pip list" to verify the installation.

## Local Server Installation
* If the user wants to host the package in there local server. It can be hosted with [___pypiserver___](https://pypi.org/project/pypiserver/)
* User can follow the 3 step process mentioned in the [pypiserver GitHub Repository](https://github.com/pypiserver/pypiserver?tab=readme-ov-file#quickstart-installation-and-usage). (pip install, serverstart & package upload)
* For ___pypiserver___ , move the files inside "xts_api_client\dist" to "packages".
* Use pip to install the package. The user needs to get comfortable with pypiserver to write the correct syntex for local server installation. Example of the command is shown below.
```
pip install --extra-index-url http://192.168.50.103:8080 xts_api_client
```
## Pip install/uv add
* Currently, the package has not been published on [Python Package Index](https://pypi.org/).   
# Explanation
* The user should have ___API Key___, ___API Secret Key___ & the ___URL___ with ___Port___ details for using this package.
* XTS API is a REST based Trading API with ___Socket IO___ streaming component. This client makes it easier to consume the data from API into Python.
* In XTS, there are two types of API, one for __trading (interactive sessions)__ & one for __market data__.

## [Trading API](https://symphonyfintech.com/xts-trading-front-end-api-v2/)
* Trading APIs allows to integrate trading system with XTS Platform for placing orders, monitor your positions, manage your portfolio and much more.
## [Market Data API](https://symphonyfintech.com/xts-market-data-front-end-api-v2/#section/Authentication)
* Market Data API is a mixed HTTP REST and HTTP streaming API. It provides access to live quotes data on a wide range of symbols.

# Functions/Methods available in package.
* Most of these functions are self explanatory in nature. However, a simple explanations is mentioned for them.
*  The __Trading API__ gives the user access to 
      *  ___interactive_login___: Send the login url to which a user should receive the token.
      *  ___get_order_book___: Request order book gives states of all the orders placed by an user.
      *  ___get_dealer_orderbook___: No idea, figure it out yourself!
      *  ___place_order___: To place an order.
      *  ___place_bracketorder___: To place a bracketorder.
      *  ___get_profile___: Using session token user can access his profile stored with the broker.
      *  ___get_balance___: Get balance API call grouped under this category information related to limits on equities, derivative, upfront margin, available exposure and other RMS related balances available to the user.
      *  ___modify_order___: The facility to modify your open orders by allowing you to change limit order to market or vice versa, change price or quantity of the limit open order, change disclosed quantity or stop-loss of any open stop loss order.
      *  ___get_trade___: Trade book returns a list of all trades executed on a particular day, that were placed by the user. The trade book will display all filled and partially filled orders.
      *  ___get_dealer_tradebook___: Trade book returns a list of all trades executed on a particular day, that were placed by the user. The trade book will display all filled and partially filled orders.
      *  ___get_holding___: Holdings API call enable users to check their long term holdings with the broker.
      *  ___bracketorder_cancel___: This API can be called to cancel any open order of the user by providing correct appOrderID matching with the chosen open order to cancel.
      *  ___get_dealerposition_netwise___: The positions API positions by net. Net is the actual, current net position portfolio.
      *  ___get_dealerposition_daywise___: The positions API returns positions by day, which is a snapshot of the buying and selling activity for that particular day.
      *  ___get_position_daywise___: The positions API returns positions by day, which is a snapshot of the buying and selling activity for that particular day.
      *  ___get_position_netwise___: The positions API positions by net. Net is the actual, current net position portfolio.
      *  ___convert_position___: Convert position API, enable users to convert their open positions from NRML intra-day to Short term MIS or vice versa, provided that there is sufficient margin or funds in the account to effect such conversion.
      *  ___cancel_order___: This API can be called to cancel any open order of the user by providing correct appOrderID matching with the chosen open order to cancel.
      *  ___cancelall_order___: This API can be called to cancel all open order of the user by providing exchange segment and exchange instrument ID.
      *  ___place_cover_order___: A Cover Order is an advance intraday order that is accompanied by a compulsory Stop Loss Order. This helps users to minimize their losses by safeguarding themselves from unexpected market movements. A Cover Order offers high leverage and is available in Equity Cash, Equity F&O, Commodity F&O and Currency F&O segments. It has 2 orders embedded in itself, they are Limit/Market Order Stop Loss Order.
      *  ___exit_cover_order___: Exit Cover API is a functionality to enable user to easily exit an open stoploss order by converting it into Exit order.
      *  ___squareoff_position___: User can request square off to close all his positions in Equities, Futures and Option. Users are advised to use this request with caution if one has short term holdings.
      *  ___get_order_history___: Order history will provide particular order trail chain. This indicate the particular order & its state changes. i.e.Pending New to New, New to PartiallyFilled, PartiallyFilled, PartiallyFilled & PartiallyFilled to Filled etc.
      *  ___interactive_logout___: This call invalidates the session token and destroys the API session. After this, the user should go through login flow again and extract session token from login response before further activities.

*  The __Market Data API__ gives the user access to 
      *  ___marketdata_login___: Send the login url to which a user should receive the token.
      *  ___get_config___: Get the configuration of the client.
      *  ___get_quote___: Get the quote of the instrument.
      *  ___send_subscription___: Send subscription for the instrument.
      *  ___send_unsubscription___: Send unsubscription for the instrument.
      *  ___get_master___: Get the master string.
      *  ___get_ohlc___: Get the OHLC of the instrument.
      *  ___get_series___: Get the series of the exchange segment.
      *  ___get_equity_symbol___: Get the equity symbol of the exchange segment.
      *  ___get_expiry_date___: Get the expiry date of the exchange segment.
      *  ___get_future_symbol___: Get the future symbol of the exchange segment.
      *  ___get_option_symbol___: Get the option symbol of the exchange segment.
      *  ___get_option_type___: Get the option type of the exchange segment.
      *  ___get_index_list___: Get the index list of the exchange segment.
      *  ___search_by_instrumentid___: Search by instrument id.
      *  ___search_by_scriptname___: Search by script name.
      *  ___marketdata_logout___: This call invalidates the session token and destroys the API session.
# How To Guide for Package


### Introduction.
Some basic methods have been listed here with example. Please refer to ___Explanation___ for list of every single function/method available in the package. 

### ___Instantiate XTS class into object before login.___

In the below code, we are trying to instantiating XTSConnect for marketdata API. The same can be done for Interactive API as well.
```
from xts_api_client.xts_connect import XTSConnect

xt_market_data = XTSConnect(
    apiKey = market_data_API_key,
    secretKey = market_data_API_secret,
    source = API_source,
    root = API_root
)

```

### ___Logging in.___

After instantiating XTSconnect. Use the method marketdata login to log in & access data.
```
response_marketdata_login = xt.marketdata_login()
```

If the credentials are correct, printing 'response_marketdata_login' will five a JSON like following.

{'type': 'success', 'code': 'e-response-0010', 'description': 'Provided Valid Credentials', 'result': {'token': ___your_token___, 'userID': ___your_userID___, 'appVersion': ___your_appVersion___, 'application_expiry_date': ___your_application_expiry_date___}}

### ___Getting Configuration.___

Once you have loggin in, you can get the configuration for the market data.
```
market_data_get_config = xt_market_data.get_config()
```

Printing the 'market_data_get_config' will give JSON like following.

```
{'type': 'success', 'code': 's-response-0001', 'description': 'Fetched configurations successfully', 'result': {'exchangeSegments': {'NSECM': 1, 'NSEFO': 2, 'NSECD': 3, 'NSECO': 4, 'SLBM': 5, 'NIFSC': 7, 'BSECM': 11, 'BSEFO': 12, 'BSECD': 13, 'BSECO': 14, 'NCDEX': 21, 'MSECM': 41, 'MSEFO': 42, 'MSECD': 43, 'MCXFO': 51}, 'xtsMessageCode': {'touchlineEvent': 1501, 'marketDepthEvent': 1502, 'indexDataEvent': 1504, 'candleDataEvent': 1505, 'openInterestEvent': 1510, 'instrumentPropertyChangeEvent': 1105, 'ltpEvent': 1512}, 'publishFormat': ['Binary', 'JSON'], 'broadCastMode': ['Full', 'Partial'], 'instrumentType': {'1': 'Futures', '2': 'Options', '4': 'Spread', '8': 'Equity', '16': 'Spot', '32': 'PreferenceShares', '64': 'Debentures', '128': 'Warrants', 
'256': 'Miscellaneous', '512': 'MutualFund', 'Futures': 1, 'Options': 2, 'Spread': 4, 'Equity': 8, 'Spot': 16, 'PreferenceShares': 32, 'Debentures': 64, 'Warrants': 128, 'Miscellaneous': 256, 'MutualFund': 512}}}
```

### ___Getting the Master Data.___

XTS provides you API Call to fetch all tradable as well as some additional Instrument/contract masters in a single structure. This call can be made once in a day and the response can be persisted in local storage or file as per you application design and you can fetch instrumented or Symbols from this dataset throughout the day.The type of _master_ is a dictionary, that contains all the data sepearted by "|"
```
market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM]
    )
```

A snippet of print of market_data_get_master.
```
nNSECM|11369|8|TTKHLTCARE|TTKHLTCARE-EQ|EQ|TTKHLTCARE-EQ|1100100011369|1798.7|1199.2|66709|0.05|1|1|TTKHLTCARE|INE910C01018|1|1|TTK HEALTHCARE LIMITED-EQ|0|-1|-1\nNSECM|20364|8|771KL43|771KL43-SG|SG|771KL43-SG|1100100020364|102.37|92.62|1025599|0.01|100|1|771KL43|IN2020230172|1|1|SDL KL 7.71% 2043-SG|0|-1|-1\nNSECM|21711|8|68PN26|68PN26-SG|SG|68PN26-SG|1100100021711|108.7|98.35|965899|0.01|100|1|68PN26|IN2820200052|1|1|SDL PN 6.8% 2026-SG|0|-1|-1'
```

### ___Getting the OHLC Data.___

The data is available in the form of a candle timestamp with epoch from 1970, Open, High, Low, Close, Volume, OI. The least compression available is 60(1 minute) for both event stream and long polling (GET at 1 Request Per Second). Other supported intervals for GET (long polling ) Request are 2 minute, 3 minutes, 5 minutes, 15 minutes, 30 minutes , hourly and daily.

```
marget_data_get_ohlc = xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM,
    exchangeInstrumentID = 22,
    startTime = "Dec 02 2024 091500",
    endTime = "Dec 02 2024 093000'",
    compressionValue = 1)
```

printing market_data_get_ohlc will give a dictionary, as shown below.

{'type': 'success', 'code': 's-instrument-0002', 'description': 'Data found', 'result': {'exchangeSegment': 'NSECM', 'exchangeInstrumentID': '22', 'dataReponse': ''}}

# Reference
*  This is a python client package for XTS API. XTS is product from [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/).The original documentation for XTS Clinet is [___linked here___](https://symphonyfintech.com/xts-market-data-front-end-api-v2/).

*  This package is a __derivative work__ of the original package written by [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/).
*  [Link for original GitHub Repository](https://github.com/symphonyfintech/xts-pythonclient-api-sdk). It takes inspirations from the original, however it differs in the implimentation.

* Link to [___pypiserver___](https://pypi.org/project/pypiserver/) for hosting the package locally.