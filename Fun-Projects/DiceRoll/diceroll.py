from os import system, name
import random

DICE_ASCII = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
# The height of each dice face (including the border)
HEIGHT = len(DICE_ASCII[1])
# The width of each dice face (including the border)
WIDTH = len(DICE_ASCII[1][0])
DICE_SEPARATOR = " "  # The space between each dice face


def clear_terminal():
    '''Clears the terminal screen.'''
    system("cls" if name == "nt" else "clear")


def check_input(nr):
    '''Checks if the input is a number from 1 to 6.'''
    if nr in ("1", "2", "3", "4", "5", "6"):
        return int(nr)
    else:
        print(f"{nr} is not a valid number of dice.")
        print("Please enter a number from 1 to 6.")
        try_again()


def try_again():
    '''Asks the user if they want to try again after an invalid input.'''
    answer = input("Do you want to try again? [y/n] ")
    if answer == "y":
        main()
    elif answer == "n":
        print("Goodbye!")
        raise SystemExit(0)
    else:
        print("Please enter 'y' or 'n'.")
        try_again()


def roll_dice(number_of_dice):
    '''Rolls the dice and returns the results.'''
    roll_results = []
    for _ in range(number_of_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def dice_faces(dice_values):
    '''Creates the faces of the dice using the ASCII art.'''
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ASCII[value])
    return dice_faces


def final_row(faces):
    '''Creates the final row of the diagram, with the dice side by side.'''
    row = []
    for row_index in range(HEIGHT):
        row_components = []
        for face in faces:
            row_components.append(face[row_index])
        row_string = DICE_SEPARATOR.join(row_components)
        row.append(row_string)
    return row


def diagram(dice_values):
    '''Creates the diagram of the dice.'''
    faces = dice_faces(dice_values)
    row = final_row(faces)

    width = len(row[0])
    header = " You Rolled ".center(width, "~")

    # Colorize the dice faces (red)
    for i in range(len(row)):
        row[i] = row[i].replace("●", "\033[1;31m●\033[0;0m")

    finished_diagram = "\n".join([header] + row)
    return finished_diagram


def play_again():
    '''Asks the user if they want to play again.'''
    answer = input("Do you want to play again? [y/n] ")
    if answer == "y":
        main()
    elif answer == "n":
        print("Goodbye!")
        raise SystemExit(0)
    else:
        print("Please enter 'y' or 'n'.")
        play_again()


def main():  # TODO: Ask for type of game and use the standard number of dice for that game. (e.g. Yahtzee = 5 dice)
    clear_terminal()
    nr = input("How many dice do you want to roll? [1-6] ")
    number_of_dice = check_input(nr)
    roll = roll_dice(number_of_dice)
    final = diagram(roll)
    print(f"\n{final}")
    print(f"\nYou rolled: {roll}")
    play_again()


if __name__ == "__main__":
    main()
