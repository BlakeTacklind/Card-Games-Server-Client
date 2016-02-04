from serverConnection import db
from zoneMutators import *


#OVERALL GAME FUNCTIONS
def startGame(playerList, gameType, instanceName):
	if not playerList:
		return False

	#find users with ids passed
	p = db.prepare("SELECT id, username, displayname, games FROM users WHERE \"id\" = any($1::integer[]);")(playerList)
	
	if len(p) != len(playerList):
		return False

	#find game type by id
	t = db.prepare("SELECT \"playerZones\", \"pubZones\", \"initFunc\" FROM \"gameTypes\" WHERE \"id\" = $1::integer;")(gameType)
	if not t:
		return False

	#create game and get game id number
	gn = db.prepare("INSERT INTO \"gameInstance\" (\"name\", players, \"type\") VALUES ($1::Text, $2::integer[], $3::integer) RETURNING \"id\";")(instanceName, playerList, gameType)[0][0]

	#add game to players game list
	for player in p:
		gameList = list(player["games"])
		gameList.append(gn)
		db.prepare("UPDATE users SET games = $1::integer[] WHERE id = $2::integer;")(gameList, player["id"])

	pubid = list()

	for z in t[0]["pubZones"]:
		pubid.append(db.prepare("INSERT INTO zones (\"name\", game) VALUES ($1::text, $2::integer) RETURNING id;")(z, gn)[0]["id"])

	privzid = list()
	numplayZones = len(t[0]["playerZones"])

	for i, username, displayname, games in p:
		# n = displayname
		# if not displayname:
		#	 n = username

		tempZ = list()

		for z in t[0]["playerZones"]:
			tempZ.append(db.prepare("INSERT INTO zones (\"name\", game, owner) VALUES ($1::text, $2::integer, $3::integer) RETURNING id;")(z, gn, i)[0]["id"])

		privzid.append(tempZ)

	t = t[0]["initFunc"]

	i = 0

	return runStartFunctions(t, pubid, privzid)


def runStartFunctions(initFuncs, pubid, privzid):
	i = 0

	while i < len(initFuncs):
		#Copy deck to zone unprompted
		if initFuncs[i] == 1:
			if len(initFuncs) < i + 2:
				return False
	
			if initFuncs[i+2] < len(pubid):
				copyDeckToZone(initFuncs[i+1], pubid[ initFuncs[i+2] ])
			else:
				for lst in privzid:
					copyDeckToZone(initFuncs[i+1], lst[ initFuncs[i+2] - len(pudid) ])

			i += 3

		#shuffle zone
		elif initFuncs[i] == 2:
			if len(initFuncs) < i + 1:
				return False

			if initFuncs[i+1] < len(pubid):
				shuffleZone(pubid[ initFuncs[i+1] ])
			else:
				for lst in privzid:
					shuffleZone(lst[ initFuncs[i+1] - len(pubid) ])
			
			i += 2

		#copy decks to zone prompted
		elif initFuncs[i] == 3:
			zid = 0
			if initFuncs[i+1] < len(pubid):
				zid = pubid[initFuncs[i+1]]
			elif len(privzid) > 0 and initFuncs[i+1] < (len(pubid) + privzid[0]):
				return False
			else:
				return False

			return [zid, initFuncs[i+2:len(initFuncs)], pubid, privzid]
			

		#draw cards
		elif initFuncs[i] == 4:
			if len(initFuncs) < i + 3:
				return False

			zoneFrom = 0

			if initFuncs[i+1] < len(pubid):
				zoneFrom = pubid[initFuncs[i+1]]
			else:
				print("can'initFuncs draw from playerzones with init")
				i += 4
				continue

			num = initFuncs[i+3]

			if initFuncs[i+2] < len(pubid):
				deal(zoneFrom, [pubid[initFuncs[i+2]]], num)
			elif initFuncs[i+2] < (len(pubid) + len(privzid)):
				deal(zoneFrom, [lst[initFuncs[i+2] - len(pubid)] for lst in privzid], num)
			else:
				print("can'initFuncs draw from a zone that doesnt exist!")

			i += 4

		elif initFuncs[i] >= 5:
			print("unsuported function!")

			i += 1

	return True

#Delete a current game from the system
def killGame(gameNum):
	x = db.prepare("DELETE FROM \"gameInstance\" WHERE \"id\" = $1::integer RETURNING players;")(gameNum)

	if len(x) == 0:
		return False

	for player in list(x[0]["players"]):
		games = db.prepare("SELECT games FROM users WHERE \"id\" = $1::integer;")(player)
		gameList = list(games[0]["games"])
		gameList.remove(gameNum)
		db.prepare("UPDATE users SET games = $1::integer[] WHERE id = $2::integer;")(gameList, player)

	return True

