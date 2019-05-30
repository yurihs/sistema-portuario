import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    APP_NAME = 'Sistema Portuário'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    SECRET_KEY = 'insecure-development-secret-key'

    @classmethod
    def init_app(cls, app):
        print('=> O APP ESTÁ EM MODO DE DESENVOLVIMENTO.')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

    SECRET_KEY = 'insecure-testing-secret-key'

    @classmethod
    def init_app(cls, app):
        print('=> O APP ESTÁ EM MODO DE TESTE.')


class ProductionConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')

    SECRET_KEY = os.environ.get('SECRET_KEY')

    @classmethod
    def init_app(cls, app):
        if not cls.SECRET_KEY:
            print('=> A SECRET_KEY NÃO FOI DEFINIDA!\n'
                  '   Se este não é o ambiente de produção, use o modo de desenvolvimento:\n'
                  '   FLASK_ENV=development flask run')
            exit()

config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
