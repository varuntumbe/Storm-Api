from app import app,db
from app.models import Storm,Position
import json

#convert class-object into dictionary
def convert_to_dic(st_obj):
    st_dic=dict()
    st_dic['name']=st_obj.name
    st_dic['year']=st_obj.year
    return st_dic

def obj_to_dic(pos_obj):
    pos_dict=dict()
    pos_dict['lattitude']=pos_obj.lat
    pos_dict['longitude']=pos_obj.longi
    pos_dict['pressure']=pos_obj.pressure
    return pos_dict 

#all routes
@app.route('/year=<year>')
def year_storm(year):
    try:
        qobj=Storm.query
        li=qobj.filter(Storm.year==int(year)).all()
        li_dic=[convert_to_dic(obj) for obj in li]
        return json.dumps(li_dic)
    except Exception as err:
        return 'This Year Record has been missing'
    


@app.route('/storm_name=<sname>/year=<year>')
def storms_location(sname,year):
    try:
        qobj=Storm.query
        fil_qobj=qobj.filter(Storm.name == str(sname)).filter(Storm.year == int(year)).first()
        li=fil_qobj.pos
        li_dic= [obj_to_dic(obj) for obj in li]
        return json.dumps(li_dic)
    except Exception as err:
        return 'No info found'
