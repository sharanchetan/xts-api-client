from xts_api_client.xts_connect import XTSConnect
from xts_api_client.market_data_socket_client import MarketDataSocketClient
from xts_api_client.market_data_socket import MDSocket_io
import os
import time
from dotenv import load_dotenv
import asyncio


class test_object(MarketDataSocketClient):
    async def test(self):
        load_dotenv()
        API_key = os.getenv("API_KEY")
        API_secret = os.getenv("API_SECRET")
        API_source = os.getenv("API_SOURCE")
        API_root = os.getenv("API_URL")
        xt = XTSConnect(API_key, API_secret, API_source, API_root, disable_ssl=True)
        response = xt.marketdata_login()
        marketDataToken = response["result"]["token"]
        userID = response["result"]["userID"]
        socket = MDSocket_io(marketDataToken, userID, API_root, self)
        await socket.connect()
        await asyncio.sleep(100)
        await socket.disconnect()
        xt.marketdata_logout()

    async def on_connect(self):
        print("Market Data Socket connected successfully!")

    async def on_disconnect(self):
        print("Market Data Socket disconnected!")
    async def on_connect(self):
        """Connect from the socket."""
        ...

    async def on_message(self, data):
        """On receiving message"""
        ...

    async def on_event_market_data_full(self, data):
        """On receiving message code 1502:Market Data full"""
        ...

    async def on_event_market_status_full(self, data):
        """On receiving message code 1507:Market Status full"""
        ...
        
    async def on_event_last_traded_price_full(self, data):
        """On receiving message code 1512:LTP full"""
        ...

    async def on_event_candle_data_full(self, data):
        """On receiving message code 1505:Candle Data full"""
        ...

    async def on_event_openinterest_full(self, data):
        """On receiving message code 1510:OpenInterest full"""
        ...

    async def on_event_touchline_full(self, data):
        """On receiving message code 1501:Touchline full"""
        ...

    async def on_event_instrument_change_full(self, data):
        self.engine_logger.info(f'I received a 1105:Instrument Change Level1, Touchline message: {data}')

    async def on_event_market_data_partial(self, data):
        """On receiving message code 1502:Market Data partial"""
        ...
    
    async def on_event_last_traded_price_partial(self, data):
        """On receiving message code 1512:LTP partial"""
        ...
 
    async def on_event_candle_data_partial(self, data):
        """On receiving message code 1505:Candle Data partial"""
        ...

    async def on_event_openinterest_partial(self, data):
        """On receiving message code 1510:OpenInterest partial"""
        ...

    async def on_event_touchline_partial(self, data):
        """On receiving message code 1501:Touchline partial"""
        ...

    async def on_event_instrument_change_partial(self, data):
        """On receiving message code 1105:Instrument Change partial"""
        ...

    async def on_disconnect(self):
        """Disconnected from the socket"""
        ...

    async def on_error(self, data):
        """Error from the socket"""
        ...
    

# Running the test method in an event loop
async def main():
    pass
    obj = test_object()
    await obj.test()
    await asyncio.sleep(5)
    
    

# Execute the async main function
asyncio.run(main())