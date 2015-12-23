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
        n = displayname
        if not displayname:
            n = username

        tempZ = list()

        for z in t[0]["playerZones"]:
            tempZ.append(db.prepare("INSERT INTO zones (\"name\", game, owner) VALUES ($1::text, $2::integer, $3::integer) RETURNING id;")(z, gn, i)[0]["id"])

        privzid.append(tempZ)

    t = t[0]["initFunc"]

    i = 0
    

    while i < len(t):
        if t[i] == 1:
            if len(t) < i + 2:
                return "bad args!"
    
            if t[i+2] < len(pubid):
                copyDeckToZone(t[i+1], pubid[ t[i+2] ])
            else:
                for lst in privzid:
                    copyDeckToZone(t[i+1], lst[ t[i+2] - len(pudid) ])

            i += 3

        elif t[i] == 2:
            if len(t) < i + 1:
                return "bad args!"

            if t[i+1] < len(pubid):
                shuffleZone(pubid[ t[i+1] ])
            else:
                for lst in privzid:
                    shuffleZone(lst[ t[i+1] - len(pubid) ])
            
            i += 2

        elif t[i] == 3:
            print("unsupported function!")
            
            i += 5

        elif t[i] == 4:
            if len(t) < i + 2:
                return "bad args!"

            zoneFrom = 0

            if t[i+1] < len(pubid):
                zoneFrom = pubid[t[i+1]]
            else:
                print("can't draw from playerzones with init")
            
            if t[i+2] < len(pubid):
                moveTopToBackOfZones(zoneFrom, pubid[t[i+2]])
            else:
                for lst in privzid:
                    moveTopToBackOfZones( zoneFrom, lst[ t[i+2] - len(pubid) ] )

            i += 3

        elif t[i] == 5:
            print("unsuported function!")

            i += 4

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

