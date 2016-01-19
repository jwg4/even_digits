import unittest

from even_digits import counts

class TestEvenDigits(unittest.TestCase):
    def test_counts_for_2(self):
        """ 2, 4, 6, 8, 10, 12, 14, 16, 18 """
        expected = [1, 5, 2, 0, 2, 0, 2, 0, 2, 0]
        self.assertEqual(counts(2), expected)
