from serverConnection import db

# returns the contents of a zone as an ordered list of cards
def getZoneContents(zoneNum):
    x = db.prepare("SELECT array_length(cards,1) from zones where id = $1::integer limit 1;")(zoneNum)

    if not x:
        return None

    y = db.prepare("SELECT x, cards.id, cards.name, cards.info, cards.resource from generate_series(1,$1::integer) as x join zones on true join cards on zones.cards[x] = cards.id where zones.id = $2::integer;")(x[0][0], zoneNum)

    x = [{'pos':i[0], 'id':i[1], 'name':i[2], 'info':i[3], 'resource':i[4]} for i in y]
        
    return y

#get list of games the player is in
#TODO: use the player's games list rather then search the whole games list
def playerGamesBad(playerID):
    x = db.prepare("SELECT \"gameInstance\".id, \"gameInstance\".name, \"gameTypes\".name FROM \"gameInstance\", \"gameTypes\" WHERE $1::integer = any(players) AND \"gameInstance\".type = \"gameTypes\".id;")(playerID)

    if not x:
        return None

    x = [{'id':i[0], 'name':i[1], 'type':i[2]} for i in x]
        
    return x


def zonesInGame(gameNum):
    x = db.prepare("SELECT z.id, z.name, u.id, u.displayname, u.username, z.\"defaultState\" FROM zones z LEFT OUTER JOIN users u ON z.owner = u.id WHERE z.game = $1::integer;")(gameNum)

    if not x:
        return None

    x = [{'id':i[0], 'name':i[1], 'owner':i[2], 'ownerd':i[3], 'owneru':i[4], 'ds':i[5]} for i in x]
        
    return x

def zonesInGameByPlayer(playerID, gameNum):
    #Get list of zones in game player can see
    x = db.prepare("SELECT id, name FROM zones WHERE game = $1::integer AND (owner = $2::integer OR owner is null);")(gameNum, playerID)

    if not x:
        return None

    return dict(x)

def getGameTypes():
    x = db.prepare("SELECT id, name, info FROM \"gameTypes\";")()

    x= [{'id':i[0], 'name':i[1], 'info':i[2]} for i in x]
        
    return x

def getPlayers():
    x = db.prepare("SELECT id, username, displayname FROM \"users\";")()

    x = [{'id':i[0], 'username':i[1], 'displayname':i[2]} for i in x]
        
    return x

