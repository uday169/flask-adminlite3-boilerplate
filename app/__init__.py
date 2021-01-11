# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .models.User import User
# local imports
from config import app_config

login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    
    app.app_context().push()
    
    login_manager.init_app(app)

    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    
    migrate = Migrate(app, db)

    from app import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)