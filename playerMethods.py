from serverConnection import db

#logs in with username and password
def login(name):
	x = db.prepare("SELECT id, username, displayname from users where username = $1::Text limit 1;")(name)

	if not x:
		return None

	return dict(x[0]);

#TODO: finish this
#currently just grabs game IDs 
def getGames(playerID):
	x = db.prepare("SELECT games from users where id = $1::integer limit 1;")(playerID)

	if not x:
		return None

	return dict(x[0]["games"]);

#Add a user to the list of users
def addUser(username):
	x = db.prepare("SELECT id from users where username = $1::Text limit 1;")(username)

	if x:
		return 0

	x = db.prepare("INSERT INTO users (username, id) VALUES ($1::Text, DEFAULT) RETURNING id, username;")(username)[0]

	return {'id':x[0], 'username':x[1]}

#update a users display name
def updateDisplayName(pid, nstr):
	x = db.prepare("UPDATE users SET displayname = $1::Text WHERE id = $2::integer RETURNING id, username, displayname")(nstr, pid)

	if not x:
		return False

	return {'id':x[0][0], 'username':x[0][1], 'displayname':x[0][2]}