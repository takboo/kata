from unittest import TestCase
from tribonacci import tribonacci


class TestTribonacci(TestCase):
    def test_tribonacci(self):
        self.assertEquals(tribonacci([1 ,1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
