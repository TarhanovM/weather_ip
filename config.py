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

    SETTINGS_PATH = '/'.join(os.readlink('/usr/bin/weather').split('/')[:-1]) + '/settings.txt'

    @staticmethod
    def initialize_variables() -> None:
        """
        This is staticmethod that initializes user environment variable.
        :return: None.
        """
        file_exists = os.path.exists(Config().SETTINGS_PATH)
        if file_exists:
            with open(Config().SETTINGS_PATH, 'r', encoding='utf-8') as file:
                data_file = file.readlines()
                for line in data_file:
                    if '=' in line:
                        key, value = line.split('=')
                        setattr(Config(), key, value.strip())
        else:
            with open(Config().SETTINGS_PATH, 'w', encoding='utf-8') as file:
                file.write('API_KEY=None\nFORMAT=short\n' + 'SETTINGS_PATH=' + Config().SETTINGS_PATH + '\n')

    @staticmethod
    def set_variable(key: str, value: str) -> None:
        setattr(Config(), key, value)
        with open(Config().SETTINGS_PATH, 'r', encoding='utf-8') as file:
            settings = file.readlines()

        with open(Config().SETTINGS_PATH, 'w', encoding='utf-8') as file:
            for setting in settings:
                if key in setting:
                    setting_key, _ = setting.split('=')
                    file.write(setting_key + '=' + value + '\n')
                    continue
                file.write(setting)
