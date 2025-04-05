from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.routes import api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(api)

    return app