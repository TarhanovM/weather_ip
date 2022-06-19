# -*- coding: utf-8 -*-
from gps_coordinates import get_coordinates
import unittest


class TestGpsCoordinates(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_coordinates(self):
        coordinates = get_coordinates()

        self.assertEqual(type(coordinates), tuple)
        self.assertEqual(len(coordinates), 2)
