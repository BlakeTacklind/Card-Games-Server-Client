from messageHandling import getReturnMessage
import json
from errorMessages import ERROR
from safety import *
from autobahn.asyncio.websocket import WebSocketServerProtocol

class MyServerProtocol(WebSocketServerProtocol):
	# clients = set()
	users = set()
	rooms = dict()
	zones = dict()

	def onConnect(self, request):
		print("Client connecting: {0}".format(request.peer))

	def onOpen(self):
		# MyServerProtocol.clients.add(self)
		print("WebSocket connection open.")

	def onClose(self, wasClean, code, reason):
		# MyServerProtocol.clients.remove(self)
		# self.removeFromUsers()
		print("WebSocket connection closed: {0}".format(reason))
		

	def onMessage(self, payload, isBinary):
		self.sendMessage(getReturnMessage(payload))
		# MyServerProtocol.sendAllClients(getReturnMessage(payload))
		# res = self.unpackMessage(payload)
		# if res is None:
		# 	return

		# (rq, args) = res

		

	#Non robust adding to set of users
	def addToUsers(self):
		self.inUsers = True
		MyServerProtocol.users.add(self)

		self.zones = set()

	def removeFromUsers():
		if self.inUsers:
			MyServerProtocol.users.remove(self)
			self.inUsers = False

	def addToZone(self, id):
		if id not in MyServerProtocol.zones:
			zones[id] = set()

		self.zones.add(id)
		MyServerProtocol.zones[id].add(self)

	def removeFromZone(self, id):
		# if id in self.zones:
		self.zones.remove(id)
		MyServerProtocol.zones[id].remove(self)

		if not bool(MyServerProtocol.zones[id]):
			MyServerProtocol.zones.pop(id, None)

	def unpackMessage(self, payload):
		#need to check if messag is a json
		raw = payload.decode('utf8')

		try:
			message = json.loads(raw)
		except ValueError:
			self.sendMessage(json.dumps(ERROR.badJSON).encode('utf8'))
			return None

		print(message)

		#need to check if there IS a rq
		if 'rq' in message:
			rq = message['rq']
		else:
			self.sendMessage(json.dumps(ERROR.noRQ).encode('utf8'))
			return None

		#need to check that rq is an int
		if type(rq) is not int:
			self.sendMessage(json.dumps(ERROR.badTypeRQ).encode('utf8'))
			return None

		#need to check if there IS a ag
		if 'ag' not in message:
			self.sendMessage(json.dumps(ERROR.noAG).encode('utf8'))
			return None

		return (rq, message['ag'])


	@classmethod
	def sendAllClients(cls, mes):
		for client in cls.clients:
			try:
				client.sendMessage(mes)
			except:
				logging.error("Error sending message", exc_info=True)

