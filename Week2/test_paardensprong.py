from unittest import TestCase
from Week2 import paardensprong


class Test_paardensprong(TestCase):
    def test_is_valid_move(self):
        self.assertTrue(paardensprong.is_valid_move((4, 4), (5, 6)),
                        "Failure validating move")
        self.assertFalse(paardensprong.is_valid_move((4, 7), (5, 6)),
                         "Failure validating move")

    def test_coordinates(self):
        self.assertTrue(paardensprong.coordinates("d4") == (4, 4),
                        "Failure translating coordinates")
        self.assertFalse(paardensprong.coordinates("d4") == (4, 5),
                         "Failure translating coordinates")
