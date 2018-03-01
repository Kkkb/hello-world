import web


urls = (
	'/hello', 'Index'
#	'/1', 'index2'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")
#app.config.debug = False
class Index(object):
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
#		return render.foo()

#class index2:
#	def GET(self):
#		greeting = "Hello world again"
#`		return greeting

if __name__ == "__main__":
	app.run()