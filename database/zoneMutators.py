from serverConnection import db
from random import shuffle

#Copies the content of a stored deck into a zone
def copyDeckToZone(deckNum, zoneNum):
    c = db.prepare("SELECT cards FROM \"presetZones\" WHERE \"id\" = $1::integer;")(deckNum)

    if not c:
        return False

    c = list(c[0]["cards"])
    
    x = db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer;")(c, zoneNum)[1]

    if x == 1:
        return True

    return False

#Copy the contents of a preset deck (dNum) to a zone (zNum) given the game (gNum) number and no-one ownes the zone
def gCDTZ(gNum, dNum, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return copyDeckToZone(dNum, game[zNum]["id"])

#Copy the contents of a preset deck (dNum) to a zone (zNum) given the game (gNum) number and owner (owner) owns the zone
def goCDTZ(gNum, owner, dNum, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, owner)

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

#shuffle the conents of a zone (zNum) given no-one owns the zone and its in game (gNum)
def gSZ(gNum, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return shuffleZone(dNum, game[zNum]["id"])

#shuffle the conents of a zone (zNum) given owner owns the zone and its in game (gNum)
def goSZ(gNum, owner, zNum):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, owner)

    if not game:
        return False

    return shuffleZone(dNum, game[zNum]["id"])

#move a card in a specific place in a zone to another zone in a specific place
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

    x = db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer AND game = $3::integer;")(a, toZ, c["game"])[1]
    
    if x == 0:
        return False

    c = list(c["cards"])

    del c[cardPos]

    db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer;")(c, fromZ)

    return True

#Move card to zone given no-one owns the zones and its in game (gNum)
def gMCBZ(gNum, pos, fZ, tZ, plc):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return moveCardBetweenZones(pos, game[fZ]["id"], game[tZ]["id"], plc)

#Move card to zone given no-one owns the zones and its in game (gNum)
def goMCBZ(gNum, ownerF, pos, fZ, tZ, plc):
    player = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerF)
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not player or not game:
        return False

    return moveCardBetweenZones(pos, player[fZ]["id"], game[tZ]["id"], plc)

def gMCBZo(gNum, ownerT, pos, fZ, tZ, plc):
    player = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerT)
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not player or not game:
        return False

    return moveCardBetweenZones(pos, game[fZ]["id"], player[tZ]["id"], plc)

def goMCBZo(gNum, pos, fZ, tZ, plc):
    player1 = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerF)
    player2 = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, ownerT)

    if not player1 or not player2:
        return False

    return moveCardBetweenZones(pos, player1[fZ]["id"], player2[tZ]["id"], plc)

def moveTopToBackOfZones(fromZ, toZ):
    if (cardPos < 0):
        return False

    c = db.prepare("SELECT cards, game FROM zones WHERE \"id\" = $1::integer;")(fromZ)

    if not c:
        return False

    c = c[0]

    if (len(c["cards"]) < 1):
        return False

    x = db.prepare("UPDATE zones SET cards = array_append(zones.cards, $1::integer) WHERE \"id\" = $2::integer AND game = $3::integer;")(c["cards"][0], toZ, c["game"])[1]
    if x == 0:
        return False

    c = list(c["cards"])

    del c[0]

    db.prepare("UPDATE zones SET cards = $1::integer[] WHERE \"id\" = $2::integer;")(c, fromZ)

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

def gMCIZ(gNum, zNum, mF, mT):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner IS NULL ORDER BY id;")(gNum)

    if not game:
        return False

    return moveCardInZone(game[zNum]["id"], mF, mT)

def goMCIZ(gNum, owner, zNum, mF, mT):
    game = db.prepare("SELECT id FROM zones WHERE game = $1::integer AND owner = $2::integer ORDER BY id;")(gNum, owner)

    if not game:
        return False

    return moveCardInZone(game[zNum]["id"], mF, mT)

def deal(fromZ, toZarr, num):
    if fromZ in toZarr:
        return False

    dealtFromZone = db.prepare("SELECT cards FROM zones WHERE id = $1::integer;")(fromZ)
    
    if not dealtFromZone:
        return False

    dealtFromZone = list(dealtFromZone[0]["cards"])

    if len(dealtFromZone) is 0:
        return True

    dealtToZones = list(map(getCardsFromZoneUnsafe, toZarr))

    print(dealtToZones)

    if any((i is None for i in dealtToZones)):
        return False
    
    if num < 0 or num*len(toZarr) > len(dealtFromZone):
        for i in range(0, len(dealtToZones)):
            dealtToZones[i] += dealtFromZone[i:len(dealtFromZone):len(dealtToZones)]
            db.prepare("UPDATE zones SET cards = $1::integer[] WHERE id = $2::integer;")(dealtToZones[i], toZarr[i])

        db.prepare("UPDATE zones SET cards = $1::integer[] WHERE id = $2::integer;")([], fromZ)
    else:
        for i in range(0, len(dealtToZones)):
            dealtToZones[i] += dealtFromZone[i:len(toZarr)*num:len(dealtToZones)]
            db.prepare("UPDATE zones SET cards = $1::integer[] WHERE id = $2::integer;")(dealtToZones[i], toZarr[i])

        db.prepare("UPDATE zones SET cards = $1::integer[] WHERE id = $2::integer;")(dealtFromZone[len(toZarr)*num:], fromZ)


    # print(dealtToZones)

    return True

def getCardsFromZoneUnsafe(zid):
    temp = db.prepare("SELECT cards FROM zones WHERE id = $1::integer;")(zid)
    if not temp:
        return None
    return list(temp[0]["cards"])