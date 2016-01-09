import json
from errorMessages import ERROR
from safety import *
from DBqueries import *

def getReturnMessage(payload):
	#need to check if messag is a json
	raw = payload.decode('utf8')

	try:
		message = json.loads(raw)
	except ValueError:
		return json.dumps(ERROR.badJSON).encode('utf8')

	print(message)

	#need to check if there IS a rq
	if 'rq' in message:
		rq = message['rq']
	else:
		return json.dumps(ERROR.noRQ).encode('utf8')

	#need to check that rq is an int
	if type(rq) is not int:
		return json.dumps(ERROR.badTypeRQ).encode('utf8')

	#need to check if there IS a ag
	if 'ag' not in message:
		return json.dumps(ERROR.noAG).encode('utf8')


	# Large Switch for different requests from client
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

	return json.dumps(ERROR.UnsupportedRQ(rq)).encode('utf8')

def handleLoginRequest(args):
	if 'username' not in args:
		return ERROR.missingARG(10, 'username')

	username = args["username"]

	if type(username) is not str:
		return ERROR.badTypeARG(10, 'username')

	if not isAlphaStr(username):
		return ERROR.InvalidCharARG(10, 'username')

	res = login(username)
	
	if res == None:
		return {'rq':12, 'ag':args}

	return {'rq':11, 'ag':res}

def handleNewPlayerRequest(args):
	if 'username' not in args:
		return ERROR.missingARG(20, 'username')

	username = args["username"]

	if type(username) is not str:
		return ERROR.badTypeARG(20, 'username')

	if not isAlphaStr(username):
		return ERROR.InvalidCharARG(10, 'username')

	res = addUser(username)
	
	if res == None:
		return {'rq':22, 'ag':args}

	return {'rq':21, 'ag':res}

def handleUpdatePlayerRequest(args):
	if 'name' not in args:
		return ERROR.missingARG(30, 'name')

	newName = args["name"]

	if type(newName) is not str:
		return ERROR.badTypeARG(30, 'name')

	if not isAlphaStr(newName):
		return ERROR.InvalidCharARG(30, 'name')

	if 'id' not in args:
		return ERROR.missingARG(30, 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(30, 'id')

	res = updateDisplayName(uid, newName)
	
	if res == None:
		return {'rq':32, 'ag':args}

	return {'rq':31, 'ag':res}

def handleGamesRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(100, 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(100, 'id')

	res = playerGamesBad(uid)

	if res == None:
		return {'rq':102, 'ag':res}

	return {'rq':101, 'ag':res}

def handleGameDataRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(120, 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(120, 'id')

	res = zonesInGame(uid)

	if res == None:
		return {'rq':122, 'ag':res}

	return {'rq':121, 'ag':res}

def handleZoneDataRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(210, 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(210, 'id')

	res = getZoneContents(uid)
	
	if res == None:
		return {'rq':212, 'ag':res}

	return {'rq':211, 'ag':res}

def handleGetPlayers(args):
	return {'rq': 171, 'ag':getPlayers()}

def handleGetGameTypes(args):
	return {'rq': 161, 'ag':getGameTypes()}

def handleCreateGame(args):
	if 'players' not in args:
		return ERROR.missingARG(150, 'players')

	players = args["players"]

	if type(players) is not list:
		return ERROR.badTypeARG(150, 'players')

	if any((type(i) is not int for i in players)):
		return ERROR.badTypeARG(150, 'players')

	if 'type' not in args:
		return ERROR.missingARG(150, 'type')

	gtype = args["type"]

	if type(gtype) is not int:
		return ERROR.badTypeARG(150, 'type')

	if 'name' not in args:
		return ERROR.missingARG(150, 'name')

	newName = args["name"]

	if type(newName) is not str:
		return ERROR.badTypeARG(150, 'name')

	if not isAlphaSpaceStr(newName):
		return ERROR.InvalidCharARG(150, 'name')

	if startGame(players, gtype, newName):
		return {'rq':151,'ag':None}
	return {'rq':152,'ag':None}

def handleShuffleZone(args):
	if 'zone' not in args:
		return ERROR.missingARG(1000, 'zone')

	uid = args["zone"]

	if type(uid) is not int:
		return ERROR.badTypeARG(1000, 'zone')

	if shuffleZone(uid):
		return {'rq':1000,'ag':None}
	return {'rq':999,'ag':1000}

def moveCardSimple(args):
	if 'posF' not in args:
		return ERROR.missingARG(1010, 'posF')

	posF = args["posF"]

	if type(posF) is not int:
		return ERROR.badTypeARG(1010, 'posF')

	if 'fromZ' not in args:
		return ERROR.missingARG(1010, 'fromZ')

	fromZ = args["fromZ"]

	if type(fromZ) is not int:
		return ERROR.badTypeARG(1010, 'fromZ')

	if 'toZ' not in args:
		return ERROR.missingARG(1010, 'toZ')

	toZ = args["toZ"]

	if type(toZ) is not int:
		return ERROR.badTypeARG(1010, 'toZ')

	if 'posT' not in args:
		return ERROR.missingARG(1010, 'posT')

	posT = args["posT"]

	if type(posT) is not int:
		return ERROR.badTypeARG(1010, 'posT')

	if moveCardBetweenZones(posF, fromZ, toZ, posT):
		return {'rq':1010,'ag':None}
	return {'rq':999,'ag':1010}
