from serverConnection import db


def getZoneContents(zoneNum):
    x = db.prepare("SELECT array_length(cards,1) from zones where id = $1::integer limit 1;")(zoneNum)

    if not x:
        return None

    y = db.prepare("SELECT x, cards.id, cards.name, cards.info, cards.resource from generate_series(1,$1::integer) as x join zones on true join cards on zones.cards[x] = cards.id where zones.id = $2::integer;")(x[0][0], zoneNum)

   # print(y)
#    return 0

    lst = list()

    for i in y:
        i = list(i)
        # print(i)
        lst.append({'pos':i[0], 'id':i[1], 'name':i[2], 'info':i[3], 'resource':i[4]})
        
    return lst

#print('cards in zone', getZoneContents(2))

#get list of games the player is in
#TODO: use the player's games list rather then search the whole games list
def playerGamesBad(playerID):
    x = db.prepare("SELECT \"gameInstance\".id, \"gameInstance\".name, \"gameTypes\".name FROM \"gameInstance\", \"gameTypes\" WHERE $1::integer = any(players) AND \"gameInstance\".type = \"gameTypes\".id;")(playerID)

    if not x:
        return None

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'name':i[1], 'type':i[2]})
        
    return lst

#print('player games', playerGames(1))

def zonesInGame(gameNum):
    x = db.prepare("SELECT z.id, z.name, u.id, u.displayname, u.username, z.\"defaultState\" FROM zones z LEFT OUTER JOIN users u ON z.owner = u.id WHERE z.game = $1::integer;")(gameNum)

    if not x:
        return None

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'name':i[1], 'owner':i[2], 'ownerd':i[3], 'owneru':i[4], 'ds':i[5]})
        
    return lst

#print('game zones', zonesInGame(1))

#print('new game?', startGame([1,3],1,'another game'))

def zonesInGameByPlayer(playerID, gameNum):
    #Get list of zones in game player can see
    x = db.prepare("SELECT id, name FROM zones WHERE game = $1::integer AND (owner = $2::integer OR owner is null);")(gameNum, playerID)

    if not x:
        return None

    return dict(x)

#print('plaers zones', zonesInGameByPlayer(1,1))

def getGameTypes():
    x = db.prepare("SELECT id, name, info FROM \"gameTypes\";")()

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'name':i[1], 'info':i[2]})
        
    return lst
#print( getGameTypes())

def getPlayers():
    x = db.prepare("SELECT id, username, displayname FROM \"users\";")()

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'username':i[1], 'displayname':i[2]})
        
    return lst

