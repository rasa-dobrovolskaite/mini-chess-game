from figure import Figure

# BishopFigure class represents bishop figure and is inherited from Figure class.
class BishopFigure(Figure):
    def __init__(self, color: str, location: tuple) -> None:
        self.color = color
        self.type = "bishop"
        self.location = location

    # get_moves defines possible moves for the bishop figure.
    def get_moves(self, board_grid: list) -> list:
        
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        possible_moves = []

        for direction in directions:
            # can move maximum of 8 tiles to each side, therefore, a loop repeats 8 times.
            for i in range(8):
                row = self.location[0] + direction[0] * (i+1)
                col = self.location[1] + direction[1] * (i+1)
                
                # Additionally, it checks if row and column indices are not out of board bounds.
                if row <= 7 and row >=0 and col <=7 and col >=0:
                    if board_grid[row][col] is None:
                        possible_moves.append((row, col))
                    else:
                        possible_moves.append((row, col))
                        break

        return possible_moves