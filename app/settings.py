# -*- coding: utf-8 -*-

"""
    app.settings
    ~~~~~~~~~~~~

    Application settings module"""

import os


# App Key
SECRET_KEY          =  os.environ.get('SECRET_KEY', 'secret_key')

# WSGI Server
SERVER_HOST         =  os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER_PORT         =  int(os.environ.get('SERVER_PORT', 4444))
DEBUG_FLAG          =  True
