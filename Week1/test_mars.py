from unittest import TestCase
from Week1 import mars


class Test_mars(TestCase):
    def test_readable_time(self):
        self.assertTrue(mars.readable_time(86400) == "1d 0h 0m 0s",
                        "Tijd wordt incorrect geformatteerd")
