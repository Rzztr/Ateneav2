from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    username = db.Column(db.String(18))
    password = db.Column(db.String(20))
    nomuser = db.Column(db.String(30))
    apPaterno = db.Column(db.String(15))
    apMaterno = db.Column(db.String(15))
    numTelefono = db.Column(db.String(13))


class incidencias(db.Model):
    id = db.Column(db.int(10))
    latitud = db.Column(db.varchar(15))
    longitud = db.Column(db.varchar(15))
    time = db.Column(db.Time(10))
    serverd = db.Column(db.bool(False))