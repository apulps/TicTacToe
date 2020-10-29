import unittest
import sys
import mock
import builtins
import random
from io import StringIO

from game.tictactoe import TicTacToe, Referee, Piece, Cell, Color, main



class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()

    def test_constructor(self):
        self.assertIsInstance(self.tictactoe, TicTacToe)

    def test_get_referee(self):
        self.assertIsInstance(self.tictactoe.get_referee(), Referee)
    
    def test_make_move(self):
        self.tictactoe.get_referee().set_players("Finn")
        self.tictactoe.get_referee().set_players("Maya")
        cell = self.tictactoe.get_referee().get_board().get_cell(0, 0)
        self.tictactoe.make_move(cell)

        result = StringIO()
        sys.stdout = result
        self.tictactoe.make_move(cell)
        self.assertEqual(result.getvalue(), "Wrong move\nCheck syntax. You cannot place a piece in a non empty cell.\n")

    def test_insert_cell(self):
        with mock.patch.object(builtins, 'input', lambda : '1A'):
            cell = self.tictactoe.insert_cell()
            self.assertEqual(cell.get_row(), 0)
            self.assertEqual(cell.get_column(), 0)
        
        with mock.patch.object(builtins, 'input', lambda : '2B'):
            cell = self.tictactoe.insert_cell()
            self.assertEqual(cell.get_row(), 1)
            self.assertEqual(cell.get_column(), 1)

        with mock.patch.object(builtins, 'input', lambda : '3C'):
            cell = self.tictactoe.insert_cell()
            self.assertEqual(cell.get_row(), 2)
            self.assertEqual(cell.get_column(), 2)

        args = ['2A', '1D']
        with mock.patch.object(builtins, 'input', lambda : args.pop()):
            result = StringIO()
            sys.stdout = result
            self.tictactoe.insert_cell()
            self.assertEqual(result.getvalue(), "Wrong input!!! Try again: \n")

    def test_show_message_wrong_move(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoe.show_message_wrong_move()

        self.assertEqual(result.getvalue(), "Wrong move\nCheck syntax. You cannot place a piece in a non empty cell.\n")

    def test_show_prompt(self):
        self.tictactoe.get_referee().set_players("Jim")

        result = StringIO()
        sys.stdout = result
        self.tictactoe.show_prompt()

        self.assertEqual(result.getvalue(), "\nTurn of Jim with pieces X of color X\n\nEnter play: \n")

    def test_show_result_match(self):
        self.tictactoe.get_referee().set_players("Laura")
        self.tictactoe.get_referee().set_players("Hugh")

        result = StringIO()
        sys.stdout = result
        self.tictactoe.show_result_match(self.tictactoe.get_referee())

        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n\t A  B  C \n\nDraw!\n")

        self.tictactoe.get_referee().get_board().place(Piece(Color.WHITE), Cell(0, 0))
        self.tictactoe.get_referee().get_board().place(Piece(Color.WHITE), Cell(1, 0))
        self.tictactoe.get_referee().get_board().place(Piece(Color.WHITE), Cell(2, 0))

        result = StringIO()
        sys.stdout = result
        self.tictactoe.show_result_match(self.tictactoe.get_referee())

        self.assertEqual(result.getvalue(), "\n1\t O  -  - \n2\t O  -  - \n3\t O  -  - \n\n\t A  B  C \n\nThe winner is Hugh/O!\n")        

    def test_are_valid_args(self):
        self.assertTrue(self.tictactoe.are_valid_args(["1A", "2B"]))
        self.assertTrue(self.tictactoe.are_valid_args([]))
        self.assertFalse(self.tictactoe.are_valid_args(["2B"]))

    def test_set_up_with_args(self):
        self.tictactoe.set_up_with_args([])
        self.assertEqual(self.tictactoe.get_referee().get_player_with_turn().get_name(), "Ellie")
        self.assertEqual(self.tictactoe.get_referee().get_player_without_turn().get_name(), "Joel")

        self.tictactoe = TicTacToe()

        self.tictactoe.set_up_with_args(["Lev", "Nate"])
        self.assertEqual(self.tictactoe.get_referee().get_player_with_turn().get_name(), "Lev")
        self.assertEqual(self.tictactoe.get_referee().get_player_without_turn().get_name(), "Nate")

    def test_set_up_referee(self):
        self.tictactoe.set_up_referee("Rick", "Jamie")

        self.assertEqual(self.tictactoe.get_referee().get_player_with_turn().get_name(), "Rick")
        self.assertEqual(self.tictactoe.get_referee().get_player_without_turn().get_name(), "Jamie")

    def test_show_help(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoe.show_help()
        self.assertEqual(result.getvalue(), "TicTacToe Game\n\nOption 1: python tictactoe.py name_player1 name_player2\n\nOption 2 (default): python tictactoe.py\n")

    def test_display_board(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoe.display_board(self.tictactoe.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n\t A  B  C \n\n")

    def test_display_rows(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoe.display_rows(self.tictactoe.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n")

    def test_display_below_letters(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoe.display_below_letters(self.tictactoe.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\t A  B  C \n\n")
