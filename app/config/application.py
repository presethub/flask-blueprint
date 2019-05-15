#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask environment config."""

import os


class DefaultConfig:
    """Default config values (Development)."""

    DEBUG = True
    SESSION_KEY = os.getenv('FLASK_SESSION_KEY')
