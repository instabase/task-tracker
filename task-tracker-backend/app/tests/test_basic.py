import unittest

from .. import server


class BasicTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual("a", "a")

