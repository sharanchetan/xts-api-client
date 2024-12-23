import socketio
import json
from xts_api_client.market_data_socket_client import MarketDataSocketClient
class MDSocket_io(socketio.AsyncClient):
    def __init__(self,
                 token,
                 userID,
                 root_url,
                 marketdatasocketclient : MarketDataSocketClient,
                 reconnection=True,
                 reconnection_attempts=0,
                 reconnection_delay=1,
                 reconnection_delay_max=50000,
                 randomization_factor=0.5,
                 logger=False,
                 engineio_logger = False, # added 
                 binary=False, #TODO: Investigate investigate its importance.
                 json=None,
                 **kwargs):
        
        super().__init__(
            reconnection = reconnection,
            reconnection_attempts = reconnection_attempts,
            reconnection_delay = reconnection_delay,
            reconnection_delay_max = reconnection_delay_max,
            randomization_factor = randomization_factor,
            engineio_logger = engineio_logger,
            logger = logger,
            #binary = binary, removed because jatin Asked: TODO Investigate
            json = json,
            **kwargs)
    

        self.on('connect', marketdatasocketclient.on_connect)
        self.on('message', marketdatasocketclient.on_message)
        self.on('1501-json-full', marketdatasocketclient.on_event_touchline_full)
        self.on('1501-json-partial', marketdatasocketclient.on_event_touchline_partial)
        self.on('1502-json-full', marketdatasocketclient.on_event_market_data_full)
        self.on('1502-json-partial', marketdatasocketclient.on_event_market_data_partial)
        self.on('1505-json-full', marketdatasocketclient.on_event_candle_data_full)
        self.on('1505-json-partial', marketdatasocketclient.on_event_candle_data_partial)
        self.on('1507-json-full', marketdatasocketclient.on_event_market_status_full)
        self.on('1510-json-full', marketdatasocketclient.on_event_openinterest_full)
        self.on('1510-json-partial', marketdatasocketclient.on_event_openinterest_partial)
        self.on('1512-json-full', marketdatasocketclient.on_event_last_traded_price_full)
        self.on('1512-json-partial', marketdatasocketclient.on_event_last_traded_price_partial)
        self.on('1105-json-full', marketdatasocketclient.on_event_instrument_change_full)
        self.on('1105-json-partial', marketdatasocketclient.on_event_instrument_change_partial)
        self.on('disconnect', marketdatasocketclient.on_disconnect)

        self.root_url = root_url
        self.userID = userID
        self.publishFormat = 'JSON'
        self.broadcastMode = "Full"
        self.token = token
        
        self.connection_url = f"{self.root_url}/?token={self.token}&userID={self.userID}&publishFormat={self.publishFormat}&broadcastMode={self.broadcastMode}"

    async def connect(self, headers={}, transports='websocket', namespaces=None, socketio_path='/apimarketdata/socket.io',
                verify=False):
       
        url = self.connection_url
        """Connected to the socket."""
        await super().connect(url, headers=headers, transports=transports, namespaces=namespaces, socketio_path=socketio_path)
        """Disconnected from the socket."""


    async def on_message(data):
        return ('I received a message!')

    async def on_event_touchline_full(self,data):
        touchline_full = json.loads(data)
        return touchline_full

    async def on_event_market_data_full(self,data):
        market_data_full = json.loads(data)
        return market_data_full
    
    async def on_event_candle_data_full(self,data):
        candle_data_full = json.loads(data)
        return candle_data_full
        
    async def on_event_market_status_full(self,data):
        market_status_full = json.loads(data)
        return market_status_full
    
    async def on_event_openinterest_full(self,data):
        openinterest_full = json.loads(data)
        return openinterest_full
    
    async def on_event_last_traded_price_full(self,data):
        last_traded_price_full = json.loads(data)
        return last_traded_price_full
    
    async def on_event_instrument_change_full(self,data):
        instrument_change_full = json.loads(data)
        return instrument_change_full
    
    def __repr__(self):
        return (f"MDSocket_io("f"token={self.token}"f"userID={self.userID}"f"root_url={self.root_url}"f"reconnection={self.reconnection}")