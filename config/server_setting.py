import motor
from os import path

##  db  engine ##

db_client = motor.MotorClient()
##

static_path = path.join(path.pardir,"resource/statics")
## setting all components ##
settings = {
    'db' : db_client,
    'debug' : True,
    'autoreload' : True,
    'cookie_secret' : 'This is a Assiociation Softs arround Center ' ,
    'static_path' : static_path,
}

if __name__ == "__main__":
    for key  in settings:
        print "{} => {}".format(key,settings[key])
