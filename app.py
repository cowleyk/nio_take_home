from socketIO_client import SocketIO
import json
from grocerystats import Grocerystats

# basic socket usage taken from Matt Dodge's example
SOCKET_HOST = 'http://eval.socket.nio.works'

# initiate new class to handle everything
# parameter is type of grocery user wants to track
grocery = Grocerystats(['fruit', 'beverage', 'vegetable'])

with SocketIO(SOCKET_HOST) as sock:
    # Set up our message handler
    sock.on('recvData', grocery.handle_message_two)
    # Join the "fruits" room
    sock.emit('ready', 'groceries')
    # Wait for messages to come through! Ctrl-C to quit
    sock.wait()