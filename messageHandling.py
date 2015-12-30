import json
from DBqueries import *

# print(getGameTypes())

# print(json.dumps(getGameTypes()).encode('utf8'))

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
	res = login(args["username"])
	
	if res == None:
		return {'rq':12, 'ag':args}

	return {'rq':11, 'ag':res}

def handleNewPlayerRequest(args):
	res = addUser(args["username"])
	
	if res == None:
		return {'rq':22, 'ag':args}

	return {'rq':21, 'ag':res}

def handleUpdatePlayerRequest(args):
	res = updateDisplayName(args["id"], args["name"])
	
	if res == None:
		return {'rq':32, 'ag':args}

	return {'rq':31, 'ag':res}

def handleGamesRequest(args):
	res = playerGamesBad(args["id"])

	if res == None:
		return {'rq':102, 'ag':res}

	return {'rq':101, 'ag':res}

def handleGameDataRequest(args):
	res = zonesInGame(args["id"])

	if res == None:
		return {'rq':122, 'ag':res}

	return {'rq':121, 'ag':res}

def handleZoneDataRequest(args):
	res = getZoneContents(args["id"])
	
	if res == None:
		return {'rq':212, 'ag':res}

	return {'rq':211, 'ag':res}

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
