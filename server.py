from cardMethods import *
from playerMethods import *
from messageHandling import getReturnMessage
from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory

myPort = 11337

# sel = selectors.DefaultSelector()

# def accept(sock, mask):
# 	conn, addr = sock.accept()  # Should be ready
# 	print('accepted', conn, 'from', addr)
# 	conn.setblocking(False)
# 	sel.register(conn, selectors.EVENT_READ, read)

# def read(conn, mask):
# 	data = conn.recv(1000)  # Should be ready
# 	if data:
# 		print('echoing', repr(data), 'to', conn)
# 		conn.send(data)  # Hope it won't block
# 	else:
# 		print('closing', conn)
# 		sel.unregister(conn)
# 		conn.close()

# # create an INET, STREAMing socket
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # bind the socket to local host on my socket
# serversocket.bind(('localhost', myPort))
# # become a server socket
# # Accepting up to 100 connections
# serversocket.listen(100)
# serversocket.setblocking(False)
# sel.register(serversocket, selectors.EVENT_READ, accept)

# while True:
# 	events = sel.select()
# 	for key, mask in events:
# 		callback = key.data
# 		callback(key.fileobj, mask)

import asyncio

class MyServerProtocol(WebSocketServerProtocol):

  # @asyncio.coroutine
	def onConnect(self, request):
		print("Client connecting: {0}".format(request.peer))
		# self.sendMessage("print me?")

	def onOpen(self):
		print("WebSocket connection open.")

  # @asyncio.coroutine
	def onMessage(self, payload, isBinary):
		self.sendMessage(getReturnMessage(payload))
  

	def onClose(self, wasClean, code, reason):
		print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':

	factory = WebSocketServerFactory(u"ws://127.0.0.1:{}".format(myPort), debug=False)
	factory.protocol = MyServerProtocol

	loop = asyncio.get_event_loop()
	coro = loop.create_server(factory, '0.0.0.0', myPort)
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		server.close()
		loop.close()

