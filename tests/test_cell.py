import unittest

from game.tictactoe import Cell, Piece, Color



class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell1 = Cell(1,2)
        self.cell2 = Cell(2,0)
        self.cell3 = Cell(0,2)
        self.cell2.set_piece(Piece(Color.WHITE))
        self.cell3.set_piece(Piece(Color.BLACK))
    
    def test_constructor(self):
        self.assertIsInstance(self.cell1, Cell)
        self.assertIsInstance(self.cell2, Cell)
        self.assertIsInstance(self.cell3, Cell)

    def test_set_piece(self):
        self.assertIsNone(self.cell1.get_piece())
        
        self.cell1.set_piece(Piece(Color.WHITE))

        self.assertIsNotNone(self.cell1.get_piece())
        self.assertIsInstance(self.cell1.get_piece(), Piece)

    def test_get_piece(self):
        self.assertIsNone(self.cell1.get_piece())
        self.assertIsNotNone(self.cell2.get_piece())
        self.assertIsNotNone(self.cell3.get_piece())

        self.assertIsInstance(self.cell2.get_piece(), Piece)
        self.assertIsInstance(self.cell3.get_piece(), Piece)

    def test_get_color_of_piece(self):
        self.assertIsNone(self.cell1.get_color_of_piece())
        self.assertIs(self.cell2.get_color_of_piece(), Color.WHITE)
        self.assertIs(self.cell3.get_color_of_piece(), Color.BLACK)

    def test_get_row(self):
        self.assertEqual(self.cell1.get_row(), 1)
        self.assertEqual(self.cell2.get_row(), 2)
        self.assertEqual(self.cell3.get_row(), 0)
    
    def test_get_column(self):
        self.assertEqual(self.cell1.get_column(), 2)
        self.assertEqual(self.cell2.get_column(), 0)
        self.assertEqual(self.cell3.get_column(), 2)
    
    def test_is_empty(self):
        self.assertTrue(self.cell1.is_empty())
        self.assertFalse(self.cell2.is_empty())
        self.assertFalse(self.cell3.is_empty())

    def test_has_same_coordinates(self):
        other_cell = Cell(1,2)

        self.assertTrue(self.cell1.has_same_coordinates(other_cell))
        self.assertFalse(self.cell2.has_same_coordinates(other_cell))

    def test_remove_piece(self):
        self.assertIsNotNone(self.cell2.get_piece())

        self.assertIsInstance(self.cell2.get_piece(), Piece)

        self.cell2.remove_piece()
        
        self.assertIsNone(self.cell2.get_piece())
    
    def test_to_string(self):
        self.assertEqual(str(self.cell1), "(1/2)")
        self.assertEqual(str(self.cell2), "(2/0)")
        self.assertEqual(str(self.cell3), "(0/2)")
