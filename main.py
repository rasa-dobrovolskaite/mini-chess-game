from board import Board
from figure import Figure
from bishop import BishopFigure
from knight import KnightFigure

# game_sequence function defines in what sequence game runs and checks for wins.
def game_sequence() -> None:
    board = Board()
    white_figure = enter_white(board)
    enter_black(board)
    possible_take_figures = board.get_takes_for_figure(white_figure)
    if len(possible_take_figures) == 0:
        print("The white piece cannot take any other piece.")
        return
    takes = [figure.location for figure in possible_take_figures]
    board.display_board(takes)
    print("Possible takes are highlighted in red!")

# enter_white function asks for user input to enter white figure to the chess board.
def enter_white(board: Board) -> Figure:
    white_figure = None
    while not white_figure:
        board.display_board()
        white_input = input("Please add your white figure to the chess board. Choose either a Knight or a Bishop. Your input should be written in this exact format: e.g. knight a5: ")
        figure_type, coordinates = white_input.split(" ")
        white_figure = try_add_figure(board, "white", figure_type, coordinates)
    return white_figure

# enter_black function runs a loop 16 times (or until user inputs "done") for user to input black figures to the chess board.
def enter_black(board: Board) -> None:
    # figure_added variable is created to prevent the player from finishing (by typing "done") before a black figure is added.
    figure_added = False

    for _ in range(16):
        black_figure = None
        while not black_figure:
            board.display_board()
            black_input = input("Please add your black figures to the chess board one by one. Your input should be written in this exact format: e.g. knight a5. (IMPORTANT: Once you add all desired pieces, type done): ")
            if str(black_input).lower() == "done" and figure_added:
                return
            figure_type, coordinates = black_input.split(" ")
            black_figure = try_add_figure(board, "black", figure_type, coordinates)
        figure_added = True

# try_add_figure function matches figure from the input, validates if figure can be added successfully and if so, adds the figure to the board.
def try_add_figure(board: Board, color: str, figure_type: str, coordinates: str) -> Figure:
    figure = None
    match figure_type:
        case "knight":
            figure = KnightFigure(color, coordinates)
        case "bishop":
            figure = BishopFigure(color, coordinates)
        case "pawn":
            figure = Figure(color, "pawn", coordinates)
        case "queen":
            figure = Figure(color, "queen", coordinates)
        case "king":
            figure = Figure(color, "king", coordinates)
        case "rook":
            figure = Figure(color, "rook", coordinates)
        case _:
            print(f"Figure of type {figure_type} does not exist. Please try again.")
            return None
        
    figure_added = board.add_figure(figure, coordinates)
    if figure_added:
        print("Figure has been added successfully!")
    else:
        print(f"Figure could not be added to location {coordinates}. Please check again!")
    return figure 
        
game_sequence()
