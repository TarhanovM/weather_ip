import unittest
import os
from config import Config


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def tearDown(self) -> None:
        if os.getenv('test_key_env') is not None:
            os.environ.pop('test_key_env')

    def test_set_environment(self):
        Config.set_environment('test_key_env', 'test_value_env')
        self.assertEqual(os.getenv('test_key_env'), 'test_value_env')
