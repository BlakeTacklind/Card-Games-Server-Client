
import json
from DBqueries import *

# print('zonesInGame ', updateDisplayName(22, "Blakey"))

def getReturnMessage(payload):
	message = json.loads(payload.decode('utf8'))

	# print(message)
	rq = message['rq']

	if rq == 1010:
		return json.dumps(moveCardSimple(message['ag'])).encode('utf8')

	if rq == 1000:
		return json.dumps(handleShuffleZone(message['ag'])).encode('utf8')

	if rq == 10:
		return json.dumps(handleLoginRequest(message['ag'])).encode('utf8')

	if rq == 20:
		return json.dumps(handleNewPlayerRequest(message['ag'])).encode('utf8')

	if rq == 30:
		return json.dumps(handleUpdatePlayerRequest(message['ag'])).encode('utf8')

	if rq == 100:
		return json.dumps(handleGamesRequest(message['ag'])).encode('utf8')

	if rq == 120:
		return json.dumps(handleGameDataRequest(message['ag'])).encode('utf8')

	if rq == 210:
		return json.dumps(handleZoneDataRequest(message['ag'])).encode('utf8')

	if rq == 150:
		return json.dumps(handleCreateGame(message['ag'])).encode('utf8')

	if rq == 160:
		return json.dumps(handleGetGameTypes(message['ag'])).encode('utf8')

	if rq == 170:
		return json.dumps(handleGetPlayers(message['ag'])).encode('utf8')

	# print(message.ag)

	return json.dumps(message).encode('utf8')

def handleLoginRequest(args):
	ret = dict()
	res = login(args["username"])
	
	if res == None:
		ret['rq'] = 12
		ret['ag'] = args
	else:
		ret['rq'] = 11
		ret['ag'] = res

	return ret

def handleNewPlayerRequest(args):
	ret = dict()
	res = addUser(args["username"])
	
	if res == 0:
		ret['rq'] = 22
		ret['ag'] = args
	else:
		ret['rq'] = 21
		ret['ag'] = res

	return ret

def handleUpdatePlayerRequest(args):
	ret = dict()
	res = updateDisplayName(args["id"], args["name"])
	
	if res == False:
		ret['rq'] = 32
		ret['ag'] = args
	else:
		ret['rq'] = 31
		ret['ag'] = res

	return ret

def handleGamesRequest(args):
	ret = dict()
	res = playerGamesBad(args["id"])
	# print(res)

	if res == None:
		ret['rq'] = 102
		ret['ag'] = res
	else:
		ret['rq'] = 101
		ret['ag'] = res

	return ret

def handleGameDataRequest(args):
	ret = dict()
	res = zonesInGame(args["id"])
	# print(res)

	if res == None:
		ret['rq'] = 122
		ret['ag'] = res
	else:
		ret['rq'] = 121
		ret['ag'] = res

	return ret

def handleZoneDataRequest(args):
	ret = dict()
	res = getZoneContents(args["id"])
	# print(res)

	if res == None:
		ret['rq'] = 212
		ret['ag'] = res
	else:
		ret['rq'] = 211
		ret['ag'] = res

	return ret

def handleGetPlayers(args):
	return {'rq': 171, 'ag':getPlayers()}

def handleGetGameTypes(args):
	return {'rq': 161, 'ag':getGameTypes()}

def handleCreateGame(args):
	if startGame(args["players"], args["type"], args["name"]):
		return {'rq':151,'ag':None}
	return {'rq':152,'ag':None}

def handleShuffleZone(args):
	if shuffleZone(args["zone"]):
		return {'rq':1000,'ag':None}
	return {'rq':999,'ag':1000}

def moveCardSimple(args):
	if moveCardBetweenZones(args['posF'], args['fromZ'], args['toZ'], args['posT']):
		return {'rq':1010,'ag':None}
	return {'rq':999,'ag':1010}
