from app import app,db
from app.extract_data import Extract_data
from app.models import Storm


def upload(eobj):
    for data in eobj.storm_data:
        try:
            name=data[0]
            year=data[1]
            lat=data[2]
            longi=data[3]
            cat=data[4]
            pressure=data[5]
            st=Storm(name=name,year=year,lat=lat,longi=longi,cat=cat,pressure=pressure)
            if not Storm.query.filter(Storm.name==name).filter(Storm.year==year).first():
                db.session.add(st)
        except Exception as err:
            db.session.rollback()
            print(err)
    db.session.commit()
if __name__ == "__main__":
    upload(Extract_data())