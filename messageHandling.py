
import json
from DBqueries import *

# print('zone ', getZoneContents(93))

def getReturnMessage(payload):
	message = json.loads(payload.decode('utf8'))

	# print(message)
	rq = message['rq']

	if rq == 10:
		return json.dumps(handleLoginRequest(message['ag'])).encode('utf8')

	if rq == 100:
		return json.dumps(handleGamesRequest(message['ag'])).encode('utf8')

	if rq == 120:
		return json.dumps(handleGameDataRequest(message['ag'])).encode('utf8')

	if rq == 210:
		return json.dumps(handleZoneDataRequest(message['ag'])).encode('utf8')

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

