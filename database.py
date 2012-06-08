import couchdb

def get_or_create(name):
	name = "xbmc-gsoc2012-" + name

	couch = couchdb.Server()
	try:
		db = couch.create(name)
	except (couchdb.PreconditionFailed):
		db = couch[name]

	return db
