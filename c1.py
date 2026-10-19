class Piece:
    selected: bool = False

    def __init__(self):
        self.selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False
    
    def __str__(self):
        return "  "


class Pawn(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0

    def __str__(self):
        return "P" + self.color[0]
    
    

class Rook(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
    def __str__(self):
        return "R" + self.color[0]


class Knight(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
    def __str__(self):
        return "N" + self.color[0]


class Bishop(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
    def __str__(self):
        return "B" + self.color[0]


class Queen(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self,  color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
    def __str__(self):
        return "Q" + self.color[0]


class King(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
    def __str__(self):
        return "K" + self.color[0]


class Chess:
    selected_piece = None
    turn: str = "w"
    board: list[list[Pawn | King | Queen | Knight | Rook | Bishop | None]] = []

    def __init__(self):
        self.turn = "w"
        self.initialize()

    def initialize(self):
        self.board = [
            [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
            [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white")],
            [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ]
    def print_board(self):
        for row in self.board:
            for piece in row:
                print("|", end="")
                if piece is None:
                    print("  ", end="")
                else:
                    print(str(piece), end="")
            print("|")

    def select(self, x, y):

        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - x
        column = y - 1

        piece = self.board[row][column]
        if piece is None:
            print("no piece on this spot selected")
            return

        if piece.color[0] != self.turn:
            print("you can only select one of your pieces")
            return
        
        self.selected_piece = piece
        piece.select()
        print("selected")
c1 = Chess()
c1.print_board()
c1.select(3,4)
c1.select(8,1)
print(c1.selected_piece)