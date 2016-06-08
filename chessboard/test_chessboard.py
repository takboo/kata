from unittest import TestCase
from chessboard import chessboard


class TestChessboard(TestCase):
    def testchessboard(self):
        self.assertEqual(chessboard(""), "", "Failed 0 Test")
        self.assertEqual(chessboard("0 1"), "", "Failed 0x1 Test")
        self.assertEqual(chessboard("1 1"), "*", "Failed 1x1 Test")
        self.assertEqual(chessboard("1 2"), "*.", "Failed 1x2 Test")
        self.assertEqual(chessboard("1 3"), "*.*", "Failed 1x3 Test")
        self.assertEqual(chessboard("2 3"), "*.*\n.*.", "Failed 2x3 Test")
        self.assertEqual(chessboard("8 8"),
                         "*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*",
                         "Failed 5x2 Test")
