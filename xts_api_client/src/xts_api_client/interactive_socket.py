import socketio
import json
from xts_api_client.interactive_socket_client import InteractiveSocketClient

class OrderSocket_io(socketio.AsyncClient):
    def __init__(self,
                 token,
                 userID,
                 root_url,
                 interativeSocketClient : InteractiveSocketClient,
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
        self.on('connect', interativeSocketClient.on_connect)
        self.on('message', interativeSocketClient.on_message)
        self.on('joined', interativeSocketClient.on_joined)
        self.on('error', interativeSocketClient.on_error)
        self.on('order', interativeSocketClient.on_order)
        self.on('trade', interativeSocketClient.on_trade)
        self.on('position', interativeSocketClient.on_position)
        self.on('tradeConversion', interativeSocketClient.on_tradeconversion)
        self.on('logout', interativeSocketClient.on_messagelogout)
        self.on('disconnect', interativeSocketClient.on_disconnect)

        self.userID = userID
        self.token = token
        self.root_url = root_url
        self.publishFormat = 'JSON'
        self.broadcastMode = "Full"

        self.connection_url = f"{self.root_url}/?token={self.token}&userID={self.userID}&apiType=INTERACTIVE"
        #self.connection_url = port + self.token + '&userID=' + self.userID + "&apiType=INTERACTIVE"

    async def connect(self, headers={}, transports='websocket', namespaces=None, socketio_path='/interactive/socket.io',
                verify=False):
        """Connected to the socket."""
        self.connect(self.connection_url, headers, transports, namespaces, socketio_path)
        

    async def get_emitter(self):
        """For getting event listener"""
        return self.eventlistener

    async def on_message(self,xts_message):
        """On message from socket"""
        on_message = json.loads(xts_message)
        return on_message

    async def on_joined(self,xts_message):
        """On socket joined"""
        on_joined = json.loads(xts_message)
        return on_joined

    async def on_error(self,xts_message):
        """On receiving error from socket"""
        on_error = json.loads(xts_message)
        return on_error

    async def on_order(self,xts_message):
        """On receiving order placed data from socket"""
        on_order = json.loads(xts_message)
        return on_order

    async def on_trade(self,xts_message):
        """On receiving trade data from socket"""
        on_trade = json.loads(xts_message)
        return on_trade

    async def on_position(self,xts_message):
        """On receiving position data from socket"""
        on_position = json.loads(xts_message)
        return on_position

    async def on_tradeconversion(self,xts_message):
        """On receiving trade conversion data from socket"""
        on_tradeconversion = json.loads(xts_message)
        return on_tradeconversion

    async def on_messagelogout(self,xts_message):
        """On receiving user logout message"""
        on_messagelogout = json.loads(xts_message)
        return on_messagelogout

    async def on_disconnect(xts_message):
        """On receiving disconnection from socket"""
        on_disconnect = json.loads(xts_message)
        return on_disconnect