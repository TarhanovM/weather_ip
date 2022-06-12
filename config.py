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

    API_KEY = os.environ.get('API_KEY') or None
    FORMAT = os.environ.get('FORMAT') or 'short'

    @staticmethod
    def initialize_variables() -> None:
        """
        This is staticmethod that initializes user environment variable.
        :return: None.
        """
        settings_path = f'{os.getcwd()}/settings.txt'
        file_exists = os.path.exists(settings_path)
        print(file_exists)
        if file_exists:
            with open(settings_path, 'r', encoding='utf-8') as file:
                data_file = file.readlines()
                for line in data_file:
                    key, value = line.split('=')
                    Config().key = value
        else:
            with open('settings.txt', 'w', encoding='utf-8') as file:
                variables = list(filter(lambda x: x.isupper(), dir(Config())))
                print(variables)
                for variable in variables:
                    file.write(f'{variable}={getattr(Config, variable)}\n')

    @staticmethod
    def set_variable(key, value) -> None:

        Config().key = value
        Config().initialize_variables()


