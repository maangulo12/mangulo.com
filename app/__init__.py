# -*- coding: utf-8 -*-

"""
    app
    ~~~~~~~~~~~

    App package
"""

from flask import Flask


app = Flask(__name__)


from app import settings
from app import views
