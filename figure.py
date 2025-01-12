#library termcolor is used for the purpose of highlighting chess pieces that can be taken.
from termcolor import colored

# class Figure defines different chess pieces, setting up their color, type and location. 
# Additionally, this class contains pieces’ display icons. 
# Figure class is the parent class of Knight and Bishop classes.
class Figure:
    def __init__(self, color: str, type: str, location: tuple) -> None:
        self.color = color
        self.type = type
        self.location = location

    # get_moves function is used to define what moves figures can do. 
    # Because knight and bishop move very differently, the exact logic is defined in their own classes.
    # For this reason get_moves function is empty in Figure class.
    def get_moves(self, board_grid: list):
        raise NotImplementedError()
    
    # get_icon fucntion contains dictonaries with display icons for each type of figure.
    # Additionally, it contains condition which returns highlighted icon when needed.
    def get_icon(self, highlight: bool) -> str:
        whites = {"knight": "♘",
                  "bishop": "♗"}
        blacks = {"knight": "♞",
                  "pawn": "♟︎",
                  "rook": "♜",
                  "bishop": "♝",
                  "queen": "♛",
                  "king": "♚"}
        
        if self.color == "white":
            return whites[self.type]
        else:
            if highlight:
                return colored(blacks[self.type], "black", "on_red")
            return blacks[self.type]