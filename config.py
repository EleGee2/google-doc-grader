class Config(object):
    DEBUG = False
    TESTING = False

    OPENAI_API_KEY = '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'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'
    GOOGLE_API_KEY = 'AIzaSyAMDdIbBcSIofCobdzre_oT2yVNIVjLdnE'


class TestConfig(Config):
    TESTING = True
