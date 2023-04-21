'''Snake Game'''
import random
import tkinter as tk

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    '''Snake class
    Attributes:
        body_size: int
        coordinates: list
        squares: list
    '''

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for _ in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    '''Food class
    Attributes:
        coordinates: list
    '''

    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y +
                           SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    '''Next turn function
    Args:
        snake: Snake
        food: Food
    '''

    x_axis, y_axis = snake.coordinates[0]

    if direction == "Up":
        y_axis -= SPACE_SIZE
    elif direction == "Down":
        y_axis += SPACE_SIZE
    elif direction == "Left":
        x_axis -= SPACE_SIZE
    elif direction == "Right":
        x_axis += SPACE_SIZE
    snake.coordinates.insert(0, (x_axis, y_axis))
    square = canvas.create_rectangle(
        x_axis, y_axis, x_axis + SPACE_SIZE, y_axis + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x_axis == food.coordinates[0] and y_axis == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    '''Change direction function
    Args:
        new_direction: str
    '''
    global direction

    if new_direction == "Up":
        if direction != "Down":
            direction = new_direction
    elif new_direction == "Down":
        if direction != "Up":
            direction = new_direction
    elif new_direction == "Left":
        if direction != "Right":
            direction = new_direction
    elif new_direction == "Right":
        if direction != "Left":
            direction = new_direction


def check_collisions(snake):
    '''Check collisions function'''
    x_cord, y_cord = snake.coordinates[0]

    if x_cord < 0 or x_cord >= GAME_WIDTH:
        return True
    elif y_cord < 0 or y_cord >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x_cord == body_part[0] and y_cord == body_part[1]:
            return True

    return False


def game_over():
    '''Game over function'''
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       text="Game Over!", fill="red", font=("TkDefaultFont", 44))


def game_window():
    '''Game window function'''
    global score
    global direction
    global label
    global canvas
    global window

    window = tk.Tk()
    window.title("Snake")
    window.resizable(False, False)

    score = 0
    direction = "Down"

    label = tk.Label(window, text=f"Score: {score}", font=("Arial", 20))
    label.pack()

    canvas = tk.Canvas(window, width=GAME_WIDTH,
                       height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    width_center = int((screen_width // 2) - (window_width // 2))
    heigh_center = int((screen_height // 2) - (window_height // 2))

    window.geometry(f"{window_width}x{window_height}+{width_center}+{heigh_center}")

    window.bind("<Left>", lambda event: change_direction("Left"))
    window.bind("<Right>", lambda event: change_direction("Right"))
    window.bind("<Up>", lambda event: change_direction("Up"))
    window.bind("<Down>", lambda event: change_direction("Down"))

    snake = Snake()
    food = Food()
    next_turn(snake, food)

    window.mainloop()


def main():
    '''Main function'''
    game_window()


if __name__ == "__main__":
    main()
