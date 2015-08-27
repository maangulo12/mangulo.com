# -*- coding: utf-8 -*-

"""
    mangulo.com
    ~~~~~~~~~~~

    My personal website.

    :copyright: (c) 2015 by Miguel Angulo.
"""

from flask import Flask


app = Flask(__name__)


from app import settings
from app import views
