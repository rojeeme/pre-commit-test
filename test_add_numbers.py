import unittest
from other_repo import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
