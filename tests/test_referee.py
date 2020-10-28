import unittest

from game.tictactoe import Referee, Board, Player, Cell, Piece, Color



class TestReferee(unittest.TestCase):
    def setUp(self):
        self.referee = Referee(Board())
    
    def test_constructor(self):
        self.assertIsInstance(self.referee, Referee)

    def test_get_board(self):
        self.assertIsInstance(self.referee.get_board(), Board)

    def test_play(self):
        self.referee.set_players("Bob")
        self.referee.set_players("Steve")
        player_with_turn = self.referee.get_player_with_turn()
        player_without_turn = self.referee.get_player_without_turn()
        cell = Cell(0,0)

        self.referee.play(cell)

        new_player_with_turn = self.referee.get_player_with_turn()
        new_player_without_turn = self.referee.get_player_without_turn()
        piece_played = self.referee.get_board().get_cell(0,0).get_piece()

        self.assertIs(player_with_turn, new_player_without_turn)
        self.assertIs(player_without_turn, new_player_with_turn)
        self.assertEqual(player_with_turn.get_color(), piece_played.get_color())
        self.assertIsInstance(piece_played, Piece)
        self.assertEqual(piece_played.get_color(), Color.BLACK)

    def test_set_players(self):
        self.assertIsNone(self.referee.get_player_with_turn())
        self.assertIsNone(self.referee.get_player_without_turn())

        self.referee.set_players("Bob")
        self.referee.set_players("Steve")

        self.assertEqual(self.referee.get_player_with_turn().get_name(), "Bob")
        self.assertEqual(self.referee.get_player_without_turn().get_name(), "Steve")
        self.assertIs(self.referee.get_player_with_turn().get_color(), Color.BLACK)
        self.assertIs(self.referee.get_player_without_turn().get_color(), Color.WHITE)

    def test_get_player_with_turn(self):
        self.assertIsNone(self.referee.get_player_with_turn())

        self.referee.set_players("Mike")

        self.assertIsInstance(self.referee.get_player_with_turn(), Player)
        self.assertEqual(self.referee.get_player_with_turn().get_name(), "Mike")
        self.assertEqual(self.referee.get_player_with_turn().get_color(), Color.BLACK)

    def test_get_player_without_turn(self):
        self.assertIsNone(self.referee.get_player_without_turn())

        self.referee.set_players("Mike")
        self.referee.set_players("Peter")

        self.assertIsInstance(self.referee.get_player_without_turn(), Player)
        self.assertEqual(self.referee.get_player_without_turn().get_name(), "Peter")
        self.assertEqual(self.referee.get_player_without_turn().get_color(), Color.WHITE)

    def test_change_turn(self):
        self.referee.set_players("Gwen")
        self.referee.set_players("Mary")
        player_with_turn = self.referee.get_player_with_turn()
        player_without_turn = self.referee.get_player_without_turn()

        self.referee.change_turn()

        new_player_with_turn = self.referee.get_player_with_turn()
        new_player_without_turn = self.referee.get_player_without_turn()

        self.assertIs(player_with_turn, new_player_without_turn)
        self.assertIs(player_without_turn, new_player_with_turn)

    def test_get_pieces_coordinates(self):
        self.referee.set_players("Norman")
        self.referee.set_players("Catherine")

        for i, row in enumerate(self.referee.get_board().get_cells()):
            for j, cell in enumerate(row):
                self.referee.get_board().place(Piece(Color.WHITE), Cell(i, j))
        
        pieces_coordenates = self.referee.get_pieces_coordinates()

        self.assertEqual(pieces_coordenates, [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])

    def test_is_over(self):
        self.referee.set_players("Anne")
        self.referee.set_players("Vin")

        self.assertFalse(self.referee.is_over())

        self.referee.get_board().place(Piece(Color.WHITE), Cell(0, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(1, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(2, 0))

        self.assertTrue(self.referee.is_over())

        self.referee.get_board().place(Piece(Color.WHITE), Cell(0, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(0, 1))
        self.referee.get_board().place(Piece(Color.BLACK), Cell(0, 2))
        self.referee.get_board().place(Piece(Color.BLACK), Cell(1, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(1, 1))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(1, 2))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(2, 0))
        self.referee.get_board().place(Piece(Color.BLACK), Cell(2, 1))

        self.assertFalse(self.referee.is_over())

        self.referee.get_board().place(Piece(Color.BLACK), Cell(2, 2))

        self.assertTrue(self.referee.is_over())

    def test_get_winner(self):
        self.referee.set_players("Dave")
        self.referee.set_players("Carol")

        self.assertIsNone(self.referee.get_winner())

        self.referee.get_board().place(Piece(Color.WHITE), Cell(0, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(1, 0))
        self.referee.get_board().place(Piece(Color.WHITE), Cell(2, 0))

        winner = self.referee.get_winner()

        self.assertIsInstance(winner, Player)
        self.assertIs(winner.get_color(), Color.WHITE)
        self.assertEqual(winner.get_name(), "Carol")

    def test_is_legal_move(self):
        cell = Cell(0, 0)

        self.assertTrue(self.referee.is_legal_move(self.referee.get_board().get_cell_with_same_coordinates(cell)))

        self.referee.get_board().place(Piece(Color.WHITE), Cell(0, 0))

        self.assertFalse(self.referee.is_legal_move(self.referee.get_board().get_cell_with_same_coordinates(cell)))
