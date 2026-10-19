import random
class Pawn:
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "P" + self.color[0]

    def move(self, x,y, board):
        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        
        old_row = 8 - self.y
        old_column = self.x - 1
        new_row = 8 - y
        new_column = x - 1
        target = board[new_row][new_column]

        print("my position:", self.x, self.y)
        print("target position:", x, y)
        print("target:", target)


        dx = x - self.x
        dy = y - self.y
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if self.color == "white":

            if x == self.x and y == self.y + 1:

                if target is not None:
                    print("cannot move to the spot")
                    return

                board[new_row][new_column] = self
                board[old_row][old_column] = None

                self.x = x
                self.y = y
                self.moved = True

                print("moved")
                return
            
            if self.moved == False and x == self.x and y == self.y + 2:

                middle_row = 8 - (self.y + 1)

                if board[middle_row][old_column] is not None:
                    print("cannot move to the spot")
                    return

                if target is not None:
                    print("cannot move to the spot")
                    return

                board[new_row][new_column] = self
                board[old_row][old_column] = None

                self.x = x
                self.y = y
                self.moved = True

                print("moved")
                return
            if y == self.y + 1:

                if x == self.x + 1 or x == self.x - 1:

                    if target is None:
                        print("cannot move to the spot")
                        return

                    if target.color == self.color:
                        print("cannot move to the spot")
                        return

                    target.alive = False

                    board[new_row][new_column] = self
                    board[old_row][old_column] = None

                    self.x = x
                    self.y = y
                    self.moved = True

                    print("rival piece destroyed")
                    return

        print("cannot move to the spot")

class Rook:
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False
    def __str__(self):
        return "R" + self.color[0]

    def move(self):
        # if # can not move thi this spot blah blah blah:
        #     pass
        # else: 
        #     if # killed enemy:
        #         pass
        #     else:
        pass
    def select(self):
        self.selected = True



class Knight:
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

    def move(self, x,y, board):
        pass



class Bishop:
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False
    def __str__(self):
        return "B" + self.color[0]

    def move(self, x,y, board):
        pass



class Queen:
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

    def move(self, x,y, board):
        pass


class King:
    color: str = 0
    alive: bool = 0
    score: int = 0
    

    def __init__(self, color, alive=True, score=0):
        self.selected=False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "K" + self.color[0]

    def move(self, x,y, board):
        pass


class Chess:
    selected_piece = None
    turn: str = "w"
    board: list[list[Pawn | King | Queen | Knight | Rook | Bishop | None]] = []

    def __init__(self):
        self.turn = "w"

    
    def print_board(self):
        for row in self.board:
            for piece in row:
                print("|", end="")
                if piece is None:
                    print("  ", end="")
                else:
                    if piece == self.selected_piece:
                        print("\033[91m" + str(piece) + "\033[0m", end="")
                    else:
                        print(str(piece), end="")
            print("|")

    def select(self, x, y):
        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - y
        column = x - 1

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
    def randomize(self):
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]

        cnt = 0
        last_white = None

        while cnt < 20:
            x = random.randint(0, 7)
            y = random.randint(0, 7)

            if self.board[x][y] is None:

                number = random.random()

                if number < 0.5:
                    color = "white"
                else:
                    color = "black"

                self.board[x][y] = Pawn(color)
                self.board[x][y].x = y + 1
                self.board[x][y].y = 8 - x

                if color == "white":
                    self.selected_piece = self.board[x][y]
                cnt += 1
                
    def move(self, x, y):
        if self.selected_piece is None:
            print("no piece selected")
            return

        self.selected_piece.move(x, y, self.board)
        # if #already moved:
        #     pass
        # elif # wrong coordinates:
        #     pass
        # elif # no selected piece:
        #     pass
        # else:
        #     self.selected_piece.move(x,y, self.board)


c1 = Chess()

c1.print_board()
c1.randomize()
c1.print_board()
print(c1.selected_piece.x, c1.selected_piece.y)        

while True:
    command = input().strip().split()

    if command[0] == "move":
        coordinates = command[1].split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])

        c1.move(x, y)
    c1.print_board()
