import postgresql
from random import shuffle

conString = "pq://cardsDatabase:tN6Y6RUZyp5J7T3bLdru@serenity.isozilla.com:5432/cardsDatabase?[sslmode]=require"

db = postgresql.open(conString)


def startGame(playerList, gameNumber, instanceName):
    if not playerList:
        return False

    #find users with ids passed
    p = db.prepare("SELECT username, displayname FROM users WHERE \"id\" = " + 
        " OR \"id\" = ".join(str(x) for x in playerList) + ";")()
    
    if len(p) != len(playerList):
        return False

    #find game type by id
    t = db.prepare("SELECT \"playerZones\", \"pubZones\" FROM \"gameTypes\" WHERE \"id\" = $1;")(gameNumber)
    if not t:
        return False

    gn = db.prepare("INSERT INTO \"gameInstance\" (\"name\", players, \"type\") VALUES ($1, $2, $3) RETURNING \"id\";")(instanceName, playerList, gameNumber)[0][0]

    for z in t[0]["pubZones"]:
        db.prepare("INSERT INTO zones (\"name\", game) VALUES ($1, $2);")(z, gn)


    for username, displayname in p:
        n = displayname
        if not displayname:
            n = username

        for z in t[0]["playerZones"]:
            db.prepare("INSERT INTO zones (\"name\", game) VALUES ($1, $2);")(n+"s "+z, gn)



    return True


def copyDeckToZone(deckNum, zoneNum):
    c = db.prepare("SELECT cards FROM \"presetZones\" WHERE \"id\" = $1;")(deckNum)

    if not c:
        return False

    c = list(c[0]["cards"])

    shuffle(c)
    
    x = db.prepare("UPDATE zones SET cards = $1 WHERE \"id\" = $2")(c, zoneNum)[1]

    if x == 1:
        return True

    return False


def moveCardBetweenZones(cardPos, fromZ, toZ):
    if (cardPos < 0):
        return False

    c = db.prepare("SELECT cards, game FROM zones WHERE \"id\" = $1;")(fromZ)

    if not c:
        return False

    c = c[0]

    if (len(c["cards"]) <= cardPos):
        return False

    x = db.prepare("UPDATE zones SET cards = array_append(zones.cards, $1) WHERE \"id\" = $2 AND game = $3;")(c["cards"][cardPos], toZ, c["game"])[1]
    if x == 0:
        return False

    c = list(c["cards"])

    del c[cardPos]

    db.prepare("UPDATE zones SET cards = $1 WHERE \"id\" = $2;")(c, fromZ)

    return True


def shuffleZone(zoneNum):
    x = db.prepare("SELECT cards FROM zones WHERE \"id\" = $1;")(zoneNum)

    if not x:
        return False

    x=list(x[0][0])
    shuffle(x)

    db.prepare("UPDATE zones SET cards = $1 WHERE \"id\" = $2;")(x, zoneNum)

    return True


def killGame(gameNum):
    if db.prepare("DELETE FROM \"gameInstance\" WHERE \"id\" = $1")(gameNum)[1] == 1:
        return True

    return False

print(killGame(2))


def moveMoveInZone(zoneNum, moveFrom, moveTo):
    
