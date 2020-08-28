from app import app,db


class Storm(db.Model):
    __tablename__='storm'
    __table_args__ =(
        db.UniqueConstraint('name','year'),
    )
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    year=db.Column(db.Integer,nullable=False)
    cat=db.Column(db.String(50))
    pos=db.relationship('Position',backref='storm_info',lazy=True)

    def __repr__(self):
        return '<storm_name : {},storm_year : {}>'.format(self.name,self.year)

class Position(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    lat=db.Column(db.Float)
    longi=db.Column(db.Float)
    storm_id=db.Column(db.Integer,db.ForeignKey('storm.id'),nullable=False)
    pressure=db.Column(db.Float)

    def __repr__(self):
        return '< lat : {} and longi : {} pressure:{} >'.format(self.lat,self.longi,self.pressure)