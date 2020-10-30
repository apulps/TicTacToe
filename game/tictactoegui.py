import tkinter


from game.tictactoe import TicTacToe



class TicTacToeGUI(TicTacToe): # pragma: no cover
    def __init__(self):
        super().__init__()
        self.__tk = tkinter.Tk()
        self.__frames = dict()
    
    def get_window(self):
        return self.__tk
    
    def get_frames(self):
        return self.__frames
    
    def add_frame(self, name, frame):
        self.__frames[name] = frame

    def set_up_start_game_window(self): #TODO
        start_game_container = tkinter.Frame(self.get_window(), width=500, height=500)
        start_game_container.pack()

        entry_player_1 = tkinter.Entry(start_game_container, justify=tkinter.LEFT)
        entry_player_1.place(x = 50, y = 50)
        name_1_label = tkinter.Label(text="Player 1")
        name_1_label.pack()

        entry_player_2 = tkinter.Entry(start_game_container, justify=tkinter.LEFT)
        entry_player_2.place(x = 300, y = 50)
        name_2_label = tkinter.Label(text="Player 2")
        name_2_label.pack()

        start_game_button = tkinter.Button(start_game_container, text="Start game", command=self.__set_up_match(entry_player_1, entry_player_2))
        start_game_button.place(x = 200, y = 300)

        self.add_frame("start_game", start_game_container)

    def __set_up_match(self, entry_player_1, entry_player_2):
        entry1 = entry_player_1.get()
        entry2 = entry_player_2.get()
        args = [entry1, entry2] if entry1 and entry2 else []
        
        if self.are_valid_args(args):
            self.set_up_with_args(args)
        else:
            raise ValueError

        self.get_frames()["game"].tkraise()
    
    def set_up_game_window(self):
        self.get_window().title("TicTacToe")
        game_container = tkinter.Frame(self.get_window(), width=500, height=500)
        game_container.pack()

        status_label = tkinter.Label(game_container, text=f"Turn of {self.get_referee().get_player_with_turn()}")
        
        legend_frame = tkinter.LabelFrame(game_container, text="Players", padx=5, pady=5)
        legend_frame.pack()
        legend_label = tkinter.Label(legend_frame, text=f"{str(self.get_referee().get_player_with_turn())}\n{str(self.get_referee().get_player_without_turn())}\n")
        # legend_label.pack()

        self.add_frame("game", game_container)



def main(): # pragma: no cover
    tictactoeGUI = TicTacToeGUI()

    tictactoeGUI.set_up_game_window()
    tictactoeGUI.set_up_start_game_window()

    tictactoeGUI.get_frames()["game"].tkraise()

    tictactoeGUI.get_window().mainloop()



if __name__ == "__main__":
    main() # pragma: no cover