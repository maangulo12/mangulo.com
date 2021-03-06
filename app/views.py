# -*- coding: utf-8 -*-

"""
    app.views
    ~~~~~~~~~~~~

    Application views module
"""

from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')
