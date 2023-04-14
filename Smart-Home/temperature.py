import random
import socket
import threading
import tkinter as tk
from random import randint

from logic import COLOR, FORMAT, HOST, PORT, window_placement

name = "Climate Sensor"
temp = randint(0, 40)
hist = []


def update():
    with open("data/history.csv", "r") as file:
        lines = file.readlines()
        file.close()
        print("Updated")

        for line in lines:
            line = line.split(",")
            hist.append(line[1])


def update_frame():
    temperature.config(text=f"Temperature: \n{random.choice(hist)}°C")
    window.update()


def receive_commands():
    while True:
        try:
            command = client.recv(1024).decode(FORMAT)
            if command == "update":
                update_frame()

            elif command == "alive":
                client.send(f"{name} is up and running\n".encode(FORMAT))

        except ConnectionResetError:
            print("The server has disconnected")
            break

        except Exception as e:
            print(e)
            break


def close():
    try:
        client.close()
        window.destroy()
    except Exception as e:
        print(e)


def main():
    global client, window, temperature, humidity
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((HOST, PORT))
    print(f"{name} connected on port: {PORT}")
    client.send(name.encode(FORMAT))

    window = tk.Tk()
    window.title("Temperature")
    window.geometry("200x200")
    window.resizable(False, False)
    window.config(bg=COLOR)
    window_placement(window, 200, 200)
    window.configure(bg=COLOR)

    window.protocol("WM_DELETE_WINDOW", close)

    temperature = tk.Label(
        window, text=f"Temp\n{temp}°C", bg=COLOR, fg="red", font=("Arial", 30)
    )
    temperature.pack(fill=tk.BOTH, expand=True)

    try:
        receive_thread = threading.Thread(target=receive_commands)
        receive_thread.daemon = True
        receive_thread.start()
    except Exception as e:
        print(e)

    window.mainloop()


if __name__ == "__main__":
    main()
