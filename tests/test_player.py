import unittest

from game.tictactoe import Player, Color, Piece



class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bob", Color.WHITE)
        self.player2 = Player("Steve", Color.BLACK)
    
    def test_constructor(self):
        self.assertIsInstance(self.player1, Player)
        self.assertIsInstance(self.player2, Player)
    
    def test_get_color(self):
        self.assertIs(self.player1.get_color(), Color.WHITE)
        self.assertIs(self.player2.get_color(), Color.BLACK)

    def test_get_name(self):
        self.assertEqual(self.player1.get_name(), "Bob")
        self.assertEqual(self.player2.get_name(), "Steve")

    def test_create_piece(self):
        piece1 = self.player1.create_piece()
        piece2 = self.player2.create_piece()

        self.assertIsInstance(piece1, Piece)
        self.assertIsInstance(piece2, Piece)

        self.assertIs(self.player1.get_color(), piece1.get_color())
        self.assertIs(self.player2.get_color(), piece2.get_color())
        
    def test_to_string(self):
        self.assertEqual(str(self.player1), "Bob/O")
        self.assertEqual(str(self.player2), "Steve/X")
