"""
    All of my views/routes will be placed here.
"""


from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('home.html')
