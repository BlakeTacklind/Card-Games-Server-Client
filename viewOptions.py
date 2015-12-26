from serverConnection import db


def getZoneContents(zoneNum):
    x = db.prepare("SELECT array_length(cards,1) from zones where id = $1::integer limit 1;")(zoneNum)

    if not x:
        return None

    y = db.prepare("SELECT x, cards.* from generate_series(1,$1::integer) as x join zones on true join cards on zones.cards[x] = cards.id where zones.id = $2::integer;")(x[0][0], zoneNum)

#    print(x[0][0])
#    return 0

    return dict(y)

#print('cards in zone', getZoneContents(2))

#get list of games the player is in
def playerGames(playerID):
    x = db.prepare("SELECT * FROM \"gameInstance\" WHERE $1::integer = any(players);")(playerID)

    if not x:
        return None

    return dict(x)

#print('player games', playerGames(1))

def zonesInGame(gameNum):
    x = db.prepare("SELECT id, name FROM zones WHERE game = $1::integer;")(gameNum)

    if not x:
        return None

    return dict(x)

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


