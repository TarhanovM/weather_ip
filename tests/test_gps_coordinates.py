# -*- coding: utf-8 -*-
import unittest
import os
import json
from gps_coordinates import get_coordinates


class TestGpsCoordinates(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_coordinates(self):
        coordinates = get_coordinates()
        self.assertEqual(type(coordinates), tuple)
        self.assertEqual(len(coordinates), 2)
        self.assertEqual(type(coordinates[0]), float)
        self.assertEqual(type(coordinates[1]), float)
        self.assertTrue(-90.0 <= coordinates[0] <= 90.0)
        self.assertTrue(-180.0 <= coordinates[0] <= 180.0)
