import tornado.web
import tornado.ioloop
from tornado.ioloop import IOLoop
from tornado import gen
import motor
import pymongo
import json

class BaseHandler(tornado.we.RequestHandler):
    def prepare(self):
        self.db = self.settings['db']

    def get_current_user(self):
        return self.get_secure_cookie('name')

    def mongo_callback(result,err):
        print 'result', repr(result), 'error', repr(error)
        IOLoop.instance().stop()

    @gen.coroutine
    def find_by(self,document_type,document):
        if not isinstance(document,dict):
            raise TypeError("this obj is not dict")
        docu = self.db.ISC[document_type]
        result = yields motor.Op(doc.find_one,document)
        if result :
            return result
        else:
            return False
    @gen.coroutine
    def insert_by(self,document_type,document,before_check=None,*additional_args):
        if not isinstance(document,dict):
            raise TypeError("this obj is not dict")

        if before_check :
            before_check(*additional_args)
        docu = self.db.ISC[document_type]
        docu.insert(document)

    @gen.coroutine
    def find_all(self,document_type,document,before_check=None,*additional_args):
        if not isinstance(document,dict):
            raise TypeError("this obj is not dict")
        if before_check:
            before_check(*additional_args)
        docu = self.db.ISC[document_type]
        return  docu.find(document)

    @gen.coroutine
    def remove_by(self,document_type,document,before_check=None,*additional_args):
        if not isinstance(document,dict):
            raise TypeError("this obj is not dict")

        if before_check:
            before_check(*additional_args)
        docu = self.db.ISC[document_type]
        docu.remove(document)

    def to_json_message(**message):
        return  json.dumps(message)

    @tornado.web.asynchronous
    def json_respond(message):
        self.write(self.to_json_message(message))
        self.finish()

    def get_message(key):
        return json.loads(self.get_argument(key))

    def params_permit(self,*args):
        def _method(f):
            params_permit = set(args)
            primary_list =list( set(self.get_arguments().keys())- params_permit)
            map(lambda x: self.get_arguments().pop(x),primary_list)

    def check_args(document,*args):
        for key in args:
            if not key in document:
                return False
        return True
class LoginHandler(BaseHandler):

    @gen.coroutine
    @tornado.web.asynchronous
    def login_user(self,id,passwd,nick=None):
        user_docu = {
            'ID':id,
            'passwd':passwd,
        }
        user_exist = self.find_by('user',user_docu)
        if user_exist:
            self.json_respond({
                'result':'ok',
            })
        else:
            self.json_respond({
                'result':'no',
                'error' :'account not right',

            })
    @tornado.web.asynchronous
    def post(self):
        login_info = self.get_message("LOGIN_INFO")
        if "ID" in login_info and "passwd"  in login_info :
            self.login_user(login_info['ID'],login_info['passwd'])
        print login_info

    @tornado.web.asynchronous
    def get(self):
        res = self.find_all('user',{})
        self.json_respond({'users':res})

class SignUpHandler(BaseHandler):

    def if_exist(self,email,ID,nick):
        user_exist_doc = {
            'email':email,
            'ID':ID,
            'nick':nick,
        }
        user_exist = self.find_by('user',user_docu)
        if user_exist:
            return True
        return False

    @tornado.web.asynchronous
    def sign_user(sign_info):
        if not isinstance(sign_info,dict):
            raise TypeError("this should be 'dict' ")

        if self.check_args(sign_info,'email','passwd','ID','nick'):
            self.insert('user',sign_info)
            self.json_respond({
                'result':'ok',
                'message':"{} ,welcom to our association".format(sign_info['nick']),
            })

    @tornado.web.asynchronous
    def post(self):
        sign_info = self.get_message('JSON_REGISTER')
        email = sign_info['email']
        user_id = sign_info['ID']
        nick_name = sign_info['nick']
        test_res =  self.if_exist(email,user_id,nick_name)
        if test_res:
            self.json_respond({
                'result':'no',
                'error' :"{} is existed".format(test_res),
            })
        else:
            self.sign_user(sign_info)

    def get(self):
        pass

class PushMessageHandler(BaseHandler):

    def post(self,request):
        pass
    def get(self):
        pass
