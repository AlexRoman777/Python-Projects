'''Imports all the necessary modules and runs the game.'''
from visuals import intro_screen, loading_bar, clear
from menu import menu


def main():
    '''Main function that runs the game.'''
    clear()
    intro_screen()
    loading_bar()
    menu()


if __name__ == "__main__":
    main()
