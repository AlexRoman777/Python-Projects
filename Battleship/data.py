'''Imports all the necessary modules and runs the game.'''
import base64
import random
import sqlite3

from logic import Player

TEXT_PATH = "Battleship/data/ships.txt"
DB_PATH = "Battleship/data/users.db"


class Data:
    '''Class that handles the text file.'''

    def __init__(self):
        self.read_one = self.read_one_position_from_file()
        self.read_random = self.read_positions_from_file()

    def create_txt_file(self):
        '''Creates a text file with 1000 random positions.'''
        for i in range(1000):
            player = Player()
            with open(TEXT_PATH, "a") as file:
                file.write(str(player.indexes) + "\n")

    def read_positions_from_file(self):
        '''Reads all the positions from the text file.'''
        with open(TEXT_PATH, "r") as file:
            positions = eval(file.readlines()[random.randint(0, 999)].strip())
        return positions

    def read_one_position_from_file(self):
        '''Reads one position from the text file.'''
        with open(TEXT_PATH, "r") as file:
            positions = eval(file.readlines()[500].strip())
        return positions

    def read_custom_position_from_file(self, custom_position):
        with open(TEXT_PATH, "r") as file:
            positions = eval(file.readlines()[custom_position].strip())
        return positions


class Database:
    '''Class that handles the database.'''

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS users (
            name text,
            password text,
            games_played integer,
            games_won integer,
            nr_of_shots_to_win integer,
            shots_missed integer
        )"""
        )
        self.conn.commit()
        self.conn.close()

    def add_user(self, user):
        '''Adds a user to the database'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
            (
                user.name,
                user.password,
                user.games_played,
                user.games_won,
                user.nr_of_shots_to_win,
                user.shots_missed,
            ),
        )
        self.conn.commit()
        self.conn.close()

    def get_user(self, name):
        '''Gets a user from the database'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM users WHERE name = ?", (name,))
        user = self.c.fetchone()
        self.conn.close()
        return user

    def update_user(self, user):
        '''Updates a user after each game'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute(
            "UPDATE users SET games_played = ?, games_won = ?, nr_of_shots_to_win = ?, shots_missed = ? WHERE name = ?",
            (
                user.games_played,
                user.games_won,
                user.nr_of_shots_to_win,
                user.shots_missed,
                user.name,
            ),
        )
        self.conn.commit()
        self.conn.close()

    def top_10(self):
        '''Creates a top 10 list of users with the best win ratio and sorted by nr of shots to win'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute(
            "SELECT * FROM users ORDER BY games_won / games_played DESC, nr_of_shots_to_win ASC LIMIT 10"
        )
        top_10 = self.c.fetchall()
        self.conn.close()
        return top_10

    def remove_user(self, name):
        '''Removes a user from the database'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM users WHERE name = ?", (name,))
        self.conn.commit()
        self.conn.close()

    def get_all_users(self):
        '''Gets all the users from the database'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM users")
        users = self.c.fetchall()
        self.conn.close()
        return users

    def create_positions_table(self):
        '''Creates a table with 1000 random positions from the text file'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS positions (
            positions text
        )"""
        )
        self.conn.commit()
        self.conn.close()
        with open(TEXT_PATH, "r") as file:
            positions = file.readlines()
            self.conn = sqlite3.connect(DB_PATH)
            self.c = self.conn.cursor()
            for position in positions:
                self.c.execute("INSERT INTO positions VALUES (?)", (position.strip(),))
            self.conn.commit()
            self.conn.close()

    def get_random_position(self):
        '''Gets a random position from the table positions from the user.db file'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM positions ORDER BY RANDOM() LIMIT 1")
        position = self.c.fetchone()
        self.conn.close()
        return position

    def get_one_position(self, position):
        '''Gets one position from the table positions from the user.db file'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM positions WHERE positions = ?", (position,))
        position = self.c.fetchone()
        self.conn.close()
        return position

    def clear_positions_table(self):
        '''Clears the content of the table positions from the user.db file'''
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM positions")
        self.conn.commit()
        self.conn.close()


class Encryption:
    '''Encrypts and decrypts the password'''

    def __init__(self, password):
        self.password = password

    def encrypt(self):
        '''Encrypts the password'''
        password = self.password
        password = password.encode()
        password = base64.b64encode(password)
        password = password.decode()
        return password

    def decrypt(self):
        '''Decrypts the password'''
        password = self.password
        password = password.encode()
        password = base64.b64decode(password)
        password = password.decode()
        return password


class User:
    '''Creates a user with the following attributes:'''

    def __init__(
        self, name, password, games_played, games_won, nr_of_shots_to_win, shots_missed
    ):  # Initialize the user
        self.name = name
        self.password = password
        self.games_played = games_played
        self.games_won = games_won
        self.nr_of_shots_to_win = nr_of_shots_to_win
        self.shots_missed = shots_missed

    def get_name(self):
        '''Returns the name of the user'''
        return self.name

    def get_password(self):
        '''Returns the password of the user'''
        return self.password

    def get_games_played(self):
        '''Returns the number of games played by the user'''
        return self.games_played

    def get_games_won(self):
        '''Returns the number of games won by the user'''
        return self.games_won

    def get_nr_of_shots_to_win(self):
        '''Returns the number of shots to win by the user'''
        return self.nr_of_shots_to_win

    def get_shots_missed(self):
        '''Returns the number of shots missed by the user'''
        return self.shots_missed
