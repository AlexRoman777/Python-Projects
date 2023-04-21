''' The logic of the game. It contains the classes Player and Ship'''
import random

from visuals import VISIBLE, NAME, WATER, AI


class Ship:
    '''Class that represents a ship.'''

    def __init__(self, size):
        self.row = random.randint(0, 9)
        self.col = random.randint(0, 9)
        self.size = size
        self.orientation = random.choice(["h", "v"])
        self.indexes = self.compute_indexes()

    def compute_indexes(self):
        '''Computes the indexes of the ship.'''
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i * 10 for i in range(self.size)]


class Player:
    '''Class that represents a player.'''

    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100)]
        self.place_ships(
            sizes=[5, 4, 3, 3, 2] if classic_game else [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        )
        self.list_of_lists = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in self.list_of_lists for index in sublist]

    def place_ships(self, sizes):
        '''Places the ships on the board.'''
        for size in sizes:
            placed = False
            while not placed:
                ship = Ship(size)
                possible = True
                for i in ship.indexes:
                    if i >= 100:
                        possible = False
                        break
                    new_row = i // 10
                    new_col = i % 10
                    if new_row != ship.row and new_col != ship.col:
                        possible = False
                        break
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible = False
                            break
                if possible:
                    self.ships.append(ship)
                    placed = True

    def board_style_1(self, opponent):
        '''Prints the board of the player - Style 1.'''
        player_board = [f"{i:2d}" if i not in self.indexes else "🚢" for i in range(100)]
        computer_board = (
            [f"{i:2d}" if i not in opponent.indexes else f"{i:2d}" for i in range(100)]
            if not VISIBLE
            else [f"{i:2d}" if i not in opponent.indexes else "🚢" for i in range(100)]
        )

        def print_separator():
            print("-" * 48 + " " * 14 + "-" * 48)

        for i in range(0, 100, 10):
            print_separator()
            field_string = (
                " | ".join(player_board[i: i + 10])
                + " " * 15
                + " | ".join(computer_board[i: i + 10])
            )
            print(field_string)
        print_separator()
        print("Your board" + " " * 52 + "Computer board")
        print(
            f"Hits: {len([i for i in self.search if i == 'H'])}"
            + " " * 55
            + f"Hits: {len([i for i in opponent.search if i == 'H'])}"
        )
        print(
            f"Misses: {len([i for i in self.search if i == 'M'])}"
            + " " * 53
            + f"Misses: {len([i for i in opponent.search if i == 'M'])}"
        )
        print(
            f"Ships left: {len([ship for ship in self.ships if ship.size > 0])}"
            + " " * 49
            + f"Ships left: {len([ship for ship in opponent.ships if ship.size > 0])}"
        )

    def board_style_2(self):
        '''Prints the board of the player - Style 2.'''
        player_board = [f"{i:2d}" if i not in self.indexes else "🚢" for i in range(100)]

        def print_separator():
            print("-" * 48)

        for i in range(0, 100, 10):
            print_separator()
            field_string = " | ".join(player_board[i: i + 10])
            print(field_string)
        print_separator()
        # print(f"Ships left: {len([ship for ship in self.ships if ship.size > 0])}")

        # print(f"Opponent Ships: {opponent.indexes}")

    def board_style_3(self, oponent):
        '''Prints the board of the player - Style 3.'''
        player_board = [f"{i:2d}" if i not in self.indexes else "🚢" for i in range(100)]
        computer_board = (
            [f"{i:2d}" if i not in oponent.indexes else f"{i:2d}" for i in range(100)]
            if not VISIBLE
            else [f"{i:2d}" if i not in oponent.indexes else "🚢" for i in range(100)]
        )
        print(
            "    1  2  3  4  5  6  7  8  9  10         " * 2
        )  # Print the numbers on the top
        print("   🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽       " * 2)  # Print the arrows on the top
        for _ in range(0, 10):  # Print the letters on the left
            player_board.append([WATER] * 10)  # Add the water to the board
            computer_board.append([WATER] * 10)  # Add the water to the board 2
        letter = 0  # The letter that will be printed
        for letter in range(0, 10):  # Print the letters on the left
            print(chr(65 + letter), end=" ⏹ ")  # Print the letter
            for column in range(0, 10):  # Print the board
                print(player_board[letter][column], end=" ")
            print("⏹      ", end=" ")  # Print the divider
            print(chr(65 + letter), end=" ⏹ ")  # Print the letter
            for column in range(0, 10):  # Print the board
                print(computer_board[letter][column], end=" ")  #
            print("⏹ ")
            letter += 1
        print("   🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼       " * 2)  # Print the arrows on the bottom
        print(
            f"   {NAME}                                                              {AI}"
        )


class Game:
    '''The game class.'''

    def __init__(self, human1, human2):

        self.human1 = human1
        self.human2 = human2
        self.player = Player()
        self.computer = Player()
        self.player_turn = True
        self.computer_turn = True if not self.human1 else False
        self.over = False
        self.result = None
        self.round = 1
        self.dificulty = "hard"
        self.player_hits_left = 17 if classic_game else 20
        self.computer_hits_left = 17 if classic_game else 20
        self.classic = classic_game

    def make_move(self, i):
        '''Makes a move.'''
        player = self.player if self.player_turn else self.computer
        opponent = self.computer if self.player_turn else self.player
        hit = False

        if self.player_turn and player.search[i] != "U":
            return

        # Set Hit as "H" or Miss as "M" or Sunk as "S"
        if i in opponent.indexes:  # Hit
            player.search[i] = "H"  # Set the search to "H"
            if self.player_turn:
                self.player_hits_left -= 1
            else:
                self.computer_hits_left -= 1

            hit = True
            for ship in opponent.ships:  # For each ship
                sunk = True  # Assume the ship is sunk
                for i in ship.indexes:  # For each index in the ship
                    if (
                        player.search[i] == "U"
                    ):  # If any part of the ship is unknown, it is not sunk
                        sunk = False
                        break
                if sunk:
                    for i in ship.indexes:
                        player.search[i] = "S"  # Set the ship as sunk

        else:  # Miss
            player.search[i] = "M"  # Set the search to "M"

        # Check if the game is over
        game_over = True
        for i in opponent.indexes:
            if player.search[i] == "U":
                game_over = False
        self.over = game_over
        self.result = (
            1 if self.player_turn else 2
        )  # Set the result 1 = Player wins, 2 = Computer wins

        # Chage the active player
        if not hit:
            self.player_turn = not self.player_turn

            # Switch between human and computer
            if (self.human1 and not self.human2) or (not self.human1 and self.human2):
                self.computer_turn = not self.computer_turn

    def easy_ai(self):
        '''Easy AI, random.'''

        search = self.player.search if self.player_turn else self.computer.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        if len(unknown) > 0:
            random_index = random.choice(unknown)
            self.make_move(random_index)

    def medium_ai(self):
        '''Medium AI, avoids squares that are not possible and tries to hit around a hit.'''

        search = self.player.search if self.player_turn else self.computer.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        hits = [i for i, square in enumerate(search) if square == "H"]
        vicinity1 = []
        vicinity2 = []

        for u in unknown:
            if u + 1 in hits or u - 1 in hits or u + 10 in hits or u - 10 in hits:
                vicinity1.append(u)
            if u + 2 in hits or u - 2 in hits or u + 20 in hits or u - 20 in hits:
                vicinity2.append(u)

        # Pick "U" square with direct and indirect neighbours marked as "H"
        for u in unknown:
            if u in vicinity1 and u in vicinity2:
                self.make_move(u)
                return

        # Pick a square that has a neighbour marked as hit
        if len(vicinity1) > 0:
            self.make_move(random.choice(vicinity1))
            return
        # Random move if no other options
        self.easy_ai()

    def hard_ai(self):
        '''Hard AI, random but avoids squares that are not possible and tries to hit around a hit.'''
        search = self.player.search if self.player_turn else self.computer.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        hits = [i for i, square in enumerate(search) if square == "H"]
        vicinity1 = []
        vicinity2 = []

        for u in unknown:
            if u + 1 in hits or u - 1 in hits or u + 10 in hits or u - 10 in hits:
                vicinity1.append(u)
            if u + 2 in hits or u - 2 in hits or u + 20 in hits or u - 20 in hits:
                vicinity2.append(u)

        # Pick "U" square with direct and indirect neighbours marked as "H"
        for u in unknown:
            if u in vicinity1 and u in vicinity2:
                self.make_move(u)
                return

        # Pick a square that has a neighbour marked as hit
        if len(vicinity1) > 0:
            self.make_move(random.choice(vicinity1))
            return

        # Checkerboard pattern
        smart_board = []
        for u in unknown:
            row = u // 10
            col = u % 10
            if (row + col) % 2 == 0:
                smart_board.append(u)
        if len(smart_board) > 0:
            self.make_move(random.choice(smart_board))
            return

        # Random move if no other options
        self.easy_ai()


def classic_game(value):
    '''Sets the game mode.'''
    global classic_game
    classic_game = value


def set_difficulty(value):
    '''Sets the difficulty.'''
    global difficulty
    difficulty = value
