import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))   # connect to database Heroku or localhost


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)   # unique names
    email = db.Column(db.String, unique=True)   #  unique mails
    secret_number = db.Column(db.Integer, unique=False)   # not unique