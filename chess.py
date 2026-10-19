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
                    self.current_user = None
                    print("login successful")
                    return

            print("no user exists with this username")
    def logout(self):
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


class Piece:
    selected: bool = False

    def __init__(self):
        self.selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False


class Pawn(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class Rook(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class Knight(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class Bishop(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class Queen(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class King(Piece):
    x: int = 0
    y: int = 0
    color: str = 0
    position: int = 0
    alive: bool = 0
    score: int = 0

    def __init__(self, x, y, color, position, alive=True, score=0):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.alive = alive
        self.score = score


class Chess:
    kings: list[King]
    queens: list[Queen]
    bishops: list[Bishop]
    knights: list[Knight]
    rooks: list[Rook]
    pawns: list[Pawn]

    def __init__(self):
        self.kings = []
        self.queens = []
        self.bishops = []
        self.knights = []
        self.rooks = []
        self.pawns = []


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

    def start_game(self):
        pass

    def next_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def show_turn(self):
        pass

    def undo_number(self):
        pass

    def undo(self):
        pass

    def exit(self):
        print("program ended")
        sys.exit()

    def new_game(self, username, limit):
        pass

    def help(self):
        print("register [username] [password]")
        print("login [username] [password]")
        print("remove [username] [password]")
        print("list_users")
        print("help")
        print("exit")

    def show_moves(self):
        pass
input_file = open("input1.txt", "r")
sys.stdin = input_file

user_manager = UserManager()
game = Game()
while True:

    parts = input().strip().split()

    if parts[0]=="register":
        if len(parts) == 3:
            username = parts[1]
            password = parts[2]
            user_manager.register(username, password)
        else:
            print("invalid command")
        

    elif parts[0]=="login":
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
    elif parts[0] == "show_board":
        if len(parts) == 1:
            game.show_board()
        else:
            print("invalid command")

    elif parts[0] == "next_turn":
        if len(parts) == 1:
            game.next_turn()
        else:
            print("invalid command")

    else:
        print("invalid command")
