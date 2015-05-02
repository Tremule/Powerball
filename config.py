class Config(object):
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'change_this_later'

class DevConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'change_this_later'