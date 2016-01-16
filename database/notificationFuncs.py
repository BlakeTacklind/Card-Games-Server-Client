from serverConnection import db


def getPlayerNotifications(playerid):
	res = db.prepare("SELECT id, message, \"fromP\", read, \"timestamp\" FROM notifications WHERE \"toP\" = $1::integer ORDER BY \"timestamp\";")(playerid)

	if not res:
		return None

	return res[0]

print(getPlayerNotifications(1))

def addNotification(message, frm, to):
	db.prepare("INSERT INTO notifications (message, \"fromP\", \"toP\") VALUES ($1::text, $2::integer, $3::integer);")(message, frm, to)

	return True

def deleteNotification(mesid):
	ret = db.prepare("DELETE FROM notifications WHERE id = $1::integer")(mesid)

	if ret[1] > 0:
		return True

	return False


def markRead(mesid):	
	ret = db.prepare("UPDATE notifications SET read = t WHERE id = $1::integer")(mesid)

	if ret[1] > 0:
		return True

	return False
