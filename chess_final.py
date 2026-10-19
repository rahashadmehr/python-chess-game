import re
import sys


class User:
    username: str = ""
    password: str = ""
    score: int = 0
    wins: int = 0
    draws: int = 0
    loses: int = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.score = 0
        self.wins = 0
        self.draws = 0
        self.loses = 0


class UserManager:
    users: list[User]

    def __init__(self):
        self.users = []
        self.current_user = None
        self.logged_out = False

    def register(self, username, password):

        if not re.search("^[a-zA-Z0-9_]*$", username):
            print("username format is invalid")
            return

        if not re.search("^[a-zA-Z0-9_]*$", password):
            print("password format is invalid")
            return

        for user in self.users:
            if user.username == username:
                print("a user exists with this username")
                return

        user = User(username, password)
        self.users.append(user)

        print("register successful")

    def login(self, username, password):
            if not re.search("^[a-zA-Z0-9_]*$", username):
                print("username format is invalid")
                return

            if not re.search("^[a-zA-Z0-9_]*$", password):
                print("password format is invalid")
                return

            for user in self.users:
                if user.username == username:

                    if user.password != password:
                        print("incorrect password")
                        return
                    self.current_user = user
                    self.logged_out = False
                    print("login successful")
                    return

            print("no user exists with this username")

    def logout(self):
        if self.current_user is None:
            print("invalid command")
            return

        self.current_user = None
        self.logged_out = True
        print("logout successful")

    def remove_user(self, username, password):
        if not re.search("^[a-zA-Z0-9_]*$", username):
            print("username format is invalid")
            return

        if not re.search("^[a-zA-Z0-9_]*$", password):
            print("password format is invalid")
            return

        for user in self.users:
            if user.username == username:

                if user.password != password:
                    print("incorrect password")
                    return

                self.users.remove(user)

                print("removed a successfully")
                return

        print("no user exists with this username")

    def list_users(self):
        users = []

        for user in self.users:
            users.append(user.username)

        users.sort()

        for username in users:
            print(username)

    def exit(self):
        pass

    def sort(self):
        pass
    def scoreboard(self):
        users = self.users.copy()

        users.sort(key=lambda user: user.score, reverse=True)

        for user in users:
            print(user.username, user.score, user.wins, user.draws, user.loses)


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
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "P" + self.color[0]

    def move(self, x, y, board):
        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        
        old_row = 8 - self.y
        old_column = self.x - 1

        new_row = 8 - y
        new_column = x - 1

        target = board[new_row][new_column]

        

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
        else:
            if x == self.x and y == self.y - 1:
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
            
            if self.moved == False and x == self.x and y == self.y - 2: 
                middle_row = 8 - (self.y - 1) 
                
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
            
        if y == self.y - 1: 
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


class Rook(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "R" + self.color[0]

    def move(self,x, y, board):
        # if # can not move thi this spot blah blah blah:
        #     pass
        # else:
        #     if # killed enemy:
        #         pass
        #     else:
        

        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - y
        column = x - 1

        if self.x != x and self.y != y:
            print("cannot move to the spot")
            return
        
        old_row =  8 - self.y
        old_column =self.x - 1

        if self.x == x:
            start = min(old_row, row) + 1
            end = max(old_row, row)

            for i in range(start, end):
                if board[i][old_column] is not None:
                    print("cannot move to the spot")
                    return
        
        else:
            start = min(old_column, column) + 1
            end = max(old_column, column)

            for i in range(start, end):
                if board[old_row][i] is not None:
                    print("cannot move to the spot")
                    return
        target = board[row][column]
        print(target)
        if target is not None and target.color == self.color:
            print("cannot move to the spot")
            return

        if target is not None:
            target.alive = False
            board[row][column] = self
            board[old_row][old_column] = None

            self.x = x
            self.y = y
            self.moved = True

            print("rival piece destroyed")
            return
        
        board[row][column] = self
        board[old_row][old_column] = None

        self.x = x
        self.y = y
        self.moved = True

        print("moved")

    def select(self):
        self.selected = True


class Knight(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0


    def __init__(self, color, alive=True, score=0):
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "N" + self.color[0]

    def move(self, x, y, board):
        

        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - y
        column = x - 1

        dx = x - self.x
        dy = y - self.y

        if dx * dx + dy * dy != 5:
            print("cannot move to the spot")
            return
        
        old_row =  8 - self.y
        old_column =self.x - 1

        if self.x == x:
            start = min(old_row, row) + 1
            end = max(old_row, row)

            for i in range(start, end):
                if board[i][old_column] is not None:
                    print("cannot move to the spot")
                    return
        
        else:
            start = min(old_column, column) + 1
            end = max(old_column, column)

            for i in range(start, end):
                if board[old_row][i] is not None:
                    print("cannot move to the spot")
                    return
        target = board[row][column]
        print(target)
        if target is not None and target.color == self.color:
            print("cannot move to the spot")
            return

        if target is not None:
            target.alive = False
            board[row][column] = self
            board[old_row][old_column] = None

            self.x = x
            self.y = y
            self.moved = True

            print("rival piece destroyed")
            return
        
        board[row][column] = self
        board[old_row][old_column] = None

        self.x = x
        self.y = y
        self.moved = True

        print("moved")


class Bishop(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "B" + self.color[0]

    def move(self, x, y, board):
        

        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return

        row = 8 - y
        column = x - 1

        if x - self.x != y - self.y and x - self.x != self.y - y:
            print("cannot move to the spot")
            return

        old_row = 8 - self.y
        old_column = self.x - 1

        if self.x == x:
            start = min(old_row, row) + 1
            end = max(old_row, row)

            for i in range(start, end):
                if board[i][old_column] is not None:
                    print("cannot move to the spot")
                    return

        else:
            start = min(old_column, column) + 1
            end = max(old_column, column)

            for i in range(start, end):
                if board[old_row][i] is not None:
                    print("cannot move to the spot")
                    return

        target = board[row][column]
        print(target)

        if target is not None and target.color == self.color:
            print("cannot move to the spot")
            return

        if target is not None:
            target.alive = False
            board[row][column] = self
            board[old_row][old_column] = None

            self.x = x
            self.y = y
            self.moved = True

            print("rival piece destroyed")
            return

        board[row][column] = self
        board[old_row][old_column] = None

        self.x = x
        self.y = y
        self.moved = True

        print("moved")


class Queen(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "Q" + self.color[0]

    
    def move(self, x, y, board):

        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - y
        column = x - 1

        dx = x - self.x
        dy = y - self.y

        if dx < 0:
            dx = -dx

        if dy < 0:
            dy = -dy

        if dx != 0 and dy != 0 and dx != dy:
            print("cannot move to the spot")
            return
        
        old_row =  8 - self.y
        old_column =self.x - 1

        if self.x == x:
            start = min(old_row, row) + 1
            end = max(old_row, row)

            for i in range(start, end):
                if board[i][old_column] is not None:
                    print("cannot move to the spot")
                    return
        
        else:
            start = min(old_column, column) + 1
            end = max(old_column, column)

            for i in range(start, end):
                if board[old_row][i] is not None:
                    print("cannot move to the spot")
                    return
        target = board[row][column]
        if target is not None and target.color == self.color:
            print("cannot move to the spot")
            return

        if target is not None:
            target.alive = False
            board[row][column] = self
            board[old_row][old_column] = None

            self.x = x
            self.y = y
            self.moved = True

            print("rival piece destroyed")
            return
        
        board[row][column] = self
        board[old_row][old_column] = None

        self.x = x
        self.y = y
        self.moved = True

        print("moved")


class King(Piece):
    color: str = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, color, alive=True, score=0):
        self.selected = False
        self.color = color
        self.alive = True
        self.score = 0
        self.x = 0
        self.y = 0
        self.moved = False

    def __str__(self):
        return "K" + self.color[0]

    def move(self, x,y, board):
        
        if x < 1 or x > 8 or y < 1 or y > 8:
            print("wrong coordination")
            return
        row = 8 - y
        column = x - 1

        dx = x - self.x
        dy = y - self.y

        if dx < 0:
            dx = -dx

        if dy < 0:
            dy = -dy

        if max(dx, dy) > 1:
            print("cannot move to the spot")
            return
        
        old_row =  8 - self.y
        old_column =self.x - 1

        if self.x == x:
            start = min(old_row, row) + 1
            end = max(old_row, row)

            for i in range(start, end):
                if board[i][old_column] is not None:
                    print("cannot move to the spot")
                    return
        
        else:
            start = min(old_column, column) + 1
            end = max(old_column, column)

            for i in range(start, end):
                if board[old_row][i] is not None:
                    print("cannot move to the spot")
                    return
        target = board[row][column]
        print(target)
        if target is not None and target.color == self.color:
            print("cannot move to the spot")
            return

        if target is not None:
            target.alive = False
            board[row][column] = self
            board[old_row][old_column] = None

            self.x = x
            self.y = y
            self.moved = True

            print("rival piece destroyed")
            return
        
        board[row][column] = self
        board[old_row][old_column] = None

        self.x = x
        self.y = y
        self.moved = True

        print("moved")    


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
        for y in range(1, 9):
            for x in range(1, 9):
                piece = self.board[8 - y][x - 1]

                if piece is not None:
                    piece.x = x
                    piece.y = y
                

    def print_board(self):
        for row in self.board:
            for i in range(8):
                piece = row[i]

                if piece is None:
                    print("  ", end="")
                else:
                    print(str(piece), end="")

                print("|", end="")

            print()

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

    def move(self, x, y):
        if self.selected_piece is None:
            print("no piece on this spot selected")
            return

        old_x = self.selected_piece.x
        old_y = self.selected_piece.y

        target = self.board[8 - y][x - 1]

        self.selected_piece.move(x, y, self.board)

        if self.selected_piece.x != old_x or self.selected_piece.y != old_y:
            game.moved = True

            if isinstance(target, King):
                if self.selected_piece.color == "white":
                    winner = game.white_player
                    loser = game.black_player
                    color = "white"
                else:
                    winner = game.black_player
                    loser = game.white_player
                    color = "black"

                game.king_captured = True
                game.winner = winner
                game.loser = loser
                game.winner_color = color
                self.selected_piece = None
class Game:
    limit: int = 0
    turn: str = ""
    undo_left: int = 0
    current_turn: str = ""
    winner: User
    white_player: User
    black_player: User

    def __init__(self):
        self.limit = 0
        self.white_player = None
        self.black_player = None
        self.turn = ""
        self.undo_left = 2
        self.winner = None
        self.current_turn = ""
        self.moved = False
        self.game_over = False
        self.turns_count = 0
        self.king_captured = False
        self.loser = None
        self.winner_color = ""

    def start_game(self):
        pass

    def next_turn(self):
        if self.game_over:
            return

        if self.moved == False:
            print("you must move then proceed to next turn")
            return

        print("turn completed")
        self.moved = False

        if self.king_captured:
            self.winner.score += 3
            self.winner.wins += 1
            self.loser.loses += 1
            self.game_over = True
            print("player", self.winner.username, "with color", self.winner_color, "won")
            return

        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"

        self.current_turn = self.turn
        chess.turn = self.turn
        self.turns_count += 1

        if self.limit > 0 and self.turns_count >= self.limit:
            self.white_player.score += 1
            self.black_player.score += 1
            self.white_player.draws += 1
            self.black_player.draws += 1
            self.game_over = True
            chess.selected_piece = None
            print("draw")

    def show_turn(self):

        if self.turn == "w":
            print("it is player", self.white_player.username, "turn with color white")
        else:
            print("it is player", self.black_player.username, "turn with color black")

    def undo_number(self):
        pass

    def undo(self):
        pass

    def exit(self):
        print("program ended")
        sys.exit()

    def new_game(self, username, limit):
        if not re.search("^[a-zA-Z0-9_]*$", username):
            print("username format is invalid")
            return

        if user_manager.current_user is None:
            print("you must login first")
            return

        other_user = None

        for user in user_manager.users:
            if user.username == username:
                other_user = user
                break

        if other_user is None:
            print("no user exists with this username")
            return

        self.white_player = user_manager.current_user
        self.black_player = other_user

        self.limit = limit
        self.turn = "w"
        self.current_turn = "w"
        chess.turn = "w"
        self.undo_left = 2

        self.moved = False
        self.game_over = False
        self.turns_count = 0
        self.king_captured = False
        self.winner = None
        self.loser = None
        self.winner_color = ""
        chess.selected_piece = None
        chess.initialize()

        print("new game started successfully between", self.white_player.username, "and", self.black_player.username, "with limit", self.limit)


    def help(self):
        print("register [username] [password]")
        print("login [username] [password]")
        print("remove [username] [password]")
        print("list_users")
        print("help")
        print("exit")

    def show_moves(self):
        pass
    def show_board(self):
        self.chess.print_board()
    def forfeit(self):
        if self.turn == "w":
            loser = self.white_player
            winner = self.black_player
            loser_color = "white"
            winner_color = "black"
        else:
            loser = self.black_player
            winner = self.white_player
            loser_color = "black"
            winner_color = "white"

        winner.score += 2
        winner.wins += 1

        loser.score -= 1
        loser.loses += 1

        print("you have forfeited")
        print("player", winner.username, "with color", winner_color, "won")

        self.white_player = None
        self.black_player = None
        self.turn = ""
        self.current_turn = ""
        self.limit = 0
        self.undo_left = 2
        self.game_over = True
        self.moved = False
        self.turns_count = 0
    
    def win(self, winner, loser, color):
        winner.score += 3
        winner.wins += 1
        loser.loses += 1

        print("player", winner.username, "with color", color, "won")




user_manager = UserManager()
game = Game()
chess = Chess()

input_file = open("input3.txt", "r")
output_file = open("output33.txt", "w")

sys.stdin = input_file
sys.stdout = output_file

while True:

    parts = input().strip().split()

    if len(parts) == 0:
        break

    if user_manager.logged_out and parts[0] != "login" and parts[0] != "register":
        parts = ["logged_out"]



    if parts[0] == "register":
        if len(parts) == 3:
            username = parts[1]
            password = parts[2]
            user_manager.register(username, password)
        else:
            print("invalid command")

    elif parts[0] == "login":
        if len(parts) == 3:
            username = parts[1]
            password = parts[2]
            user_manager.login(username, password)
        else:
            print("invalid command")

    elif parts[0] == "help":
        if len(parts) == 1:
            game.help()
        else:
            print("invalid command")

    elif parts[0] == "remove":
        if len(parts) == 3:
            username = parts[1]
            password = parts[2]
            user_manager.remove_user(username, password)
        else:
            print("invalid command")

    elif parts[0] == "list_users":
        if len(parts) == 1:
            user_manager.list_users()
        else:
            print("invalid command")

    elif parts[0] == "logout":
        if len(parts) == 1:
            user_manager.logout()
        else:
            print("invalid command")

    elif parts[0] == "exit":
        if len(parts) == 1:
            game.exit()
        else:
            print("invalid command")

    elif parts[0] == "select":
        if len(parts) == 2:
            coordinates = parts[1].split(",")
            x = int(coordinates[0])
            y = int(coordinates[1])
            x, y = y, x
            chess.select(x, y)
        else:
            print("invalid command")

    elif parts[0] == "move":
        if len(parts) == 2:
            coordinates = parts[1].split(",")
            x = int(coordinates[0])
            y = int(coordinates[1])
            x, y = y, x
            chess.move(x, y)
        else:
            print("invalid command")
    elif parts[0] == "new_game":
        if len(parts) == 3:
            username = parts[1]
            limit = int(parts[2])
            game.new_game(username, limit)
        else:
            print("invalid command")
    elif parts[0] == "next_turn":
        if len(parts) == 1:
            game.next_turn()
        else:
            print("invalid command")
    elif parts[0] == "show_board":
        if len(parts) == 1:
            chess.print_board()
        else:
            print("invalid command")
    elif parts[0] == "scoreboard":
        if len(parts) == 1:
            user_manager.scoreboard()
        else:
            print("invalid command")
    else:
        print("invalid command")

