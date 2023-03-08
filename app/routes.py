from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Din'}
    n = 10
    flag = True
    return render_template(
        'index.html', 
        title='TExp', 
        username=user['name'], 
        flag=flag, 
        n=n
        )