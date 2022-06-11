# -*- coding: utf-8 -*-
import os


class Config(object):
    """
    The Config class provides a means to retrieve configuration preferences.
    This is a singleton class.
    Attributes:
    API_KEY (str): This is an environment variable which must be having from WeatherAPI.com and
                   must be setting to environment.
    FORMAT (str): This is an environment variable which user sets."""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    API_KEY = os.environ.get('API_KEY')
    FORMAT = os.environ.get('FORMAT') or 'short'

    @staticmethod
    def set_environment(key_env, value_env):
        """
        This is staticmethod that sets user environment variable.
        :param key_env: this is name variable.
        :param value_env: this is value variable.
        :return: The message is print from user console.
        """
        try:
            os.environ[key_env] = value_env
            print('Success!')
        except Exception as ex:
            print('Problem:', ex)
