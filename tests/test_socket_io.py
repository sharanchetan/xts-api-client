import os
import pytest
from dotenv import load_dotenv
from xts_api_client.xts_connect import XTSConnect
from xts_api_client.market_data_socket_client import MarketDataSocketClient
from xts_api_client.market_data_socket import MDSocket_io
import asyncio
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")

xt = XTSConnect(API_key, API_secret, API_source, API_root, disable_ssl=True)
response = xt.marketdata_login()
marketDataToken = response["result"]["token"]
userID = response["result"]["userID"]

XTS_MDSocket = MDSocket_io(
    token = marketDataToken,
    userID = userID,
    root_url = API_root,
    marketdatasocketclient = MarketDataSocketClient
)

Instruments = [
                {'exchangeSegment': 1, 'exchangeInstrumentID': 2885},
                {'exchangeSegment': 1, 'exchangeInstrumentID': 26000},
                {'exchangeSegment': 2, 'exchangeInstrumentID': 51601}
               ]

@pytest.mark.asyncio
async def test_connect():
   result = XTS_MDSocket.connect()
   assert asyncio.iscoroutine(result)
   response = xt.send_subscription(Instruments, 1501)
   assert type(response) == dict
   assert response['type'] == 'success'
   assert response['result']['Remaining_Subscription_Count']<500
   print(response)


   
