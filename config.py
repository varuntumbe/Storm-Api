import os

basepath=os.path.abspath(os.path.dirname(__name__))

class Config(object):
    DEBUG=True
    SECRET_KEY='This_is_secrete'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(basepath,'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False