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

    def get_settings_path(self, is_testing: bool = False) -> str:
        """
        This method sets settings path depending on the usage mode
        :param is_testing: usage mode variable
        :return: path from the settings
        """
        deploy_path = '/'.join(os.readlink('/usr/bin/weather').split('/')[:-1]) + '/settings.txt'
        testing_path = '/'.join(os.readlink('/usr/bin/weather').split('/')[:-1]) + '/tests/settings.txt'
        settings_path = deploy_path if not is_testing else testing_path
        setattr(self, 'SETTINGS_PATH', settings_path)
        return settings_path

    def initialize_variables(self) -> None:
        """
        This method creates the settings file if it does not exist,
        or reads this file and sets the settings from the instance.
        :return: None.
        """
        file_exists = os.path.exists(getattr(self, 'SETTINGS_PATH'))
        if file_exists:
            with open(getattr(self, 'SETTINGS_PATH'), 'r', encoding='utf-8') as file:
                data_file = file.readlines()
                for line in data_file:
                    if '=' in line:
                        key, value = line.split('=')
                        setattr(Config(), key, value.strip())
        else:
            with open(getattr(self, 'SETTINGS_PATH'), 'w', encoding='utf-8') as file:
                file.write('API_KEY=None\nFORMAT=short\n' + 'SETTINGS_PATH=' + getattr(self, 'SETTINGS_PATH') + '\n')

    def set_variable(self, key: str, value: str) -> None:
        """
        This method reads the settings file and sets new value from key
        :param key: key setting
        :param value: value setting
        :return: None
        """
        setattr(Config(), key, value)
        with open(getattr(self, 'SETTINGS_PATH'), 'r', encoding='utf-8') as file:
            settings = file.readlines()

        with open(getattr(self, 'SETTINGS_PATH'), 'w', encoding='utf-8') as file:
            for setting in settings:
                if key in setting:
                    setting_key, _ = setting.split('=')
                    file.write(setting_key + '=' + value + '\n')
                    continue
                file.write(setting)
