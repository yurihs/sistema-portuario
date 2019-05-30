import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    config_name = os.environ.get('FLASK_ENV', 'production')
    config = config_map[config_name]
    app.config.from_object(config)
    config.init_app(app)

    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
