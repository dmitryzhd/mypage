from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# @app.route('/distance')
# def distance():
#     return render_template('distance.html')

@app.route('/distance-kendall')
def distance_kendall():
    return render_template('distance-kendall.html')
