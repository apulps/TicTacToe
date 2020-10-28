import unittest

from game.tictactoe import Color


class TestColor(unittest.TestCase):
    def test_color(self):
        self.assertEqual(str(Color.WHITE), "O")
        self.assertEqual(str(Color.BLACK), "X")
