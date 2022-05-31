# -*- coding: utf-8 -*-
import os


class Config(object):
    API_KEY = os.environ.get('API_KEY')
    FORMAT = os.environ.get('FORMAT')

    @staticmethod
    def set_environment(key_env, value_env):
        os.environ[key_env] = value_env
