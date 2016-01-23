from serverConnection import db

def convertToSerializable(notification):
	id, message, read, timestamp, fromP, displayname, username = notification
	return {"id": id, "message": message, "fromP": fromP, "read": read, "timestamp": str(timestamp), "displayname": displayname, "username":username }

def getPlayerNotifications(playerid):
	res = db.prepare(" SELECT n.id, n.message, n.read, n.\"timestamp\", n.\"fromP\", u.displayname, u.username FROM notifications n LEFT OUTER JOIN users u ON n.\"fromP\" = u.id WHERE n.\"toP\" = $1::integer ORDER BY n.\"timestamp\";")(playerid)

	if not res:
		return None

	return [convertToSerializable(r) for r in res]

# print(getPlayerNotifications(1))

def addNotification(message, frm, to):
	db.prepare("INSERT INTO notifications (message, \"fromP\", \"toP\") VALUES ($1::text, $2::integer, $3::integer);")(message, frm, to)

	return True

def deleteNotification(mesid):
	ret = db.prepare("DELETE FROM notifications WHERE id = $1::integer")(mesid)

	if ret[1] > 0:
		return True

	return False


# def markRead(mesid):	
# 	ret = db.prepare("UPDATE notifications SET read = t WHERE id = $1::integer")(mesid)

# 	if ret[1] > 0:
# 		return True

# 	return False

# def deleteNotifications(mesids):
# 	ret = db.prepare("DELETE FROM notifications WHERE id = any($1::integer[])")(mesids)

# 	if ret[1] > 0:
# 		return True

# 	return False


def markReadAlot(mesids):	
	ret = db.prepare("UPDATE notifications SET read = t WHERE id = any($1::integer[])")(mesids)

	if ret[1] > 0:
		return True

	return False
