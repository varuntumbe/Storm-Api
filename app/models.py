from app import app,db


class Storm(db.Model):
    name=db.Column(db.String(50),primary_key=True)
    year=db.Column(db.Integer,primary_key=True)
    lat=db.Column(db.Float)
    longi=db.Column(db.Float)
    cat=db.Column(db.String(50))
    pressure=db.Column(db.Float)