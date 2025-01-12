from figure import Figure 
# Board class contains all chess board related functions, such as:
# displaying the board, adding figures to the board, defining logic to check for takes, etc.
class Board:
    def __init__(self) -> None:
        # To internally represent the board (8x8 grid), a list in a list is used.
        self.board_grid = [[ None for _ in range(8)] for _ in range(8)]

    # display_board function prints the board state. 
    # Additionally, it takes in a list of coordinates that can be used to highlight specific cells. 
    # (Highlighting specific cells is used to show which pieces can be taken when displaying the board)
    def display_board(self, colored_coordinates = []) -> None:
        print("   CHESS BOARD   ")

        for i, row in enumerate(self.board_grid, 0):
            print(8-i, end=" ")
            for j in range(len(row)):
                figure = self.board_grid[i][j]
                highlight = figure.location in colored_coordinates if figure else False
                figure_icon = figure.get_icon(highlight) if figure else "‧"
                print(figure_icon, end=" ")
            print()
        print("  a b c d e f g h")

    # convert_coordinate function is used to convert string input coordinates to grid coordinates, for example, a5 -> (3, 0)
    # This function is needed because user input is a string (for example, a5), 
    # but since the board is represented as a list in a list,
    # it does not understand this raw input and should only receive indices, like (3, 0)
    def convert_coordinate(self, coordinates: str) -> str:
        letter_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        first_char = coordinates[0]
        last_char = 8 - int(coordinates[-1])

        if first_char in letter_mapping:
            first_char = letter_mapping[first_char]

        return (last_char, first_char)
    
    # add_figure function is used to add figure to the grid based on the string coordinates.
    def add_figure(self, figure: Figure, coordinates: str) -> bool:

        grid_coordinates = self.convert_coordinate(coordinates)
        row = grid_coordinates[0]
        col = grid_coordinates[1]
        if self.board_grid[row][col] != None:
            return False
        self.board_grid[row][col] = figure
        figure.location = grid_coordinates
        return True

    # get_takes_for_figure function checks which enemy pieces can be taken for a specified figure.
    def get_takes_for_figure(self, figure: Figure) -> list:
        possible_moves = figure.get_moves(self.board_grid)
        enemy_figures = []
        for grid_coordinates in possible_moves:
            row = grid_coordinates[0]
            col = grid_coordinates[1]
            if self.board_grid[row][col] != None:
                found_figures = self.board_grid[row][col] 
                if found_figures.color != figure.color:
                    enemy_figures.append(found_figures)
        return enemy_figures