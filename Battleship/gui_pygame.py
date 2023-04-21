'''GUI for the game Battleship. This file contains the pygame code for the GUI.'''
import random
import pygame

from logic import Game, classic_game
from menu import menu

pygame.init()  # Initialize pygame
pygame.font.init()  # Initialize pygame font
pygame.display.set_caption("Battleship")  # Set the window title
myfont = pygame.font.SysFont("futura", 100)  # Set the font
clock = pygame.time.Clock()


SQ_SIZE = 30  # Size of each square
H_MARGIN = SQ_SIZE * 1  # Horizontal margin
V_MARGIN = SQ_SIZE  # Vertical margin

INDENT = 7  # Indentation for ships
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN  # Function to draw the text
HEIGHT = SQ_SIZE * 10 + 3 * V_MARGIN  # Function to draw the text
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the window size
HUMAN1 = True  # Wait for the player to click on a square
HUMAN2 = False  # The AI will make a move


# Colors
GREY = (40, 50, 60)
WHITE = (255, 250, 250)
GREEN = (50, 250, 150)
BLUE = (50, 150, 200)
ORANGE = (250, 140, 20)
RED = (255, 50, 100)
YELLOW = (255, 255, 0)
COLORS = {
    "U": GREY,
    "M": BLUE,
    "H": ORANGE,
    "S": RED,
}


def draw_grid(player, left=0, top=0, search=False):
    '''Function to draw the grid.'''
    for i in range(100):  # For each square
        x = left + i % 10 * SQ_SIZE  # Calculate the x position
        y = top + i // 10 * SQ_SIZE  # Calculate the y position
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)  # Create a rectangle
        pygame.draw.rect(SCREEN, WHITE, square, width=1)  # Draw the rectangle
        if search:  # If the grid is the search grid
            x += SQ_SIZE // 2  # Center the text
            y += SQ_SIZE // 2  # Center the text
            pygame.draw.circle(
                SCREEN, COLORS[player.search[i]], (x, y), radius=SQ_SIZE // 2
            )  # Draw the circle


def draw_ships(player, left=0, top=0):
    '''Function to draw the ships.'''
    for ship in player.ships:  # For each ship
        x = left + ship.col * SQ_SIZE + INDENT  # Calculate the x position
        y = top + ship.row * SQ_SIZE + INDENT  # Calculate the y position
        if ship.orientation == "h":  # If the ship is horizontal
            width = SQ_SIZE * ship.size - INDENT * 2  # Calculate the width
            height = SQ_SIZE - INDENT * 2  # Calculate the height
        else:  # If the ship is vertical
            width = SQ_SIZE - INDENT * 2  # Calculate the width
            height = SQ_SIZE * ship.size - INDENT * 2  # Calculate the height
        rectangle = pygame.Rect(x, y, width, height)  # Create a rectangle
        pygame.draw.rect(
            SCREEN, GREEN, rectangle, border_radius=10
        )  # Draw the rectangle


game = Game(HUMAN1, HUMAN2)


ANIMATING = True
PAUSING = False

while ANIMATING:

    # Track user interaction
    for event in pygame.event.get():  # For each event

        # user clicks the close button
        if event.type == pygame.QUIT:
            ANIMATING = False
            pygame.quit()
            menu()  # Return to the menu in terminal for now

        # User clicks on mouse
        if (
            event.type == pygame.MOUSEBUTTONDOWN and not game.over
        ):  # If the game is not over
            x, y = pygame.mouse.get_pos()  # Get the mouse position
            if (
                game.player_turn and x > SQ_SIZE * 10 + V_MARGIN and y < SQ_SIZE * 10
            ):  # If it is the player's turn and the click is on the search grid
                row = y // SQ_SIZE  #
                col = (x - H_MARGIN - SQ_SIZE * 10) // SQ_SIZE
                index = row * 10 + col  # Calculate the index
                game.make_move(index)  # Make a move

            elif (
                not game.player_turn and x < SQ_SIZE * 10 and y < SQ_SIZE * 10
            ):  # If it is the computer's turn and the click is on the position grid
                row = y // SQ_SIZE
                col = x // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)

        # User presses the key "d" to toggle the difficulty
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            # Choose easy on the first press, medium on the second press, and hard on the third press
            if game.dificulty == "easy":
                game.dificulty = "medium"
            elif game.dificulty == "medium":
                game.dificulty = "hard"
            else:
                game.dificulty = "easy"

        # User presses the key "t" to toggle the type of game, classic or modern
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            classic_game(False)
            game = Game(HUMAN1, HUMAN2)

        # Press "c" for classic game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            classic_game(True)
            game = Game(HUMAN1, HUMAN2)

        # user presses a key
        if event.type == pygame.KEYDOWN:

            # Escape key
            if event.key == pygame.K_ESCAPE:
                ANIMATING = False
                pygame.quit()
                menu()

            # user presses the space bar pause the game and write a message to the screen "Paused"
            if event.key == pygame.K_SPACE:
                PAUSING = not PAUSING
                if PAUSING:
                    text = myfont.render("Paused", False, YELLOW)
                    SCREEN.blit(
                        text,
                        (
                            WIDTH // 2 - text.get_width() // 2,
                            HEIGHT // 2 - text.get_height() // 2,
                        ),
                    )
                    pygame.display.flip()
                else:
                    continue

            # Return key to restart the game
            if event.key == pygame.K_RETURN:
                game = Game(HUMAN1, HUMAN2)
                game.dificulty = random.choice(["easy", "medium", "hard"])

    # Execution
    if not PAUSING:

        # draw background
        SCREEN.fill(GREY)

        # Draw search grids
        draw_grid(game.computer, search=True)
        draw_grid(game.player, left=SQ_SIZE * 10 + H_MARGIN, search=True)

        # Draw position grids
        draw_grid(game.player)
        draw_grid(game.computer, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)

        # Draw ships onto position grids
        draw_ships(game.player)
        name = "Player"

        # Draw the names and information at the bottom of the screen
        player_name = f"{name} board  Hits left: {game.computer_hits_left}"
        font = pygame.font.SysFont("Arial", 18)
        player = (
            font.render(player_name, True, BLUE)
            if game.player_turn
            else font.render(player_name, True, WHITE)
        )
        computer = font.render(
            f"Computer board  Hits left: {game.player_hits_left}", True, BLUE
        )
        dificulty = game.dificulty
        mesaj_second = font.render(f"Dificulty: {dificulty}", True, WHITE)
        mesaj_third = font.render(
            f"Player's turn: {game.player_turn}, Game over: {game.over}", True, RED
        )
        space_key = font.render(
            "Press Space to pause, Enter to restart, D for difficulty, M or C for type of game",
            True,
            RED,
        )
        enter_key = font.render(f"Difficulty: {dificulty}", True, RED)

        SCREEN.blit(player, (0, HEIGHT - SQ_SIZE * 3))
        SCREEN.blit(computer, (WIDTH // 2 + H_MARGIN // 2, HEIGHT - SQ_SIZE * 3))
        SCREEN.blit(mesaj_second, (0, HEIGHT - SQ_SIZE * 2))
        SCREEN.blit(space_key, (0, HEIGHT - SQ_SIZE))

        # Game difficulty, this is setting the AI's difficulty
        if not game.over and game.computer_turn:
            if game.dificulty == "easy":
                game.easy_ai()
            elif game.dificulty == "medium":
                game.medium_ai()
            elif game.dificulty == "hard":
                game.hard_ai()

        if game.over:
            if str(game.result) == "1":
                text = myfont.render("You won!", False, YELLOW)
            else:
                draw_ships(game.computer, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)
                text = myfont.render("You lost!", False, YELLOW)

            SCREEN.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )

        # Update the display
        pygame.time.wait(0)  # Wait x milliseconds, good to slow down the game
        pygame.display.flip()  # Update the display
        clock.tick(60)  # 60 frames per second


pygame.quit()  # Quit pygame
