# -*- coding: utf-8 -*-

"""
    app.core
    ~~~~~~~~~~~

    Core module
"""

from flask import Flask


app = Flask(__name__)


from app import settings
from app import views
