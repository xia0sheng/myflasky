import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', '465')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', True)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'wangyouyu6')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'Wangyouyu')
    FLASKY_MAIL_SUBJECT_PREFIX = '[UNIS]'
    FLASK_MAIL_SENDER = 'Unis Admin <wangyouyu6@163.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN', 'wangyy@thunis.com')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_POSTS_PER_PAGE = 20


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}