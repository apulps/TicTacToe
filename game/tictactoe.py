"""
TicTacToe Game
"""
from enum import Enum
import sys


class Color(Enum):
    WHITE = "O"
    BLACK = "X"

    def __str__(self):
        return self.value



class Piece:
    def __init__(self, color):
        self.__color = color
        self.__cell = None
    
    def __str__(self):
        if self.get_cell():
            if self.get_cell().is_empty():
                return f"{str(self.get_cell())}/{self.get_color()}"
        else:
            return f"None/{self.get_color()}"

    def place_in(self, cell):
        self.__cell = cell

    def get_color(self):
        return self.__color

    def get_cell(self):
        return self.__cell



class Cell:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column
        self.__piece = None
    
    def __str__(self):
        return f"({self.get_row()}/{self.get_column()})"

    def set_piece(self, piece):
        self.__piece = piece

    def get_piece(self):
        return self.__piece
    
    def get_color_of_piece(self):
        return self.get_piece().get_color() if self.get_piece() else None

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def is_empty(self):
        return False if self.get_piece() else True
    
    def has_same_coordinates(self, other):
        return True if self.get_row() == other.get_row() and self.get_column() == other.get_column() else False

    def remove_piece(self):
        self.__piece = None



class Player:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def __str__(self):
        return f"{self.get_name()}/{self.get_color()}"

    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name

    def create_piece(self):
        return Piece(self.get_color())



class Board:
    def __init__(self):
        self.__rows = 3
        self.__columns = 3
        self.__cells = []

        for i in range(self.__rows):
            aux = []
            for j in range(self.__rows):
                aux.append(Cell(i, j))
            self.__cells.append(aux)
    
    def __str__(self):
        r = ""

        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if self.get_cell(i, j).is_empty():
                    r += "-"
                else:
                    r += str(self.get_cell(i, j).get_piece().get_color())
            r += "\n"
        
        return r

    def get_rows(self):
        return self.__rows
    
    def get_columns(self):
        return self.__columns
    
    def get_cells(self):
        return self.__cells
    
    def get_cell(self, row, column):
        return self.__cells[row][column] if self.is_on_board(self.__cells[row][column]) else None
    
    def place(self, piece, cell):
        board_cell = self.get_cell_with_same_coordinates(cell)
        
        piece.place_in(board_cell)
        board_cell.set_piece(piece)
    
    def get_cell_with_same_coordinates(self, cell):
        return self.__cells[cell.get_row()][cell.get_column()]
    
    def is_on_board(self, cell):
        return True if cell.get_row() >= 0 and cell.get_row() < self.get_rows() and cell.get_column() >= 0 and cell.get_column() < self.get_columns() else False

    def is_full(self):
        for row in self.get_cells():
            for cell in row:
                if cell.is_empty():
                    return False

        return True



class Referee:
    def __init__(self, board):
        self.__board = board
        self.__player1 = None
        self.__player2 = None
        self.__turn = True

    def get_board(self):
        return self.__board

    def play(self, cell):
        piece = self.get_player_with_turn().create_piece()
        self.__board.place(piece, cell)
        self.change_turn()

    def set_players(self, name):
        if not self.__player1:
            self.__player1 = Player(name, Color.BLACK)
        elif not self.__player2:
            self.__player2 = Player(name, Color.WHITE)
    
    def get_player_with_turn(self):
        return self.__player1 if self.__turn else self.__player2
    
    def get_player_without_turn(self):
        return self.__player2 if self.__turn else self.__player1
    
    def change_turn(self):
        self.__turn = False if self.__turn else True
    
    def get_pieces_coordenates(self):
        color = self.get_player_without_turn().get_color()
        coordenates = []

        for i in range(self.get_board().get_rows()):
            for j in range(self.get_board().get_columns()):
                if self.get_board().get_cell(i, j).get_color_of_piece() == color:
                    coordenates.append((i, j))
        
        return coordenates

    def is_over(self):
        return True if self.get_winner() or self.get_board().is_full() else False
    
    def get_winner(self):
        result = None
        
        winning_combinations = [
            [(0,0),(0,1),(0,2)], [(0,0),(1,1),(2,2)], [(0,0),(1,0),(2,0)], 
            [(1,0),(1,1),(1,2)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
            [(2,0),(2,1),(2,2)], [(0,2),(1,1),(2,0)]
        ]

        for combination in winning_combinations:
            if all(coordinates in self.get_pieces_coordenates() for coordinates in combination):
                return self.get_player_without_turn()
        
        return result
    
    def is_legal_move(self, cell):
        return True if cell.is_empty() else False



class TicTacToe:
    def __init__(self):
        self.__referee = Referee(Board())
    
    def get_referee(self):
        return self.__referee

    def make_move(self, cell):
        self.__referee.play(cell) if cell.is_empty() and self.__referee.is_legal_move(cell) else self.show_message_wrong_move()
            
    def insert_cell(self):
        valid = False

        while not valid:
            s = input()
            if len(s) == 2:
                try:
                    if int(s[0]) and s[1] in ["A", "B", "C"]:
                        valid = True
                    else:
                        raise ValueError
                except ValueError:
                    print("Wrong input!!! Try again: ")

        row = int(s[0]) - 1

        if s[1] == "A":
            column = 0
        elif s[1] == "B":
            column = 1
        elif s[1] == "C":
            column = 2
        
        return self.get_referee().get_board().get_cell(row, column)
    
    def show_message_wrong_move(self):
        print("Wrong move\nCheck syntax. You cannot place a piece in a non empty cell.")
    
    def show_prompt(self):
        print(f"\nTurn of {self.__referee.get_player_with_turn().get_name()} with pieces {str(self.__referee.get_player_with_turn().get_color())} of color {self.__referee.get_player_with_turn().get_color()}")
        print("\nEnter play: ")
    
    def show_result_match(self, referee):
        self.display_board(referee.get_board())
        winner = referee.get_winner()

        if winner:
            print(f"The winner is {str(winner)}!")
        else:
            print("Draw!")
    
    def are_valid_args(self, args):
        return False if len(args) != 0 and len(args) != 2 else True
    
    def set_up_with_args(self, args):
        if len(args) == 0:
            name1 = "Player A"
            name2 = "Player B"
        else:
            name1 = args[0]
            name2 = args[1]
        
        self.set_up_referee(name1, name2)
    
    def set_up_referee(self, name1, name2):
        self.__referee.set_players(name1)
        self.__referee.set_players(name2)
    
    def show_help(self):
        print("TicTacToe Game")
        print("\nOption 1: python tictactoe.py name_player1 name_player2")
        print("\nOption 2 (default): python tictactoe.py")
    
    def display_board(self, board):
        self.display_rows(board)
        self.display_below_letters(board)

    def display_rows(self, board):
        r = "\n"

        for i in range(board.get_rows()):
            r += f"{i + 1}\t"
            for j in range(board.get_columns()):
                cell = board.get_cell(i, j)
                if cell.is_empty():
                    r += " - "
                else:
                    r += f" {str(cell.get_color_of_piece())} "
            r += "\n"
        
        print(r)
    
    def display_below_letters(self, board):
        print("\t A  B  C \n")



def main(args):
    tictactoe = TicTacToe()

    if not tictactoe.are_valid_args(args):
        tictactoe.show_help()
    else:
        tictactoe.set_up_with_args(args)
        keep_going = True
        tictactoe.display_board(tictactoe.get_referee().get_board())

        while keep_going:
            tictactoe.show_prompt()
            cell = tictactoe.insert_cell()
            tictactoe.make_move(cell)

            if tictactoe.get_referee().is_over():
                keep_going = False
            else:
                tictactoe.display_board(tictactoe.get_referee().get_board())
        
    tictactoe.show_result_match(tictactoe.get_referee())



if __name__ == "__main__":
    main(sys.argv[1:])
