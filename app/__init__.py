import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from config import config_map

from app import assets

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    config_name = os.environ.get('FLASK_ENV', 'production')
    config = config_map[config_name]
    app.config.from_object(config)
    config.init_app(app)

    db.init_app(app)

    assets_env = Environment(app)
    assets_env.append_path(os.path.join(basedir, 'assets/scripts'))
    assets_env.append_path(os.path.join(basedir, 'assets/styles'))
    assets_env.append_path(os.path.join(basedir, 'assets/vendor'))
    assets_env.url_expire = True

    assets_env.register('app_css', assets.app_css)
    assets_env.register('app_js', assets.app_js)
    assets_env.register('vendor_css', assets.vendor_css)
    assets_env.register('vendor_js', assets.vendor_js)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
