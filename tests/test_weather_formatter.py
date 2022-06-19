# -*- coding: utf-8 -*-
from unittest.mock import patch
from io import StringIO
from weather_formatter import Weather
import unittest


class TestGpsCoordinates(unittest.TestCase):
    def setUp(self) -> None:
        weather = {'location': {'name': 'Ala (1)', 'region': '', 'country': 'Eritrea', 'lat': 15.19,
                                'lon': 39.03, 'tz_id': 'Africa/Asmara', 'localtime_epoch': 1653817004,
                                'localtime': '2022-05-29 12:36'},
                   'current': {'last_updated_epoch': 1653816600, 'last_updated': '2022-05-29 12:30',
                               'temp_c': 28.2, 'temp_f': 82.8, 'is_day': 1,
                               'condition': {'text': 'Солнечно',
                                             'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png',
                                             'code': 1000}, 'wind_mph': 8.5, 'wind_kph': 13.7,
                               'wind_degree': 67, 'wind_dir': 'ENE', 'pressure_mb': 1013.0,
                               'pressure_in': 29.92, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 17,
                               'cloud': 4, 'feelslike_c': 26.2, 'feelslike_f': 79.2, 'vis_km': 10.0,
                               'vis_miles': 6.0, 'uv': 7.0, 'gust_mph': 9.8, 'gust_kph': 15.8}}
        self.Weather = Weather(weather)

    def tearDown(self) -> None:
        pass

    def test_short_weather(self):
        printed_data = f'The current weather:\n' \
                       f"Condition:         {self.Weather.weather['current']['condition']['text']}\n" \
                       f"Temperature:       {self.Weather.weather['current']['temp_c']}\n" \
                       f"Wind, kph:         {self.Weather.weather['current']['wind_kph']}\n" \
                       f"Wind directional:  {self.Weather.weather['current']['wind_dir']}\n" \
                       f"Pressure, kPa:     {self.Weather.weather['current']['pressure_mb']}\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.Weather.weather_short_format()
            self.assertEqual(fake_out.getvalue(), printed_data)

    def test_long_weather(self):
        printed_data = f"Location:          {self.Weather.weather['location']['name']} -> " \
                       f"{self.Weather.weather['location']['region']} -> " \
                       f"{self.Weather.weather['location']['country']}\n" \
                       f"Localtime:         {self.Weather.weather['location']['localtime']}\n" \
                       f"The current weather:\n" \
                       f"Condition:         {self.Weather.weather['current']['condition']['text']}\n" \
                       f"Temperature, C:    {self.Weather.weather['current']['temp_c']}\n" \
                       f"Temperature, F:    {self.Weather.weather['current']['temp_f']}\n" \
                       f"Wind, kph:         {self.Weather.weather['current']['wind_kph']}\n" \
                       f"Wind, mph:         {self.Weather.weather['current']['wind_mph']}\n" \
                       f"Wind degree:       {self.Weather.weather['current']['wind_degree']}\n" \
                       f"Wind directional:  {self.Weather.weather['current']['wind_dir']}\n" \
                       f"Pressure, kPa:     {self.Weather.weather['current']['pressure_mb']}\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.Weather.weather_long_format()
            self.assertEqual(fake_out.getvalue(), printed_data)
