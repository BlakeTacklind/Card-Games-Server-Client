import json
from errorMessages import ERROR
from safety import *
from DBqueries import *
from messages import Messages

def handleLoginRequest(args):
	if 'username' not in args:
		return ERROR.missingARG(Messages["LoginReq"], 'username')

	username = args["username"]

	if type(username) is not str:
		return ERROR.badTypeARG(Messages["LoginReq"], 'username')

	if not isAlphaStr(username):
		return ERROR.InvalidCharARG(Messages["LoginReq"], 'username')

	res = login(username)
	
	if res == None:
		return {'rq':Messages["LoginFail"], 'ag':args}

	return {'rq':Messages["LoginSuccess"], 'ag':res}

def handleNewPlayerRequest(args):
	if 'username' not in args:
		return ERROR.missingARG(Messages["NewPlayer"], 'username')

	username = args["username"]

	if type(username) is not str:
		return ERROR.badTypeARG(Messages["NewPlayer"], 'username')

	if not isAlphaStr(username):
		return ERROR.InvalidCharARG(Messages["LoginReq"], 'username')

	res = addUser(username)
	
	if res == None:
		return {'rq':Messages["NewPlayerFail"], 'ag':args}

	return {'rq':Messages["NewPlayerSuccess"], 'ag':res}

def handleUpdatePlayerRequest(args):
	if 'name' not in args:
		return ERROR.missingARG(Messages["ChangeNameRQ"], 'name')

	newName = args["name"]

	if type(newName) is not str:
		return ERROR.badTypeARG(Messages["ChangeNameRQ"], 'name')

	if not isAlphaStr(newName):
		return ERROR.InvalidCharARG(Messages["ChangeNameRQ"], 'name')

	if 'id' not in args:
		return ERROR.missingARG(Messages["ChangeNameRQ"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["ChangeNameRQ"], 'id')

	res = updateDisplayName(uid, newName)
	
	if res == None:
		return {'rq':Messages["ChangeNameRQFail"], 'ag':args}

	return {'rq':Messages["ChangeNameRQSuccess"], 'ag':res}

def handleGamesRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["GetGameList"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["GetGameList"], 'id')

	res = playerGamesBad(uid)

	if res == None:
		return {'rq':Messages["GetGameListFail"], 'ag':res}

	return {'rq':Messages["GetGameListSuccess"], 'ag':res}

def handleGameDataRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["GetGameData"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["GetGameData"], 'id')

	res = zonesInGame(uid)

	if res == None:
		return {'rq':Messages["GetGameDataFail"], 'ag':res}

	return {'rq':Messages["GetGameDataSuccess"], 'ag':res}

def handleZoneDataRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["GetGameZoneAllData"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["GetGameZoneAllData"], 'id')

	res = getZoneContents(uid)
	
	if res == None:
		return {'rq':Messages["GetGameZoneAllDataFail"], 'ag':res}

	return {'rq':Messages["GetGameZoneAllDataSuccess"], 'ag':res}

def handleZoneDataRequestAndExtra(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["GetGameZoneAllData"], 'id'), None

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["GetGameZoneAllData"], 'id'), None

	res, extra = getZoneContentsAndExtra(uid)
	
	if res == None:
		return {'rq':Messages["GetGameZoneAllDataFail"], 'ag':None}, None

	return {'rq':Messages["GetGameZoneAllDataSuccess"], 'ag':res}, extra

def handleGetPlayers(args):
	return {'rq': Messages["GetAllOtherPlayersSuccess"], 'ag':getPlayers()}

def handleGetGameTypes(args):
	return {'rq': Messages["GetGameTypesSuccess"], 'ag':getGameTypes()}

def handleCreateGame(args):
	if 'players' not in args:
		return ERROR.missingARG(Messages["CreateNewGame"], 'players')

	players = args["players"]

	if type(players) is not list:
		return ERROR.badTypeARG(Messages["CreateNewGame"], 'players')

	if any((type(i) is not int for i in players)):
		return ERROR.badTypeARG(Messages["CreateNewGame"], 'players')

	if 'type' not in args:
		return ERROR.missingARG(Messages["CreateNewGame"], 'type')

	gtype = args["type"]

	if type(gtype) is not int:
		return ERROR.badTypeARG(Messages["CreateNewGame"], 'type')

	if 'name' not in args:
		return ERROR.missingARG(Messages["CreateNewGame"], 'name')

	newName = args["name"]

	if type(newName) is not str:
		return ERROR.badTypeARG(Messages["CreateNewGame"], 'name')

	if not isAlphaSpaceStr(newName):
		return ERROR.InvalidCharARG(Messages["CreateNewGame"], 'name')

	if startGame(players, gtype, newName):
		return {'rq':Messages["CreateNewGameSuccess"],'ag':None}
	return {'rq':Messages["CreateNewGameFail"],'ag':None}

def handleShuffleZone(args):
	if 'zone' not in args:
		return ERROR.missingARG(Messages["SuffleZoneRQ"], 'zone')

	uid = args["zone"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["SuffleZoneRQ"], 'zone')

	if shuffleZone(uid):
		return {'rq':Messages["SuffleZoneRQ"],'ag':None}
	return {'rq':Messages["ErrorInCardOperation"],'ag':Messages["SuffleZoneRQ"]}

def moveCardSimple(args):
	if 'posF' not in args:
		return ERROR.missingARG(Messages["MoveCardRQ"], 'posF')

	posF = args["posF"]

	if type(posF) is not int:
		return ERROR.badTypeARG(Messages["MoveCardRQ"], 'posF')

	if 'fromZ' not in args:
		return ERROR.missingARG(Messages["MoveCardRQ"], 'fromZ')

	fromZ = args["fromZ"]

	if type(fromZ) is not int:
		return ERROR.badTypeARG(Messages["MoveCardRQ"], 'fromZ')

	if 'toZ' not in args:
		return ERROR.missingARG(Messages["MoveCardRQ"], 'toZ')

	toZ = args["toZ"]

	if type(toZ) is not int:
		return ERROR.badTypeARG(Messages["MoveCardRQ"], 'toZ')

	if 'posT' not in args:
		return ERROR.missingARG(Messages["MoveCardRQ"], 'posT')

	posT = args["posT"]

	if type(posT) is not int:
		return ERROR.badTypeARG(Messages["MoveCardRQ"], 'posT')

	if moveCardBetweenZones(posF, fromZ, toZ, posT):
		return {'rq':Messages["MoveCardRQ"],'ag':None}
	return {'rq':Messages["ErrorInCardOperation"],'ag':Messages["MoveCardRQ"]}

def zoneNotifyString(zid):
	return json.dumps({'rq':Messages["ZoneUpdateNot"], 'ag':zid}).encode('utf8')

def dealCards(args):
	if 'toZarr' not in args:
		return ERROR.missingARG(Messages["dealCards"], 'toZarr')

	toZarr = args["toZarr"]

	if type(toZarr) is not list:
		return ERROR.badTypeARG(Messages["dealCards"], 'toZarr')

	if any((type(i) is not int for i in toZarr)):
		return ERROR.badTypeARG(Messages["dealCards"], 'toZarr')

	if 'fromZ' not in args:
		return ERROR.missingARG(Messages["dealCards"], 'fromZ')

	fromZ = args["fromZ"]

	if type(fromZ) is not int:
		return ERROR.badTypeARG(Messages["dealCards"], 'fromZ')

	if 'num' not in args:
		return ERROR.missingARG(Messages["dealCards"], 'num')

	num = args["num"]

	if type(num) is not int:
		return ERROR.badTypeARG(Messages["dealCards"], 'num')

	if deal(fromZ, toZarr, num):
		return {'rq':Messages["DealCardsRQ"],'ag':None}
	return {'rq':Messages["ErrorInCardOperation"],'ag':Messages["DealCardsRQ"]}

def handleNotificationRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["RequestMessages"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["RequestMessages"], 'id')

	ret = getPlayerNotifications(uid)
	if ret is None:
		return {'rq':Messages["RequestMessagesFail"],'ag':None}
	return {'rq':Messages["RequestMessagesSuccess"],'ag':ret}

def handleMarkReadRequest(args):
	
	if 'mesids' not in args:
		return ERROR.missingARG(Messages["MarkReadRequest"], 'mesids')

	mesids = args["mesids"]

	if type(mesids) is not list:
		return ERROR.badTypeARG(Messages["MarkReadRequest"], 'mesids')

	if any((type(i) is not int for i in mesids)):
		return ERROR.badTypeARG(Messages["MarkReadRequest"], 'mesids')

	if markReadAlot(mesids):
		return {'rq':Messages["MarkReadRequestSuccess"], 'ag': None}

	return {'rq':Messages["MarkReadRequestFail"], 'ag': args}

def handleDeleteNotificationRequest(args):
	if 'id' not in args:
		return ERROR.missingARG(Messages["deleteNotificationRequest"], 'id')

	uid = args["id"]

	if type(uid) is not int:
		return ERROR.badTypeARG(Messages["deleteNotificationRequest"], 'id')

	if deleteNotification(uid):
		return {'rq':Messages["deleteNotificationRequestSuccess"],'ag':args}
	return {'rq':Messages["deleteNotificationRequestFail"],'ag':args}

