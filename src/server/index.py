import tornado.ioloop
import tornado.web

application = tornado.web.Application([
	(r"/SignUp",SignUpHandler),
	(r"/PushMessage",PushMessageHandler),
	(r"/LoginIn",LoginInHandler),
	],**settings
)
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()