'''Importing modules from the same package'''
import getpass
import sys

from data import Database, Encryption, User

from easy import easy_play
from visuals import clear, loading_bar

data = Database()


class Menu:
    '''Menu class that displays a menu and gets the user's choice.'''

    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        '''Displays the menu.'''
        clear()
        print(self.title)
        print()
        # Use enumerate to get the index of each option
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
        # for i in range(len(self.options)):
        #     print(str(i + 1) + ". " + self.options[i])
        print("q. Quit")

    def get_choice(self):
        '''Gets the user's choice.'''
        while True:
            choice = input("Enter your choice: ")
            if choice == "q":
                print("Goodbye!")
                exit()
            elif choice.isdigit():
                choice = int(choice)
                if choice > 0 and choice <= len(self.options):
                    return choice
            print("Invalid choice, try again.")

    def get_user(self):
        '''Gets the user's name.'''
        return input("Enter your username: ")

    def get_pass(self):
        '''Gets the user's password.'''
        password = getpass.getpass("Enter your password: ")
        return password


def menu():
    '''Displays the main menu.'''
    title = "Main Menu"
    options = ["Play Game", "Save/Load Game", "Highscore", "Developer", "Exit Game"]
    main_menu = Menu(title, options)
    main_menu.display()
    choice = main_menu.get_choice()
    if choice == 1:
        play_game()
    elif choice == 2:
        save_load_game()
    elif choice == 3:
        highscore()
    elif choice == 4:
        developer()
    elif choice == 5:
        exit_game()
    else:
        print("Please enter a valid option.")
        menu()


def play_game():
    '''Displays the play game menu.'''
    title = "Play Game"
    options = ["Play", "User", "Graphical User Interface"]
    play_game_menu = Menu(title, options)
    play_game_menu.display()
    choice = play_game_menu.get_choice()
    if choice == 1:
        start_new_game()
    elif choice == 2:
        user()
    elif choice == 3:
        gui()
    else:
        print("Please enter a valid option.")
        play_game()


def gui():
    '''Displays the GUI menu.'''

    import gui_pygame

    menu()


def save_load_game():
    '''Displays the save/load game menu.'''
    title = "Save/Load Game"
    options = ["Save Game", "Load Game"]
    save_load_game_menu = Menu(title, options)
    save_load_game_menu.display()
    choice = save_load_game_menu.get_choice()
    if choice == 1:
        save_game()
    elif choice == 2:
        load_game()
    else:
        print("Please enter a valid option.")
        save_load_game()


def highscore():
    '''Displays the highscore menu.'''
    title = "Highscore"
    options = ["Your Stats", "Guest Stats", "Hall of Fame"]
    highscore_menu = Menu(title, options)
    highscore_menu.display()
    choice = highscore_menu.get_choice()
    if choice == 1:
        user_highscore()
    elif choice == 2:
        guest_highscore()
    elif choice == 3:
        hall_of_fame()
    else:
        print("Please enter a valid option.")
        highscore()


def developer():
    '''Displays the developer menu.'''
    title = "Developer"
    options = [
        "Remove User",
        "Update user stats",
        "View all users",
        "Save positions in database",
        "Remove positions from database",
        "Back to main menu"
    ]
    developer_menu = Menu(title, options)
    developer_menu.display()
    choice = developer_menu.get_choice()
    if choice == 1:
        remove_user()
    elif choice == 2:
        update_user_stats()
    elif choice == 3:
        view_all_users()
    elif choice == 4:
        save_positions()
    elif choice == 5:
        remove_positions()
    elif choice == 6:
        menu()
    else:
        print("Please enter a valid option.")
        developer()


def exit_game():
    '''Exits the game.'''
    print("Thank you for playing Battleships!")
    input("Press enter to exit...")
    sys.exit()


def user():
    '''Displays the user menu.'''
    title = "User"
    options = ["New User", "Returning User"]
    user_menu = Menu(title, options)
    user_menu.display()
    choice = user_menu.get_choice()
    if choice == 1:
        new_user()
    elif choice == 2:
        returning_user()
    else:
        print("Please enter a valid option.")
        user()


def new_user():
    '''Creates a new user.'''
    name = input("\nEnter your name: ").capitalize()
    password = input("Enter your password: ")
    check_password = input("Enter your password again: ")
    if password == check_password:
        password = Encryption(password)
        password = password.encrypt()
        user = User(name, password, "0", "0", "0", "0")
        print("User created")
        data.add_user(user)
        input("Press enter to continue...")
        menu()
    else:
        print("Passwords do not match")
        new_user()


def returning_user():
    '''Logs in a returning user.'''
    name = input("\nEnter your name: ").capitalize()
    password = input("Enter your password: ")
    password = Encryption(password)
    password = password.encrypt()
    user = data.get_user(name)
    if user:
        if user[1] == password:
            print("Welcome back " + user[0])
            input("Press enter to continue...")
            menu()
        else:
            print("Incorrect password")
            returning_user()
    else:
        print("User not found")
        returning_user()


def remove_user():
    '''Removes a user.'''
    name = input("\nEnter the user name you want to remove: ").capitalize()
    user = data.get_user(name)
    deletable = user[0]
    if user:
        confirmation = input(
            "Are you sure you want to remove " + deletable + "? (y/n): "
        )
        if confirmation == "y":
            data.remove_user(deletable)
            print("User removed")
            input("Press enter to continue...")
            menu()
        else:
            print("User not removed")
            input("Press enter to continue...")
            menu()


def update_user_stats():
    '''Updates a user's stats.'''
    name = input("\nEnter the user name you want to update: ").capitalize()
    user = data.get_user(name)
    updatable = user[0]
    if user:
        print("User found")
        print(
            "Update user games played, games won, number of shots to win and shots missed\n"
        )
        games_played = input("Games played: ")
        games_won = input("Games won: ")
        shots_to_win = input("Shots to win: ")
        shots_missed = input("Shots missed: ")
        update = User(
            updatable, user[1], games_played, games_won, shots_to_win, shots_missed
        )
        data.update_user(update)
        print("User updated")
        input("Press enter to continue...")
        menu()
    else:
        print("User not found")
        input("Press enter to continue...")
        menu()


def view_all_users():
    '''Displays all users.'''
    clear()
    users = data.get_all_users()
    print("User name\tGames played\tGames won\tShots to win\tShots missed")
    for loser in users:
        print(f"{loser[0]}\t\t{loser[2]}\t\t{loser[3]}\t\t{loser[4]}\t\t{loser[5]}")
    input("Press enter to continue...")
    menu()


def start_new_game():
    '''Displays the start new game menu.'''
    title = "Start New Game)"
    options = [
        "Easy (Terminal - Variant 1)",
        "Medium (Terminal - Variant 2)",
        "Hard (GUI)"
    ]
    start_new_game_menu = Menu(title, options)
    start_new_game_menu.display()
    choice = start_new_game_menu.get_choice()
    if choice == 1:
        easy()
    elif choice == 2:
        medium()
    elif choice == 3:
        hard()
    else:
        print("Please enter a valid option.")
        start_new_game()


def easy():
    '''Displays the easy menu.'''
    loading_bar()
    easy_play()


def medium():
    '''Displays the medium menu.'''
    loading_bar()
    import medium


def hard():
    '''Displays the hard menu.'''
    loading_bar()
    gui()


def save_game():
    '''Saves the game.'''
    print("Game saved")
    input("Press enter to continue...")
    menu()


def load_game():
    '''Loads the game.'''
    print("Game loaded")
    input("Press enter to continue...")
    menu()


def save_positions():
    '''Saves the positions.'''
    data = data.create_positions_table()
    print("Positions saved")
    input("Press enter to continue...")
    menu()


def remove_positions():
    '''Removes the positions.'''
    data.clear_positions_table()
    print("Positions removed, database is empty")
    input("Press enter to continue...")
    menu()


def user_highscore():
    '''Displays the user highscore.'''
    name = input("\nEnter your name: ").capitalize()
    user = data.get_user(name)
    clear()
    print("\nYour stats\n")
    print("User name\tGames played\tGames won\tShots to win\tShots missed")
    print("{user[0]} \t\t {user[2]} \t\t {user[3]} \t\t {user[4]} \t\t {user[5]}")
    print("You won {user[3]} games from {user[2]} games played")
    input("Press enter to continue")
    menu()


def guest_highscore():
    '''Displays the guest highscore.'''
    guest = data.get_user("Guest")
    clear()
    print("\nGuest player stats\n")
    print(f"{guest[0]} won {guest[3]} games from {guest[2]} games played")
    input("Press enter to continue")
    menu()


def hall_of_fame():
    '''Displays the hall of fame.'''
    clear()
    print("\nHall of Fame\n")
    print("User name\tGames played\tGames won\tShots to win\tShots missed")
    for user in data.top_10():
        print(f"{user[0]} \t\t {user[2]} \t\t {user[3]} \t\t {user[4]} \t\t {user[5]}")
    input("Press enter to continue")
    menu()


def going_back():
    '''Displays the going back menu.'''
    title = "Going back to main menu?"
    options = ["Yes", "No"]
    going_back_menu = Menu(title, options)
    going_back_menu.display()
    choice = going_back_menu.get_choice()
    if choice == 1:
        menu()
    elif choice == 2:
        print("You have chosen to stay here")
        input("Press enter to continue...")
    else:
        print("Please enter a valid option.")
        going_back()
