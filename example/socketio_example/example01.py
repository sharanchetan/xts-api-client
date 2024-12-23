from xts_api_client.xts_connect import XTSConnect
from xts_api_client.market_data_socket_client import MarketDataSocketClient
from xts_api_client.market_data_socket import MDSocket_io
import os
import time
from dotenv import load_dotenv
import asyncio
import logging
from datetime import datetime


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_directory = r'example\socketio_example\logs'

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger()

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.ERROR) 
# console_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
# console_handler.setFormatter(console_format)
log_filename = os.path.join(log_directory, f"{timestamp}_example.log")  
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG) 
file_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_format)
#logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


Instruments = [
                {'exchangeSegment': 1, 'exchangeInstrumentID': 2885},
                {'exchangeSegment': 1, 'exchangeInstrumentID': 26000},
                {'exchangeSegment': 2, 'exchangeInstrumentID': 51601}
               ]


class XTS_MarketDataSocketClient(MarketDataSocketClient):
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
        # response_1105 = xt.send_subscription(Instruments, 1105)
        # logging.info(f"Subscription Response: {response_1105}")
        response_1501 = xt.send_subscription(Instruments, 1501)
        logging.info(f"Subscription Response: {response_1501}")
        response_1502 = xt.send_subscription(Instruments, 1502)
        logging.info(f"Subscription Response: {response_1502}")
        # response_1505 = xt.send_subscription(Instruments, 1505)
        # logging.info(f"Subscription Response: {response_1505}")
        # response_1507 = xt.send_subscription(Instruments, 1507)
        # logging.info(f"Subscription Response: {response_1507}")
        response_1510 = xt.send_subscription(Instruments, 1510)
        logging.info(f"Subscription Response: {response_1510}")
        response_1512 = xt.send_subscription(Instruments, 1512)
        logging.info(f"Subscription Response: {response_1512}")
        await asyncio.sleep(50)
        await socket.disconnect()
        xt.marketdata_logout()

    async def on_connect(self):
        print("Market Data Socket connected successfully!")

    async def on_disconnect(self):
        print("Market Data Socket disconnected!")

   
    async def on_message(self, data):
        """On receiving message"""
        print('I received a message!' + data)

    async def on_event_market_data_full(self, data):
        """On receiving message code 1502:Market Data full"""
        print('I received a 1502 Market depth message!' + data)

    async def on_event_market_status_full(self, data):
        """On receiving message code 1507:Market Status full"""
        print('I received a 1507 MarketStatus message!' + data)
        
    async def on_event_last_traded_price_full(self, data):
        """On receiving message code 1512:LTP full"""
        print('I received a 1512 LTP message!' + data)

    async def on_event_candle_data_full(self, data):
        """On receiving message code 1505:Candle Data full"""
        print('I received a 1505 Candle data message!' + data)

    async def on_event_openinterest_full(self, data):
        """On receiving message code 1510:OpenInterest full"""
        print('I received a 1510 Open interest message!' + data)

    async def on_event_touchline_full(self, data):
        """On receiving message code 1501:Touchline full"""
        print('I received a 1501 Level1,Touchline message!' + data)

    async def on_event_instrument_change_full(self, data):
        print(f'I received a 1105:Instrument Change full: {data}')

    async def on_event_market_data_partial(self, data):
        """On receiving message code 1502:Market Data partial"""
        print('I received a 1502 Market depth partial message!' + data)
    
    async def on_event_last_traded_price_partial(self, data):
        """On receiving message code 1512:LTP partial"""
        print('I received a 1512 LTP partial message!' + data)
 
    async def on_event_candle_data_partial(self, data):
        """On receiving message code 1505:Candle Data partial"""
        print('I received a 1505 Candle data partial message!' + data)

    async def on_event_openinterest_partial(self, data):
        """On receiving message code 1510:OpenInterest partial"""
        print('I received a 1510 Open interest partial message!' + data)

    async def on_event_touchline_partial(self, data):
        """On receiving message code 1501:Touchline partial"""
        print('I received a 1501 Level1,Touchline partial message!' + data)

    async def on_event_instrument_change_partial(self, data):
        """On receiving message code 1105:Instrument Change partial"""
        print(f'I received a 1105:Instrument Change partial: {data}')

    async def on_error(self, data):
        """Error from the socket"""
        print('I received an error!' + data)
    

# Running the test method in an event loop
async def main():
    pass
    obj = XTS_MarketDataSocketClient()
    await obj.test()
    await asyncio.sleep(5)
    
    

# Execute the async main function
asyncio.run(main())