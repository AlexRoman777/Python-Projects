from random import randint

HOST = "localhost"
PORT = 54321
FORMAT = "utf-8"

WIDTH_S = 200
HEIGHT_S = 200

WIDTH_B = 640
HEIGHT_B = 480

ON = "yellow"
OFF = "black"
COLOR = "dark slate gray"

WIDTH_F = 200
HEIGHT_F = 480


def window_placement(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    # Random placement around the center of the screen
    x = randint(int(x - (screen_width * 0.1)), int(x + (screen_width * 0.1)))
    y = randint(int(y - (screen_height * 0.1)), int(y + (screen_height * 0.1)))
    window.geometry(f"{int(width)}x{int(height)}+{int(x)}+{int(y)}")
