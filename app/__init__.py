#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

fa = Flask(__name__)
fa.wsgi_app = ProxyFix(app.wsgi_app)

configurations = {
    'development': 'app.config.DefaultConfig'
}
fa.config.from_object(configurations[os.getenv('FLASK_ENV')])

import app.main
