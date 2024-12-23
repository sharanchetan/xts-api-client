from typing import Protocol

class MarketDataSocketClient(Protocol):
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
    