from app import app
from flask import render_template
from app.tel import get_messages, client

@app.route('/')
@app.route('/index')
async def index():
    user = {'name': 'Din'}
    async with client:
        messages = await get_messages('t.me/zarubezhom_jobs', days=14)
    return render_template(
        'index.html', 
        title='TExp', 
        username=user['name'], 
        messages=messages
    )