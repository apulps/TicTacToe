import unittest

from game.tictactoe import Board, Cell, Piece, Color



class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_constructor(self):
        self.assertIsInstance(self.board, Board)

    def test_get_rows(self):
        self.assertEqual(self.board.get_rows(), 3)
    
    def test_get_columns(self):
        self.assertEqual(self.board.get_columns(), 3)

    def test_get_cells(self):
        cells = self.board.get_cells()

        for i in range(self.board.get_rows()):
            for j in range(self.board.get_columns()):
                self.assertIsInstance(cells[i][j], Cell)
                self.assertEqual(cells[i][j].get_row(), i)
                self.assertEqual(cells[i][j].get_column(), j)

    def test_get_cell(self):
        cell = self.board.get_cell(1, 2)

        self.assertTrue(any(cell in row for row in self.board.get_cells()))

    def test_place(self):
        piece = Piece(Color.WHITE)
        cell = Cell(0,2)

        self.assertIsNone(self.board.get_cell(0,2).get_piece())

        self.board.place(piece, cell)

        self.assertIs(self.board.get_cell(0,2).get_piece(), piece)

    def test_get_cell_with_same_coordenates(self):
        cell = Cell(1,0)
        board_cell = self.board.get_cell_with_same_coordinates(cell)

        self.assertEqual(board_cell.get_row(), cell.get_row())
        self.assertEqual(board_cell.get_column(), cell.get_column())

    def test_is_on_board(self):
        cell_on_board = Cell(0,1)
        cell_not_on_board = Cell(3,3)

        self.assertTrue(self.board.is_on_board(cell_on_board))
        self.assertFalse(self.board.is_on_board(cell_not_on_board))

    def test_is_full(self):
        self.assertFalse(self.board.is_full())

        for row in self.board.get_cells():
            for cell in row:
                cell.set_piece(Piece(Color.BLACK))
        
        self.assertTrue(self.board.is_full())

    def test_to_string(self):
        self.assertEqual(str(self.board), "---\n---\n---\n")

        self.board.place(Piece(Color.WHITE), Cell(1,1))

        self.assertEqual(str(self.board), "---\n-O-\n---\n")

        self.board.place(Piece(Color.BLACK), Cell(2,2))

        self.assertEqual(str(self.board), "---\n-O-\n--X\n")
