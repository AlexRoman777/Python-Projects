import os
import sys
import time

visible = True
difficulty = None
classic = True
classic_game = True
boat_sign = "🚢"
hit_sign = "🔥"
miss_sign = "💦"
unknown_sign = "🌀"
sunk_sign = "❌"

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


name = "Alex"
AI = "Computer"

# Boats
BATTLESHIP = "🚢🚢🚢🚢"
DESTROYER = "🚢🚢🚢"
SUBMARINE = "🚢🚢"
PATROL = "🚤"

intro_screen = """
██████   █████  ████████ ████████ ██      ███████ ███████ ██   ██ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██      ██      ██   ██ ██ ██   ██ 
██████  ███████    ██       ██    ██      █████   ███████ ███████ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██           ██ ██   ██ ██ ██      
██████  ██   ██    ██       ██    ███████ ███████ ███████ ██   ██ ██ ██      
                                                                             
"""


def clear():
    '''Clear the screen'''
    os.system("cls" if os.name == "nt" else "clear")


def sleep(x):
    '''Sleep for x seconds'''
    time.sleep(x)


def loading_bar():
    '''A fake progress loading bar'''
    print("\nLoading...")
    for i in range(0, 100, 5):
        time.sleep(0.1)
        sys.stdout.write("\r" + str(i + 1) + "%")
        sys.stdout.flush()


def welcome_screen_short():
    clear()
    loading_bar()
    clear()
    welcome_short = """
Welcome to Battleship!
The objective of the game is to sink all the enemy ships.
You will be asked to enter coordinates to hit the ships.
The coordinates are numbers from 0 to 99.
Good luck!
"""
    print(welcome_short)