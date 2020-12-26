from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()


def create_app():
    # app
    app = Flask(__name__)
    app.config[
        "SECRET_KEY"
    ] = "wCoNQ7kSY3RPeenKQwkVepqlZoEeQU162vvzz9V8GoBtjadvIiWMX2REJQgu"

    # database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tracker.db"
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    db.init_app(app)

    # folder to store images
    UPLOAD_FOLDER = "/static/img"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Error handling - passes through error code and template forms based on code
    # @app.errorhandler(Exception)
    # def handle_error(e):
    #     return render_template("error.html", error=e)

    # Blueprint registration
    from . import views
    from . import auth

    app.register_blueprint(views.bp)
    app.register_blueprint(auth.bp)

    return app
