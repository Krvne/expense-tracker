from . import db
from flask_login import UserMixin
from datetime import datetime

now = datetime.now()


class User(db.Model, UserMixin):
    __tablename__ = "users"  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # relationships
    loans = db.relationship("Entry", backref="user")
