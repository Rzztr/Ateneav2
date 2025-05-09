from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#TODO hacer modelos de los querys e insert
class User(db.Model):
    id = db.Column(db.String(18), primary_key=True)
    password = db.Column(db.String(150))