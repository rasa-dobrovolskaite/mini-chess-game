from figure import Figure

# KnightFigure class Represents knight figure and is inherited from Figure class.
class KnightFigure(Figure):
    def __init__(self, color: str, location: tuple) -> None:
        self.color = color
        self.type = "knight"
        self.location = location
    
    # get_moves defines possible moves for the knight figure.
    def get_moves(self, board_grid: list) -> list:
        
        offset_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        possible_moves = []

        for offset in offset_moves:
            row = self.location[0] + offset[0]
            col = self.location[1] + offset[1]
            
            # Additionally, it checks if row and column indexes are not out of board bounds.
            if row <= 7 and row >=0 and col <=7 and col >=0:
                possible_moves.append((row, col))
        return possible_moves