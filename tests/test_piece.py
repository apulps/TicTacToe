import unittest

from game.tictactoe import Color, Piece, Cell



class TestPiece(unittest.TestCase):
    def setUp(self):
        self.black_piece = Piece(Color.BLACK)
        self.white_piece = Piece(Color.WHITE)

    def test_constructor(self):
        self.assertIsInstance(self.black_piece, Piece)
        self.assertIsInstance(self.white_piece, Piece)

    def test_place_in(self):
        self.black_piece.place_in(Cell(0,0))
        self.white_piece.place_in(Cell(1,1))

        self.assertEqual(self.black_piece.get_cell().get_row(), 0)
        self.assertEqual(self.white_piece.get_cell().get_column(), 1)

    def test_get_color(self):
        self.assertEqual(self.black_piece.get_color(), Color.BLACK)
        self.assertEqual(self.white_piece.get_color(), Color.WHITE)

    def test_get_cell(self):
        self.assertEqual(self.black_piece.get_cell(), None)
        self.assertEqual(self.white_piece.get_cell(), None)

        self.black_piece.place_in(Cell(0,0))
        self.white_piece.place_in(Cell(1,1))

        self.assertIsInstance(self.white_piece.get_cell(), Cell)
        self.assertIsInstance(self.white_piece.get_cell(), Cell)

        self.assertEqual(str(self.black_piece.get_cell()), "(0/0)")
        self.assertEqual(str(self.white_piece.get_cell()), "(1/1)")

    def test_to_string(self):
        self.assertEqual(str(self.black_piece), "None/X")
        self.assertEqual(str(self.white_piece), "None/O")

        self.white_piece.place_in(Cell(0,0))
        self.black_piece.place_in(Cell(1,1))

        self.assertEqual(str(self.white_piece), "(0/0)/O")
        self.assertEqual(str(self.black_piece), "(1/1)/X")



if __name__ == "__main__":
    unittest.main()