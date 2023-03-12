from app import app
from flask import render_template
from app.tel import get_messages

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Din'}
    n = 10
    flag = True
    messages = get_messages('t.me/talentservicejobs', 3)
    print(messages)
    print(type(messages))
    return render_template(
        'index.html', 
        title='TExp', 
        username=user['name'], 
        messages=messages
        )