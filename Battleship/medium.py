'''Medium mode of the game.'''
from logic import Player
from visuals import clear, sleep, welcome_screen_short

welcome_screen_short()
player = Player()
computer = Player()
remove_player_indexes = []
remove_computer_indexes = []
check_indexes = computer.indexes if player == player else player.indexes


class Play:
    '''Class that handles the game.'''

    def __init__(self, title, player, computer):
        self.title = title
        self.player = player
        self.computer = computer
        # self.visible = False
        self.player_board = []
        self.computer_board = []

    def display(self):
        '''Displays the board of the player and the computer.'''
        clear()
        print(f"{self.title} Turn")
        # It will print ship indexes for testing, to be removed later
        print(
            f"Opponent's Ship indexes{computer.indexes if self.player == player else player.indexes}"
        )
        print()
        computer.board_style_2() if self.player == player else player.board_style_2()
        print()

    def get_shot(self):
        '''Gets the shot from the player and checks if it's a hit or a miss.'''

        shot = input("Enter your shot: ")
        # Checks in the indexes of the opponent if the shot is a hit or a miss
        check_indexes = computer.indexes if self.player == player else player.indexes
        if shot.isdigit() and int(shot) in range(100):
            if int(shot) in check_indexes:
                self.player.search[int(shot)] = "🔥"

                check_indexes.remove(int(shot))
                print("Hit!")
                sleep(1)
            else:
                self.player.search[int(shot)] = "🌊"
                print("Miss!")
                sleep(1)
        else:
            print("Invalid input, going back to menu")
            from menu import menu
            menu()

    def print_board(self):
        '''Prints the board of the player.'''
        player_board = [
            f"{i:2d}" if i not in player.indexes else "🚢" for i in range(100)
        ]

        def print_separator():
            print("-" * 48)

        for i in range(0, 100, 10):
            print_separator()
            field_string = " | ".join(player_board[i: i + 10])
            print(field_string)
        print_separator()
        print(f"Ships left: {len([ship for ship in player.ships if ship.size > 0])}")

    def update_board(self):
        '''Updates the board of the player.'''
        self.player.board = []
        for i in range(100):
            if i in self.player.indexes:
                if i in self.player.search:
                    self.player.board.append("🔥")
                else:
                    self.player.board.append("🚢")
            else:
                if i in self.player.search:
                    self.player.board.append(self.player.search[i])
                else:
                    self.player.board.append("U")

    def print_updated_board(self):
        '''Prints the updated board of the player.'''
        self.update_board()
        self.print_board()

    def change_player(self):
        '''Changes the player.'''
        if self.player == player:
            self.player = computer
        else:
            self.player = player


def anothertest(name, player):
    '''Function that tests the game.'''
    title = name
    play = Play(title, player, computer)
    play.display()
    shot = play.get_shot()


player = Player()
computer = Player()
player.board_style_2()

for i in range(len(check_indexes)):
    anothertest("Player's", player)
    anothertest("Computer's", computer)
