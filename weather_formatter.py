# -*- coding: utf-8 -*-
from pprint import pprint, pformat


class Weather(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Weather, cls).__new__(cls)
        return cls.instance

    def __init__(self, weather: dict):
        self.weather = weather

    def weather_short_format(self) -> None:
        """
        This function prints weather short information.
        :return: None
        """
        try:
            print(f"The current weather:\nCondition:         {self.weather['current']['condition']['text']}")
            print(f"Temperature:       {self.weather['current']['temp_c']}")
            print(f"Wind, kph:         {self.weather['current']['wind_kph']}")
            print(f"Wind directional:  {self.weather['current']['wind_dir']}")
            print(f"Pressure, kPa:     {self.weather['current']['pressure_mb']}")
        except KeyError:
            print('Some error, please check your api key')

    def weather_long_format(self) -> None:
        """
        This function prints weather long information.
        :return:
        """
        try:
            print(f"Location:      {self.weather['location']['name']} -> {self.weather['location']['region']} -> "
                  f"{self.weather['location']['country']}")
            print(f"Localtime:         {self.weather['location']['localtime']}")
            print(f"The current weather:\n"
                  f"Condition:         {self.weather['current']['condition']['text']}")
            print(f"Temperature, C:    {self.weather['current']['temp_c']}")
            print(f"Temperature, F:    {self.weather['current']['temp_f']}")
            print(f"Wind, kph:         {self.weather['current']['wind_kph']}")
            print(f"Wind, mph:         {self.weather['current']['wind_mph']}")
            print(f"Wind degree:       {self.weather['current']['wind_degree']}")
            print(f"Wind directional:  {self.weather['current']['wind_dir']}")
            print(f"Pressure, kPa:     {self.weather['current']['pressure_mb']}")
        except KeyError:
            print('Some error, please check your api key')
