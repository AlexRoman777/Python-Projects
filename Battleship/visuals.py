'''This module contains all the visuals for the game.'''
import os
import sys
import time


VISIBLE = True
DIFFICULTY = None
CLASSIC = True
CLASSIC_GAME = True
BOAT_SIGN = "🚢"
HIT_SIGN = "🔥"
MISS_SIGN = "💦"
SUNK_SIGN = "❌"

SHIP = "🚢"
MISS = "🌊"
HIT = "🔥"
WATER = "🌀"
SHOT = "🚀"
TOP = "🔽"
BOTTOM = "🔼"
VERTICAL = "⏹"
BORDER = "⏹"
SUNK = "❌"

NAME = "Alex"
AI = "Computer"

BATTLESHIP = "🚢🚢🚢🚢"
DESTROYER = "🚢🚢🚢"
SUBMARINE = "🚢🚢"
PATROL = "🚤"

ASCII_TEXT = """
██████   █████  ████████ ████████ ██      ███████ ███████ ██   ██ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██      ██      ██   ██ ██ ██   ██ 
██████  ███████    ██       ██    ██      █████   ███████ ███████ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██           ██ ██   ██ ██ ██      
██████  ██   ██    ██       ██    ███████ ███████ ███████ ██   ██ ██ ██      
                                                                             
                                                                             """

WELCOME_SHORT = """
Welcome to Battleship!

The objective of the game is to sink all the enemy ships.
You will be asked to enter coordinates to hit the ships.
The coordinates are numbers from 0 to 99.

Good luck!
"""


def clear():
    '''Clears the terminal screen.'''
    os.system("cls" if os.name == "nt" else "clear")


def sleep(seconds):
    '''Sleeps for x seconds.'''
    time.sleep(seconds)


def intro_screen():
    '''Prints the intro screen.'''
    print(ASCII_TEXT)


def welcome_screen_short():
    '''Prints the short welcome screen.'''
    clear()
    loading_bar()
    clear()
    print(WELCOME_SHORT)
    input("Press enter to continue.")


def loading_bar():
    '''Prints a fake loading bar.'''
    print("\nLoading...")
    for i in range(0, 100, 5):
        time.sleep(0.1)
        sys.stdout.write("\r" + str(i + 1) + "%")
        sys.stdout.flush()
