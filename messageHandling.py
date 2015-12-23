
import json

def getReturnMessage(payload):
	message = json.loads(payload.decode('utf8'))

	print(message)

	return json.dumps(message).encode('utf8')