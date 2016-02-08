from serverProtocol import MyServerProtocol
from autobahn.asyncio.websocket import WebSocketServerFactory

import asyncio

myPort = 11337

if __name__ == '__main__':

	factory = WebSocketServerFactory(u"ws://127.0.0.1:{}".format(myPort), debug=False, externalPort = 80)
	factory.protocol = MyServerProtocol

	socket_filepath = "/home/blake/cards.sock"
	loop = asyncio.get_event_loop()
	coro = loop.create_server(factory, '127.0.0.1', myPort)
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		server.close()
		loop.close()

