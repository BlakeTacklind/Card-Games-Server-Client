from serverConnection import db
from random import shuffle
import re
from viewOptions import *


def copyDeckToZone(deckNum, zoneNum):
    c = db.prepare("SELECT cards FROM \"presetZones\" WHERE \"id\" = $1::integer;")(deckNum)

    if not c:
        return False

    c = list(c[0]["cards"])

    #shuffle(c)
    
    x = db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer;")(c, zoneNum)[1]

    if x == 1:
        return True

    return False

def gCDTZ(gNum, dNum, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return copyDeckToZone(dNum, game[zNum]["id"])

#shuffle the conents of a zone
def shuffleZone(zoneNum):
    x = db.prepare("SELECT cards FROM zones WHERE \"id\" = $1::integer;")(zoneNum)

    if not x:
        return False

    x=list(x[0][0])
    shuffle(x)

    db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer;")(x, zoneNum)

    return True

def gSZ(gNum, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return shuffleZone(dNum, game[zNum]["id"])

def moveCardBetweenZones(cardPos, fromZ, toZ, cardPlace):
    if (cardPos < 0):
        return False

    c = db.prepare("SELECT cards, game FROM zones WHERE \"id\" = $1::integer;")(fromZ)

    if not c:
        return False

    c = c[0]

    if (len(c["cards"]) <= cardPos):
        return False

    a = db.prepare("SELECT cards FROM zones WHERE id = $1::integer AND game = $2::integer;")(toZ, c["game"])

    if not a:
        return False

    a = list(a[0]["cards"])

    if (len(a) < cardPlace):
        return False

    a.insert(cardPlace, c["cards"][cardPos])

    #print(a)

    x = db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer AND game = $3::integer;")(a, toZ, c["game"])[1]
    
    if x == 0:
        return False

    c = list(c["cards"])

    del c[cardPos]

    db.prepare("UPDATE zones SET cards = $1 WHERE \"id\" = $2;")(c, fromZ)

    return True

def gMCBZ(gNum, pos, fZ, tZ, plc):
    return False

def moveTopToBackOfZones(fromZ, toZ):
    if (cardPos < 0):
        return False

    c = db.prepare("SELECT cards, game FROM zones WHERE \"id\" = $1::integer;")(fromZ)

    if not c:
        return False

    c = c[0]

    if (len(c["cards"]) < 1):
        return False

    x = db.prepare("UPDATE zones SET cards = array_append(zones.cards, $1) WHERE \"id\" = $2 AND game = $3;")(c["cards"][0], toZ, c["game"])[1]
    if x == 0:
        return False

    c = list(c["cards"])

    del c[0]

    db.prepare("UPDATE zones SET cards = $1 WHERE \"id\" = $2;")(c, fromZ)

    return True


def gMTTBOZ(gNum, fZ, tZ):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return moveTopToBackOfZones(game[fZ]["id"], game[tZ]["id"])

def goMTTBOZ(gNum, ownerF, fZ, tZ):
    player = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerF)
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not player or not game:
        return False

    return moveTopToBackOfZones(player[fZ]["id"], game[tZ]["id"])


def gMTTBOZo(gNum, ownerT, fZ, tZ):
    player = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerT)
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not player or not game:
        return False

    return moveTopToBackOfZones(game[fZ]["id"], player[tZ]["id"])

def goMTTBOZo(gNum, ownerF, ownerT, fZ, tZ):
    player1 = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerF)
    player2 = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerT)

    if not player1 or not player2:
        return False

    return moveTopToBackOfZones(player1[fZ]["id"], player2[tZ]["id"])


#move a card from a spot in a zone to another spot in the zone
def moveCardInZone(zoneNum, moveFrom, moveTo):
    x = db.prepare("SELECT cards FROM zones WHERE id = $1::integer;")(zoneNum)

    if not x:
        return False
    
    x = list(x[0]["cards"])

    if moveTo >= len(x) or moveFrom >= len(x):
        return False

    x.insert(moveTo, x.pop(moveFrom))

    db.prepare("UPDATE zones SET cards = $1::integer[] WHERE id = $2::integer;")(x, zoneNum)

    return True

#print('move card', moveCardInZone(2,0,2))

def funcExec(funcArr, gNum):
    func = db.prepare("SELECT code, args FROM funcs WHERE id = $1::integer;")(funcArr[0])

    if not func:
        return -1
    
    func = func[0]

    if len(funcArr) <= func["args"]:
        return -2

    fstr = re.sub(r"\$0", str(gNum), func["code"])

    for i in range(1, func["args"]+1):
        fstr = re.sub(r"\$"+str(i), str(funcArr[i]), fstr)

    exec(fstr)

    return func["args"]

print(funcExec([1,1,0], 13))

#OVERALL GAME FUNCTIONS
def startGame(playerList, gameType, instanceName):
    if not playerList:
        return False

    #find users with ids passed
    p = db.prepare("SELECT id, username, displayname FROM users WHERE \"id\" = any($1::integer[]);")(playerList)
    
    if len(p) != len(playerList):
        return False

    #find game type by id
    t = db.prepare("SELECT \"playerZones\", \"pubZones\", \"initFunc\" FROM \"gameTypes\" WHERE \"id\" = $1::integer;")(gameType)
    if not t:
        return False

    gn = db.prepare("INSERT INTO \"gameInstance\" (\"name\", players, \"type\") VALUES ($1::Text, $2::integer[], $3::integer) RETURNING \"id\";")(instanceName, playerList, gameType)[0][0]

    pubid = list()

    for z in t[0]["pubZones"]:
        pubid.append(db.prepare("INSERT INTO zones (\"name\", game) VALUES ($1::text, $2::integer) RETURNING id;")(z, gn)[0]["id"])

    #print(pubid)

    privzid = list()
    numplayZones = len(t[0]["playerZones"])

    for i, username, displayname in p:
        n = displayname
        if not displayname:
            n = username

        tempZ = list()

        for z in t[0]["playerZones"]:
            tempZ.append(db.prepare("INSERT INTO zones (\"name\", game, owner) VALUES ($1::text, $2::integer, $3::integer) RETURNING id;")(n+"'s "+z, gn, i)[0]["id"])

        privzid.append(tempZ)

    #print(privzid)

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

#print(startGame([1,2], 1, 'test'))

#Delete a current game from the system
def killGame(gameNum):
    x = db.prepare("DELETE FROM \"gameInstance\" WHERE \"id\" = $1::integer;")(gameNum)
    #print(str(x))
    if int(x[1]) == 1:
        return True

    return False


