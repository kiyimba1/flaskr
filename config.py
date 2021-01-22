import os

basedir = os.path.abspath(os.path.dirname(__file__))


class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nhfhBBB54GDs%^%$#86G&^%4fttfdd^$'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USER_NAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = ['Flasky']
    FLASKY_MAIL_SENDER = 'Flasky Admin <flask@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = os.environ.get('POSTS_PER_PAGE') or 20
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopementConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                                                                'data-dev.sqlite')


class TestingConfig(config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite://'


class ProductionConfig(config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'developement': DevelopementConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopementConfig
}
