# -*- coding: utf-8 -*-
import unittest
from gps_coordinates import get_coordinates


class TestGpsCoordinates(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_coordinates(self):
        coordinates = get_coordinates()
        self.assertEqual(type(coordinates), str)

