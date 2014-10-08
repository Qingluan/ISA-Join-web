import tornado.ioloop
import tornado.web
import motor
from handlers import IndexHandler
from handlers import PushMessageHandler
from handlers import LoginHandler
from handlers import SignUpHandler
from env import settings

application = tornado.web.Application([
	(r"/",IndexHandler),
	(r"/SignUp",SignUpHandler),
	(r"/PushMessage",PushMessageHandler),
	(r"/Login",LoginHandler),
	],**settings
)
if __name__ == "__main__":
	application.listen(80)
	tornado.ioloop.IOLoop.instance().start()
