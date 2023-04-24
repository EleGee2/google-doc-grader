class Config(object):
    DEBUG = ""
    TESTING = ""

    OPENAI_API_KEY = ''


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = ''
    GOOGLE_API_KEY = ''


class TestConfig(Config):
    TESTING = True
