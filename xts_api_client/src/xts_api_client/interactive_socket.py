import socketio
from xts_api_client.interactive_socket_client import InteractiveSocketClient

class OrderSocket_io(socketio.AsyncClient):
    def __init__(self,
                 token,
                 userID,
                 root_url,
                 port,
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
        self.port = port

        self.connection_url = f"{self.root_url}:{self.port}?token={self.token}&userID={self.userID}&apiType=INTERACTIVE"
        #self.connection_url = port + self.token + '&userID=' + self.userID + "&apiType=INTERACTIVE"

    async def connect(self, headers={}, transports='websocket', namespaces=None, socketio_path='/interactive/socket.io',
                verify=False):
        """Connected to the socket."""
        self.connect(self.connection_url, headers, transports, namespaces, socketio_path)
        

    async def get_emitter(self):
        """For getting event listener"""
        return self.eventlistener
