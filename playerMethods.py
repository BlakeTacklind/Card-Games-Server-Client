from serverConnection import db

def login(name):
	x = db.prepare("SELECT id, username, displayname from users where username = $1::Text limit 1;")(name)

	if not x:
		return None

	return dict(x[0]);

def getGames(playerID):
	x = db.prepare("SELECT games from users where id = $1::integer limit 1;")(playerID)

	if not x:
		return None

	return dict(x[0]["games"]);

def addUser(username):
	return 0

def updateDisplayName(str):
	return False