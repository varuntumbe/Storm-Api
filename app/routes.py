from app import app,db
from app.models import Storm,Position
import json
import webbrowser

#convert class-object into dictionary
def convert_to_dic(st_obj):
    st_dic=dict()
    st_dic['name']=st_obj.name
    st_dic['year']=st_obj.year
    return st_dic

def obj_to_dic(pos_obj):
    # pos_dict=dict()
    # pos_dict['lattitude']=pos_obj.lat
    # pos_dict['longitude']=pos_obj.longi
    # pos_dict['pressure']=pos_obj.pressure
    pos_list=list()
    pos_list.append(pos_obj.lat)
    pos_list.append(pos_obj.longi)
    pos_list.append(pos_obj.pressure)
    return pos_list

#all routes
@app.route('/year=<year>/storms_detail')
def year_storm(year):
    try:
        qobj=Storm.query
        li=qobj.filter(Storm.year==int(year)).all()
        li_dic=[convert_to_dic(obj) for obj in li]
        return json.dumps(li_dic)
    except Exception as err:
        return 'This Year Record has been missing'
    


@app.route('/storm_name=<sname>/year=<year>')
def storms_and_year_to_location(sname,year):
    try:
        qobj=Storm.query
        fil_qobj=qobj.filter(Storm.name == str(sname)).filter(Storm.year == int(year)).first()
        li=fil_qobj.pos
        li_dic= [obj_to_dic(obj) for obj in li]
        return json.dumps(li_dic)
    except Exception as err:
        return 'No info found'


@app.route('/storm_name=<sname>')
def storms_to_location(sname):
    try:
        qobj=Storm.query
        fil_qobj=qobj.filter(Storm.name == str(sname)).first()
        li=fil_qobj.pos
        li_dic= [obj_to_dic(obj) for obj in li]
        return json.dumps(li_dic)
    except Exception as err:
        return str(err)


@app.route('/year=<year>/location_detail')
def years_to_location(year):
    try:
        qobj=Storm.query
        fil_qobj=qobj.filter(Storm.year == int(year)).first()
        li=fil_qobj.pos
        li_dic= [obj_to_dic(obj) for obj in li]
        #writing data to where.js
        with open('./map_visualization/where.js','w') as fobj:
            fobj.write('myData = ')
            fobj.write(json.dumps(li_dic))
        webbrowser.open_new_tab('file:///F:/flask-api/map_visualization/where.html')
        return json.dumps(li_dic)
    except Exception as err:
        return str(err)