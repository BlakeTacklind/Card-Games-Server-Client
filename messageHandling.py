
import json
from DBqueries import *


def getReturnMessage(payload):
	message = json.loads(payload.decode('utf8'))

	rq = message['rq']


	if rq == 10:
		ret = dict()
		res = login(message['ag'][0])
		
		if res == None:
			ret['rq'] = 12
			ret['ag'] = message['ag']
		else:
			ret['rq'] = 11
			ret['ag'] = res

		return json.dumps(ret).encode('utf8')

	# print(message.ag)

	return json.dumps(message).encode('utf8')