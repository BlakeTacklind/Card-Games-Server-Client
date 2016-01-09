from messageHandling import *
import json
from errorMessages import ERROR
from safety import *
from autobahn.asyncio.websocket import WebSocketServerProtocol

class MyServerProtocol(WebSocketServerProtocol):
	users = set()
	zones = dict()
	rooms = dict()

	def __init__(self):
		self.inUsers = False
		self.zones = set()

	def onConnect(self, request):
		print("Client connecting: {0}".format(request.peer))

	def onOpen(self):
		print("WebSocket connection open.")

	def onClose(self, wasClean, code, reason):
		self.removeFromUsers()
		self.removeFromAllZones()
		print("WebSocket connection closed: {0}".format(reason))
		

	def onMessage(self, payload, isBinary):
		# self.sendMessage(getReturnMessage(payload))
		# MyServerProtocol.sendAllClients(getReturnMessage(payload))
		res = self.unpackMessage(payload)
		if res is None:
			return

		(rq, args) = res

		self.handleRQ(rq, args)

	def handleRQ(self, rq, args):

		# Large Switch for different requests from client
		if rq == 1010:
			ret = moveCardSimple(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not 999:
				MyServerProtocol.notifyZonesOfUpdate([args['fromZ'], args['toZ']], self)
			return

		if rq == 1000:
			ret = handleShuffleZone(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not 999:
				MyServerProtocol.notifyZonesOfUpdate([args['zone']], self)
			return

		if rq == 10:
			ret = handleLoginRequest(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not 12:
				self.addToUsers()
			return

		if rq == 20:
			ret = handleNewPlayerRequest(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not 22:
				self.addToUsers()
			return

		if rq == 30:
			self.sendMessage(json.dumps(handleUpdatePlayerRequest(args)).encode('utf8'))
			return

		if rq == 100:
			self.sendMessage(json.dumps(handleGamesRequest(args)).encode('utf8'))
			return

		if rq == 120:
			self.sendMessage(json.dumps(handleGameDataRequest(args)).encode('utf8'))
			return

		if rq == 210:
			ret = handleZoneDataRequest(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not 212:
				self.addToZone(args['id'])
			return

		if rq == 150:
			self.sendMessage(json.dumps(handleCreateGame(args)).encode('utf8'))
			return

		if rq == 160:
			self.sendMessage(json.dumps(handleGetGameTypes(args)).encode('utf8'))
			return

		if rq == 170:
			self.sendMessage(json.dumps(handleGetPlayers(args)).encode('utf8'))
			return


	#Notify all vested intrests in zones of mutation to zone, except player that caused it
	@classmethod
	def notifyZonesOfUpdate(cls, zids, player):
		for zid in zids:
			if zid in MyServerProtocol.zones:
				mes = zoneNotifyString(zid)

				for user in MyServerProtocol.zones[zid]:
					if user != player:
						user.sendMessage(mes)


	#Non robust adding to set of users
	def addToUsers(self):
		self.inUsers = True
		MyServerProtocol.users.add(self)


	def removeFromUsers(self):
		if self.inUsers:
			MyServerProtocol.users.remove(self)
			self.inUsers = False

	def addToZone(self, zid):
		if zid not in MyServerProtocol.zones:
			MyServerProtocol.zones[zid] = set()

		self.zones.add(zid)
		MyServerProtocol.zones[zid].add(self)

	def removeFromZone(self, zid):
		# if id in self.zones:
		self.zones.remove(zid)
		MyServerProtocol.zones[zid].remove(self)

		if not bool(MyServerProtocol.zones[zid]):
			MyServerProtocol.zones.pop(zid, None)

	def removeFromAllZones(self):
		for zone in self.zones:
			MyServerProtocol.zones[zone].remove(self)

			if not bool(MyServerProtocol.zones[zone]):
				MyServerProtocol.zones.pop(zone, None)

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
	def sendAllUsers(cls, mes):
		for user in cls.users:
			try:
				user.sendMessage(mes)
			except:
				logging.error("Error sending message", exc_info=True)

