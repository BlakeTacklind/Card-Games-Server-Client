
import json
from DBqueries import *


def getReturnMessage(payload):
	message = json.loads(payload.decode('utf8'))

	print(message)
	rq = message['rq']

	if rq == 10:
		return json.dumps(handleLoginRequest(message['ag'])).encode('utf8')

	if rq == 100:
		return json.dumps(handleGamesRequest(message['ag'])).encode('utf8')

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
	res = playerGames(args["id"])
	
	if res == None:
		ret['rq'] = 102
		ret['ag'] = res
	else:
		ret['rq'] = 101
		ret['ag'] = res

	return ret