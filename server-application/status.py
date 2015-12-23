def auth(key):
	import db
	stat = db.database("status")
	print stat.rows

auth(1)