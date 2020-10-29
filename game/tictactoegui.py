import tkinter


from game.tictactoe import TicTacToe



class TicTacToeGUI(TicTacToe): # pragma: no cover
    def __init__(self):
        super().__init__()
        self.__tk = tkinter.Tk()

    def display_start_game_window(self):
        self.__tk.geometry("500x400")

        entry_player_1 = tkinter.Entry(self.__tk, justify=tkinter.LEFT)
        entry_player_1.place(x = 50, y = 50)

        entry_player_2 = tkinter.Entry(self.__tk, justify=tkinter.LEFT)
        entry_player_2.place(x = 300, y = 50)

        start_game_button = tkinter.Button(self.__tk, text="Start game", command=self.__set_up_match(entry_player_1, entry_player_2))
        start_game_button.place(x = 200, y = 300)

        self.__tk.mainloop()

    def __set_up_match(self, entry_player_1, entry_player_2):
        entry1 = entry_player_1.get()
        entry2 = entry_player_2.get()
        args = [entry1, entry2] if entry1 and entry2 else []
        
        if self.are_valid_args(args):
            self.set_up_with_args(args)
        else:
            raise ValueError
    
    def display_game_window(self):
        pass



def main():
    tictactoeGUI = TicTacToeGUI()

    tictactoeGUI.display_start_game_window()



if __name__ == "__main__":
    main() # pragma: no cover