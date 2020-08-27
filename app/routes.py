from app import app,db 


#all routes

@app.route('/')
def index():
    return 'index page'