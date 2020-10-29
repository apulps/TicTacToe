import unittest
import sys
import mock
import builtins
import random
from io import StringIO

from game.tictactoe import TicTacToe, TicTacToeTextUI, Referee, Piece, Cell, Color, main
from game.tictactoegui import TicTacToeGUI



class TestTicTacToeTextUI(unittest.TestCase):
    def setUp(self):
        self.tictactoetextUI = TicTacToeTextUI()

    def test_constructor(self):
        self.assertIsInstance(self.tictactoetextUI, TicTacToe)

    def test_get_referee(self):
        self.assertIsInstance(self.tictactoetextUI.get_referee(), Referee)
    
    def test_make_move(self):
        self.tictactoetextUI.get_referee().set_players("Finn")
        self.tictactoetextUI.get_referee().set_players("Maya")
        cell = self.tictactoetextUI.get_referee().get_board().get_cell(0, 0)
        self.tictactoetextUI.make_move(cell)

        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.make_move(cell)
        self.assertEqual(result.getvalue(), "Wrong move\nCheck syntax. You cannot place a piece in a non empty cell.\n")

    def test_insert_cell(self):
        with mock.patch.object(builtins, 'input', lambda : '1A'):
            cell = self.tictactoetextUI.insert_cell()
            self.assertEqual(cell.get_row(), 0)
            self.assertEqual(cell.get_column(), 0)
        
        with mock.patch.object(builtins, 'input', lambda : '2B'):
            cell = self.tictactoetextUI.insert_cell()
            self.assertEqual(cell.get_row(), 1)
            self.assertEqual(cell.get_column(), 1)

        with mock.patch.object(builtins, 'input', lambda : '3C'):
            cell = self.tictactoetextUI.insert_cell()
            self.assertEqual(cell.get_row(), 2)
            self.assertEqual(cell.get_column(), 2)

        args = ['2A', '1D', '4C']
        with mock.patch.object(builtins, 'input', lambda : args.pop()):
            result = StringIO()
            sys.stdout = result
            self.tictactoetextUI.insert_cell()
            self.assertEqual(result.getvalue(), "Wrong input!!! Try again: \nWrong input!!! Try again: \n")

    def test_show_message_wrong_move(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.show_message_wrong_move()

        self.assertEqual(result.getvalue(), "Wrong move\nCheck syntax. You cannot place a piece in a non empty cell.\n")

    def test_show_prompt(self):
        self.tictactoetextUI.get_referee().set_players("Jim")

        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.show_prompt()

        self.assertEqual(result.getvalue(), "\nTurn of Jim with pieces X of color X\n\nEnter play: \n")

    def test_show_result_match(self):
        self.tictactoetextUI.get_referee().set_players("Laura")
        self.tictactoetextUI.get_referee().set_players("Hugh")

        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.show_result_match(self.tictactoetextUI.get_referee())

        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n\t A  B  C \n\nDraw!\n")

        self.tictactoetextUI.get_referee().get_board().place(Piece(Color.WHITE), Cell(0, 0))
        self.tictactoetextUI.get_referee().get_board().place(Piece(Color.WHITE), Cell(1, 0))
        self.tictactoetextUI.get_referee().get_board().place(Piece(Color.WHITE), Cell(2, 0))

        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.show_result_match(self.tictactoetextUI.get_referee())

        self.assertEqual(result.getvalue(), "\n1\t O  -  - \n2\t O  -  - \n3\t O  -  - \n\n\t A  B  C \n\nThe winner is Hugh/O!\n")        

    def test_are_valid_args(self):
        self.assertTrue(self.tictactoetextUI.are_valid_args(["1A", "2B"]))
        self.assertTrue(self.tictactoetextUI.are_valid_args([]))
        self.assertFalse(self.tictactoetextUI.are_valid_args(["2B"]))

    def test_set_up_with_args(self):
        self.tictactoetextUI.set_up_with_args([])
        self.assertEqual(self.tictactoetextUI.get_referee().get_player_with_turn().get_name(), "Ellie")
        self.assertEqual(self.tictactoetextUI.get_referee().get_player_without_turn().get_name(), "Joel")

        self.tictactoetextUI = TicTacToe()

        self.tictactoetextUI.set_up_with_args(["Lev", "Nate"])
        self.assertEqual(self.tictactoetextUI.get_referee().get_player_with_turn().get_name(), "Lev")
        self.assertEqual(self.tictactoetextUI.get_referee().get_player_without_turn().get_name(), "Nate")

    def test_set_up_referee(self):
        self.tictactoetextUI.set_up_referee("Rick", "Jamie")

        self.assertEqual(self.tictactoetextUI.get_referee().get_player_with_turn().get_name(), "Rick")
        self.assertEqual(self.tictactoetextUI.get_referee().get_player_without_turn().get_name(), "Jamie")

    def test_show_help(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.show_help()
        self.assertEqual(result.getvalue(), "TicTacToe Game\n\nOption 1: python tictactoe.py name_player1 name_player2\n\nOption 2 (default): python tictactoe.py\n")

    def test_display_board(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.display_board(self.tictactoetextUI.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n\t A  B  C \n\n")

    def test_display_rows(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.display_rows(self.tictactoetextUI.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\n1\t -  -  - \n2\t -  -  - \n3\t -  -  - \n\n")

    def test_display_below_letters(self):
        result = StringIO()
        sys.stdout = result
        self.tictactoetextUI.display_below_letters(self.tictactoetextUI.get_referee().get_board())
        self.assertEqual(result.getvalue(), "\t A  B  C \n\n")

    def test_main(self):
        args = ["Jon", "Elisa"]
        moves = ['1A','2A','2B','2C','3C']
        with mock.patch.object(builtins, 'input', lambda : moves.pop()):
            main(args)

        args = ["Charlie"]
        main(args)



class TestTicTacToeGUI(unittest.TestCase):
    pass
