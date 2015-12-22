from cardMethods import *
from messageHandling import getReturnMessage
from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory

myPort = 11337

import asyncio

class MyServerProtocol(WebSocketServerProtocol):

  # @asyncio.coroutine
  def onConnect(self, request):
    print("Client connecting: {0}".format(request.peer))

  def onOpen(self):
    print("WebSocket connection open.")

  # @asyncio.coroutine
  def onMessage(self, payload, isBinary):
    self.sendMessage(getReturnMessage(payload));
  

  def onClose(self, wasClean, code, reason):
    print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':

  factory = WebSocketServerFactory(u"ws://127.0.0.1:{}".format(myPort), debug=False)
  factory.protocol = MyServerProtocol

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

