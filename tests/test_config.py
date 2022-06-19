# -*- coding: utf-8 -*-
from config import Config
import unittest
import os


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()
        self.config.get_settings_path(is_testing=True)
        self.config.initialize_variables()

    def test_get_settings_path(self):
        testing_path = self.config.get_settings_path(is_testing=True)
        deploy_path = self.config.get_settings_path()
        self.assertTrue(os.path.exists(testing_path))
        self.assertTrue(os.path.exists(deploy_path))

    def test_initialize_variables(self):
        self.config.initialize_variables()
        self.assertEqual(getattr(self.config, 'API_KEY'), 'None')
        self.assertEqual(getattr(self.config, 'FORMAT'), 'short')

    def test_set_environment(self):
        self.config.set_variable('test_key_env', 'test_value_env')
        self.assertEqual(getattr(self.config, 'test_key_env'), 'test_value_env')
