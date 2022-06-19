# -*- coding: utf-8 -*-
import unittest
from weather_api_service import get_weather
from config import Config


class TestGpsCoordinates(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        # using a real api key
        self.config.get_settings_path()
        self.config.initialize_variables()

    def tearDown(self) -> None:
        pass

    def test_get_weather(self):
        weather = get_weather((42.3121, 31.1235), self.config)
        self.assertIsInstance(weather, dict)
        self.assertIn('text', weather['current']['condition'].keys())
        self.assertIn('country', weather['location'].keys())
        self.assertIn('region', weather['location'].keys())
        self.assertIn('name', weather['location'].keys())
        self.assertIn('temp_c', weather['current'].keys())
        self.assertIn('wind_kph', weather['current'].keys())
        self.assertIn('wind_dir', weather['current'].keys())
        self.assertIn('pressure_mb', weather['current'].keys())
