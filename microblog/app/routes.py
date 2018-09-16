from app import app
from flask import request
import app.Title as Title


@app.route('/')
@app.route('/index')
def index():
    url = request.args.get("url","")
    Title.function(url)
    return (url)

