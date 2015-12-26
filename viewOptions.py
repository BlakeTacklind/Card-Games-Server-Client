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
    x = db.prepare("SELECT id, name, type FROM \"gameInstance\" WHERE $1::integer = any(players);")(playerID)

    if not x:
        return None

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'name':i[1], 'type':i[2]})
        
    return lst

#print('player games', playerGames(1))

def zonesInGame(gameNum):
    x = db.prepare("SELECT id, name, owner, \"defaultState\" FROM zones WHERE game = $1::integer;")(gameNum)

    if not x:
        return None

    lst = list()

    for i in x:
        i = list(i)
        lst.append({'id':i[0], 'name':i[1], 'owner':i[2], 'ds':i[3]})
        
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
    x = db.prepare("SELECT id, name FROM \"gameTypes\";")()

    return dict(x)

#print( getGameTypes())


