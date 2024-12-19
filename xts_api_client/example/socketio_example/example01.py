from xts_api_client.xts_connect import XTSConnect
from xts_api_client.market_data_socket_client import MarketDataSocketClient
from xts_api_client.market_data_socket import MDSocket_io
import os
import time
from dotenv import load_dotenv


class test_object(MarketDataSocketClient):
    async def test(self):
        load_dotenv()
        API_key = os.getenv("API_KEY")
        API_secret = os.getenv("API_SECRET")
        API_source = os.getenv("API_SOURCE")
        API_root = os.getenv("API_URL")
        xt = XTSConnect(API_key, API_secret, API_source, API_root)
        response = xt.marketdata_login()
        marketDataToken = response["result"]["token"]
        userID = response["result"]["userID"]
        socket = MDSocket_io(marketDataToken, userID, API_root, self)
        await socket.connect()
        time.sleep(10)
        await socket.disconnect()
        xt.marketdata_logout()

    async def on_connect(self):
        print("Market Data Socket connected successfully!")

    async def on_disconnect(self):
        print("Market Data Socket disconnected!")


obj = test_object()
obj.test()