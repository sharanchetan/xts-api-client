# Introduction

* This package is written to be used as a XTS API Client in Python.
* With the correct API credentials, User can access XTS interactive & market data.

# Reference
*  This is a python client package for XTS API. XTS is product from [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/) The original documentation for XTS Client is [___linked here___](https://symphonyfintech.com/xts-market-data-front-end-api-v2/).

*  This package is a __derivative work__ of the original package written by [Symphony Fintech Solutions Pvt. Ltd.](https://symphonyfintech.com/)
*  [Link for original GitHub Repository](https://github.com/symphonyfintech/xts-pythonclient-api-sdk). It takes inspirations from the original, however it differs in the implementation.

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

There are two version of xts_connect. A __synchronous__ version & an __asynchronous__ version.

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

## __A Simple Example__

* Here's an example code block that loads API credentials from environment variables and uses them to log in to a MarketData API. It has been explained in subsequent steps.

```
import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")

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