from messageHandling import *
import json
from errorMessages import ERROR
from safety import *
from autobahn.asyncio.websocket import WebSocketServerProtocol
from messages import Messages

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
		res = self.unpackMessage(payload)
		if res is None:
			return

		(rq, args) = res

		self.handleRQ(rq, args)

	def handleRQ(self, rq, args):

		# Large Switch for different requests from client
		if rq == Messages["MoveCardRQ"]:
			ret = moveCardSimple(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["ErrorInCardOperation"]:
				MyServerProtocol.notifyZonesOfUpdate([args['fromZ'], args['toZ']], self)
			return

		if rq == Messages["DealCardsRQ"]:
			ret = dealCards(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["ErrorInCardOperation"]:
				MyServerProtocol.notifyZonesOfUpdate([args['fromZ']]+args['toZarr'], self)
			return

		if rq == Messages["SuffleZoneRQ"]:
			ret = handleShuffleZone(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["ErrorInCardOperation"]:
				MyServerProtocol.notifyZonesOfUpdate([args['zone']], self)
			return

		if rq == Messages["LoginReq"]:
			ret = handleLoginRequest(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["LoginFail"]:
				self.addToUsers()
				self.playerid = ret['ag']['id']
			return

		if rq == Messages["NewPlayer"]:
			ret = handleNewPlayerRequest(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["NewPlayerFail"]:
				self.addToUsers()
			return

		if rq == Messages["ChangeNameRQ"]:
			self.sendMessage(json.dumps(handleUpdatePlayerRequest(args)).encode('utf8'))
			return

		if rq == Messages["GetGameList"]:
			self.sendMessage(json.dumps(handleGamesRequest(args)).encode('utf8'))
			return

		if rq == Messages["GetGameData"]:
			self.sendMessage(json.dumps(handleGameDataRequest(args)).encode('utf8'))
			return

		if rq == Messages["RequestMessages"]:
			self.sendMessage(json.dumps(handleNotificationRequest(args)).encode('utf8'))
			return

		# if rq == Messages["GetGameZoneAllData"]:
		# 	ret = handleZoneDataRequest(args)
		# 	self.sendMessage(json.dumps(ret).encode('utf8'))
		# 	if 'rq' in ret and ret['rq'] is not Messages["GetGameZoneAllDataFail"]:
		# 		self.addToZone(args['id'])
		# 	return

		if rq == Messages["GetGameZoneAllData"]:
			ret, extra = handleZoneDataRequestAndExtra(args)
			self.sendMessage(json.dumps(ret).encode('utf8'))
			if 'rq' in ret and ret['rq'] is not Messages["GetGameZoneAllDataFail"]:
				self.addToZone(args['id'])
				if extra['owner'] is not self.playerid:
					MyServerProtocol.notifyOfCheat(extra['id'], self.playerid)
			return

		if rq == Messages["CreateNewGame"]:
			self.sendMessage(json.dumps(handleCreateGame(args)).encode('utf8'))
			return

		if rq == Messages["GetGameTypes"]:
			self.sendMessage(json.dumps(handleGetGameTypes(args)).encode('utf8'))
			return

		if rq == Messages["GetAllOtherPlayers"]:
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

	@classmethod
	def notifyOfCheat(cls, zoneid, playerid):
		print(str(zoneid)+' '+str(playerid))
		
		return

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

