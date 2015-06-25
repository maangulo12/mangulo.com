# -*- coding: utf-8 -*-

"""
    mangulo.com
    -----------

    Run this to deploy this application.

    :copyright: (c) 2015 by Miguel Angulo.
"""

from app import app
from app.config import SERVER_HOST, SERVER_PORT, DEBUG_FLAG


if __name__ == '__main__':
    app.run(host = SERVER_HOST, port = SERVER_PORT, debug = DEBUG_FLAG)
