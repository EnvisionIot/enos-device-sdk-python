class IConnectCallback:

    def on_connect(self):
        """ Called when the connection to the server is completed."""
        print('connect success')

    def on_disconnect(self):
        """ Called when the client connection lost."""
        print('connect lost')

    def on_connect_failed(self):
        """ Called when the client connect failed"""
        print('connect failed...')
