import socketio
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
                 binary=False,
                 json=None,
                 **kwargs):
        
        super().__init__(
            reconnection = reconnection,
            reconnection_attempts = reconnection_attempts,
            reconnection_delay = reconnection_delay,
            reconnection_delay_max = reconnection_delay_max,
            randomization_factor = randomization_factor,
            logger = logger,
            binary = binary,
            json = json,
            **kwargs)

        self.eventlistener = self
        self.on('connect', marketdatasocketclient.on_connect)
        self.on('message', marketdatasocketclient.on_message)
        self.on('1501:touchline full', marketdatasocketclient.on_event_touchline_full)
        self.on('1501:touchline partial', marketdatasocketclient.on_event_touchline_partial)
        self.on('1502:market data full', marketdatasocketclient.on_event_market_data_full)
        self.on('1502:market data partial', marketdatasocketclient.on_event_market_data_partial)
        self.on('1505:candle data full', marketdatasocketclient.on_event_candle_data_full)
        self.on('1505:candle data partial', marketdatasocketclient.on_event_candle_data_partial)
        self.on('1507:market status full', marketdatasocketclient.on_event_market_status_full)
        self.on('1510:openinterest full', marketdatasocketclient.on_event_openinterest_full)
        self.on('1510:openinterest partial', marketdatasocketclient.on_event_openinterest_partial)
        self.on('1512:last traded price full', marketdatasocketclient.on_event_last_traded_price_full)
        self.on('1512:last traded price partial', marketdatasocketclient.on_event_last_traded_price_partial)
        self.on('1105:instrument change full', marketdatasocketclient.on_event_instrument_change_full)
        self.on('1105:instrument change partial', marketdatasocketclient.on_event_instrument_change_partial)
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

    async def get_emitter(self):
        """For getting the event listener"""
        return self.eventlistener
