import urllib
import urllib2
from tg import expose, TGController, AppConfig
from wsgiref.simple_server import make_server

rokuIP = "192.168.0.10"
rokuPort = "8060"
validKeys = set(["Up", "Down", "Left", "Right", "Select", "Back", "Home", "Info", "Play"])

class RootController(TGController):
	@expose()
	def index(self):
		print "index() called"
		return 'Hello World'

	@expose()
	def press(self, key):
		print "press() called"

		if key in validKeys:
			print "START"
			self.pressButton(key)
			print "FINISH"
			return "pressed"
		else:
			return "bad key"

	def pressButton(self, key):
		print "pressButton: %s" % key
		url = "http://" + rokuIP + ":" + rokuPort + "/keypress/" + key
		print url
		data = urllib.urlencode({})
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		print response.read()


config = AppConfig(minimal=True, root_controller=RootController())
application = config.make_wsgi_app()

print "Serving on port 8080..."
httpd = make_server('', 8080, application)
httpd.serve_forever()
