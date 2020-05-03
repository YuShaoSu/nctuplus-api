class Config(object):
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    # app.secret_key = '7138a508b1a2ade2faea975e'
    # DATABASE_URI = 'sqlite:///:memory:'
    SESSION_TYPE = 'sqlalchemy'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DB_USERNAME:DB_PASSWD@SERVER' \
                              '/DB_NAME?charset=utf8mb4'
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True

