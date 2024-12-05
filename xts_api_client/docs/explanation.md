# Explanation
* The user should have ___API Key___, ___API Secret Key___ & the ___URL___ with ___Port___ details for using this package.
* XTS API is a REST based Trading API with ___Socket IO___ streaming component. This client makes it easier to consume the data from API into Python.
* In XTS, there are two types of API, one for __trading (interactive sessions)__ & one for __market data__.

## [Trading API](https://symphonyfintech.com/xts-trading-front-end-api-v2/)
* Trading APIs allows to integrate trading system with XTS Platform for placing orders, monitor your positions, manage your portfolio and much more.
## [Market Data API](https://symphonyfintech.com/xts-market-data-front-end-api-v2/#section/Authentication)
* Market Data API is a mixed HTTP REST and HTTP streaming API. It provides access to live quotes data on a wide range of symbols.

## __Steps to use the Package__
## ___Step 1. Instantiate XTS class into object before login.___
* Import _class_ 'XTSConnect' & then instantiate it as shown.
* Write your apikey, secretkey, source & root. Root is the URL with port included.

```
from xts_api_client.xts_connect import XTSConnect

xt_market_data = XTSConnect(
    apiKey = market_data_API_key,
    secretKey = market_data_API_secret,
    source = API_source,
    root = API_root
)
```
## ___Step 2. Logging in.___

* As mentioned earlier, there are two types of API in XTS. The below example is for market data API.
* After instantiating XTSConnect. Use the method marketdata login to log in & access data.

```
response_marketdata_login = xt_market_data_marketdata_login()
```

If the credentials are correct, printing 'response_marketdata_login' will five a JSON like following.
```
{'type': 'success', 'code': 'e-response-0010', 'description': 'Provided Valid Credentials', 'result': {'token': data removed, 'userID': data removed, 'appVersion': data removed, 'application_expiry_date': data removed}}
```
## ___Step 3. Getting Configuration.___

* Once you have logged in through market_data_API, you can get the configuration for the market data.
```
market_data_get_config = xt_market_data.get_config()
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
market_data_get_master = xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM]
    )
```
* Both above & below code will give same result. 
```
market_data_get_master = xt_market_data.get_master(
      exchangeSegmentList = ['NSECM']
      )
```

A snippet of print of market_data_get_master.
```
...nNSECM|11369|8|TTKHLTCARE|TTKHLTCARE-EQ|EQ|TTKHLTCARE-EQ|1100100011369|1798.7|1199.2|66709|0.05|1|1|TTKHLTCARE|INE910C01018|1|1|TTK HEALTHCARE LIMITED-EQ|0|-1|-1\nNSECM|20364|8|771KL43|771KL43-SG|SG|771KL43-SG|1100100020364|102.37|92.62|1025599|0.01|100|1|771KL43|IN2020230172|1|1|SDL KL 7.71% 2043-SG|0|-1|-1\nNSECM|21711|8|68PN26|68PN26-SG|SG|68PN26-SG|1100100021711|108.7|98.35|965899|0.01|100|1|68PN26|IN2820200052|1|1|SDL PN 6.8% 2026-SG|0|-1|-1'}
```
* __We can make a DataFrame of master data, using the following code snippet.__

```
import pandas as pd

market_data_get_master = xt_market_data.get_master(exchangeSegmentList=['NSECM'])
col_header = "ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series| NameWithSeries|InstrumentID|PriceBand.High|PriceBand.Low| FreezeQty|TickSize|LotSize|Multiplier|displayName|ISIN|PriceNumerator|PriceDenominator".split("|")
cm_master_df = pd.read_csv(StringIO(market_data_get_master['result']), sep = "|", usecols=range(18), low_memory =False,header=None)
cm_master_df.columns = col_header
print(CM_MASTER_df)
```

## ___Step 5. Getting the OHLC Data.___

* The data is available in the form of a candle timestamp with epoch from 1970, Open, High, Low, Close, Volume, OI.
* The least compression available is 60(1 minute) for both event stream and long polling (GET at 1 Request Per Second).
* Other supported intervals for GET (long polling ) Request are 2 minute, 3 minutes, 5 minutes, 15 minutes, 30 minutes , hourly and daily.
* Format of startTime & endTime is "MMM DD YYYY HHMMSS". In the example given below 091500 means morning nine fifteen in IST. Market open  time :-) .

```
marget_data_get_ohlc = xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM,
    exchangeInstrumentID = 22,
    startTime = "Dec 02 2024 091500",
    endTime = "Dec 02 2024 093000",
    compressionValue = 60)
```

Printing market_data_get_ohlc will give a dictionary, as shown below.

```
{'type': 'success', 'code': 's-instrument-0002', 'description': 'Data found', 'result': {'exchangeSegment': 'NSECM', 'exchangeInstrumentID': '22', 'dataReponse': 'data removed'}}
```

* From the DataFrame made above (in master data section), user can select different instruments & can gain further insight.