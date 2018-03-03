import web
from gothonweb import map
from random import randint

# web.config.debug = False
urls = (
#	'/hello', 'Index',
#	'/count', 'count',
#	'/reset', 'reset',
	'/game', 'GameEngine',
	'/', 'Index',
#	'/1', 'index2'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")
#app.config.debug = False
#store = web.session.DiskStore('sessions')
#session = web.session.Session(app, store, initializer={'count': 0})
'''
class count:
	def GET(self):
		session.count += 1
		return str(session.count)

class reset:
	def GET(self):
		session.kill()
		return ""
'''
class Index(object):
	def GET(self):
		# this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")

#	def POST(self):
#		form = web.input(name="Nobody", greet="Hello")
#		greeting = "%s, %s" % (form.greet, form.name)
#		return render.index(greeting = greeting)
#		return render.foo()

#class index2:
#	def GET(self):
#		greeting = "Hello world again"
#`		return greeting
class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is there here? do you need it?
			bye = map.generic_death.go(str(randint(1, 4)))
			return render.you_died(bye)

	def POST(self):
		form = web.input(action=None)

		# there is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")

if __name__ == "__main__":
	app.run()