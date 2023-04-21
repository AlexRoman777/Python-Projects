import random

from visuals import *


# This function runs the game in terminal
def easy_play():
    clear()
    intro_screen()
    welcome_screen()
    clear()
    board1 = []
    board2 = []
    print_boards_side_by_side(board1, board2)
    print(
        "The bords updates automatically with 10 ships of this sizes (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)."
    )
    print(
        "Input the coordinates of your shot in the format A1, B2, C3, etc. \nor press q to return to Main Menu."
    )
    input("Press Enter to continue...")
    clear()
    board_update(board1)
    board_update(board2)
    print_boards_side_by_side(board1, board2)
    while True:
        clear()
        print_boards_side_by_side(board1, board2)
        row, column = get_shot()
        if check_shot(board2, row, column):
            if check_game_over(board2):
                print(f"You win!")
                play_again()
                break
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        if check_shot(board1, row, column):
            if check_game_over(board1):
                print(f"{AI} wins!")
                play_again()
                break
    # Go back to the main menu in menu.py
    from menu import menu

    menu()


# Draw the boards side by side with some emojis.
def print_boards_side_by_side(board1, board2):
    print(
        "    1  2  3  4  5  6  7  8  9  10         " * 2
    )  # Print the numbers on the top
    print(f"   🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽       " * 2)  # Print the arrows on the top
    for row in range(0, 10):  # Print the letters on the left
        board1.append([WATER] * 10)  # Add the water to the board
        board2.append([WATER] * 10)  # Add the water to the board 2
    letter = 0  # The letter that will be printed
    for letter in range(0, 10):  # Print the letters on the left
        print(chr(65 + letter), end=" ⏹ ")  # Print the letter
        for column in range(0, 10):  # Print the board
            print(board1[letter][column], end=" ")
        print("⏹      ", end=" ")  # Print the divider
        print(chr(65 + letter), end=" ⏹ ")  # Print the letter
        for column in range(0, 10):  # Print the board
            print(board2[letter][column], end=" ")  #
        print("⏹ ")
        letter += 1
    print("   🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼       " * 2)  # Print the arrows on the bottom
    print(
        f"   {name}                                                              {AI}"
    )


# Place the ship on the board.
def place_battleship(board):  # 1 battleship
    ship_placed = False
    while not ship_placed:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        direction = random.randint(0, 1)
        if direction == 0:  # Horizontal
            if column + 4 > 10:  # If the ship is out of bounds
                continue
            for i in range(column, column + 4):  # Check if the ship is overlapping
                if board[row][i] != WATER:  # Add the ship to the board
                    break
            else:  #
                for i in range(column, column + 4):  # Check if the ship is overlapping
                    board[row][i] = BATTLESHIP[i - column]  # Add the ship to the board
                ship_placed = True  # If the ship is not overlapping, place the ship
        else:
            # Vertical
            if row + 4 > 10:  # If the ship is out of bounds
                continue
            for i in range(row, row + 4):  # Check if the ship is overlapping
                if board[i][column] != WATER:  # Add the ship to the board
                    break
            else:
                for i in range(row, row + 4):  # Check if the ship is overlapping
                    board[i][column] = BATTLESHIP[i - row]  # Add the ship to the board
                ship_placed = True
    return board


# Place the ship on the board.
def place_destroyer(board):
    for i in range(2):  # 2 destroyers
        ship_placed = False
        while not ship_placed:
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            direction = random.randint(0, 1)
            if direction == 0:
                # Horizontal
                if column + 3 > 10:
                    continue
                for i in range(column, column + 3):
                    if board[row][i] != WATER:
                        break
                else:
                    for i in range(column, column + 3):
                        board[row][i] = DESTROYER[i - column]
                    ship_placed = True
            else:
                # Vertical
                if row + 3 > 10:
                    continue
                for i in range(row, row + 3):
                    if board[i][column] != WATER:
                        break
                else:
                    for i in range(row, row + 3):
                        board[i][column] = DESTROYER[i - row]
                    ship_placed = True
    return board


# Place the ship on the board.
def place_submarine(board):
    for i in range(3):  # 3 submarines
        ship_placed = False
        while not ship_placed:
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            direction = random.randint(0, 1)
            if direction == 0:
                # Horizontal
                if column + 2 > 10:
                    continue
                for i in range(column, column + 2):
                    if board[row][i] != WATER:
                        break
                else:
                    for i in range(column, column + 2):
                        board[row][i] = SUBMARINE[i - column]
                    ship_placed = True
            else:
                # Vertical
                if row + 2 > 10:
                    continue
                for i in range(row, row + 2):
                    if board[i][column] != WATER:
                        break
                else:
                    for i in range(row, row + 2):
                        board[i][column] = SUBMARINE[i - row]
                    ship_placed = True
    return board


# Place the ship on the board.
def place_patrol_boat(board):
    for i in range(4):  # 4 patrol boats
        ship_placed = False
        while not ship_placed:
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            if board[row][column] != WATER:
                continue
            else:
                board[row][column] = PATROL
                ship_placed = True
    return board


# Update the board with the ships.
def board_update(board):
    placement = place_battleship(board)
    placement = place_destroyer(board)
    placement = place_submarine(board)
    placement = place_patrol_boat(board)
    return placement


def get_shot():
    shot = input("Enter the coordinates of the shot: ")
    if shot == "q":
        print("You quit the game.")
        from menu import menu

        menu()
    if len(shot) != 2:
        print("Please enter two characters.")
        return get_shot()
    if not shot[0].isalpha():
        print("Please enter a letter.")
        return get_shot()
    if not shot[1].isdigit():
        print("Please enter a number.")
        return get_shot()
    if ord(shot[0].upper()) < 65 or ord(shot[0].upper()) > 74:
        print("Please enter a letter between A and J.")
        return get_shot()
    if int(shot[1]) < 1 or int(shot[1]) > 10:
        print("Please enter a number between 1 and 10.")
        return get_shot()
    row = ord(shot[0].upper()) - 65  # Convert the letter to a number
    column = int(shot[1]) - 1  # Convert the number to an index
    return row, column


# Check if the shot is a hit or a miss.
def check_shot(board, row, column):
    if board[row][column] == WATER:  # If the shot finds water
        print("You missed!")
        board[row][column] = MISS  # Mark the shot as a miss
        return False
        sleep(2)
    elif (
        board[row][column] == MISS or board[row][column] == HIT
    ):  # If the shot is a repeat
        print("You already shot there!")
        sleep(2)
        return False
    else:  # If the shot finds a ship
        print("You hit a ship!")
        board[row][column] = HIT  # Mark the shot as a hit
        sleep(2)
        return True


# Check if the game is over.
def check_game_over(board):
    for row in range(10):
        for column in range(10):
            if board[row][column] in SHIP:  # If there is a ship on the board
                return False
    return True


# Ask the user if they want to play again.
def play_again():
    while True:
        again = input("Do you want to play again? (y/n) ")
        if again == "y":
            return True
        elif again == "n":
            # Go back to the main menu in menu.py
            from menu import menu

            menu()
            return False
        else:
            print("Please enter y or n.")
            continue
