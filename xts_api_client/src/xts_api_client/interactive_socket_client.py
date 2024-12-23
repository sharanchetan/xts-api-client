from typing import Protocol

class InteractiveSocketClient(Protocol):
    async def on_connect(self):
        """Connect from the socket"""
        ...

    async def on_message(self):
        """On message from socket"""
        ...

    async def on_joined(self, data):
        """On socket joined"""
        ...

    async def on_error(self, data):
        """On receiving error from socket"""
        ...

    async def on_order(self, data):
        """On receiving order placed data from socket"""
        ...

    async def on_trade(self, data):
        """On receiving trade data from socket"""
        ...

    async def on_position(self, data):
        """On receiving position data from socket"""
        ...

    async def on_tradeconversion(self, data):
        """On receiving trade conversion data from socket"""
        ...

    async def on_messagelogout(self, data):
        """On receiving user logout message"""
        ...

    async def on_disconnect(self):
        """On receiving disconnection from socket"""
        ...