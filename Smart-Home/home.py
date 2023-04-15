import socket
import threading
import tkinter as tk
from time import sleep

import PIL.Image
import PIL.ImageTk

from logic import COLOR, FORMAT, HEIGHT_B, HOST, PORT, WIDTH_B, window_placement

past = []
connection = "Disconnected" if threading.active_count() == 0 else "Connected"
name = "Control Panel"
active_clients = 0


def simple_test(a, b):
    return a + b


def radio_commands(radio):
    if radio == 1:
        if radio1["bg"] == "blue":
            radio1["text"] = "Lights\nOn"
            radio1["bg"] = "green"
            message = "all on"
            client.send(message.encode(FORMAT))
        else:
            radio1["bg"] = "blue"
            radio1["text"] = "Lights\nOff"
            message = "all off"
            client.send(message.encode(FORMAT))

    elif radio == 2:
        message = "history"
        client.send(message.encode(FORMAT))

    elif radio == 3:
        message = "update"
        client.send(message.encode(FORMAT))

    elif radio == 4:
        message = "devices"
        client.send(message.encode(FORMAT))


def send_command():
    command = write_area.get()
    history.configure(state=tk.NORMAL)
    history.insert(tk.END, f"{command}\n")
    past.append(command)
    history.see(tk.END)
    history.configure(state=tk.DISABLED)
    write_area.delete(0, tk.END)
    client.send(command.encode(FORMAT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            history.configure(state=tk.NORMAL)
            history.insert(tk.END, f"{message}\n")
            history.see(tk.END)
            history.configure(state=tk.DISABLED)

        except ConnectionResetError:
            print("The server has disconnected")
            client.close()
            break


def alive():
    client.send("alive".encode(FORMAT))
    sleep(1)
    client.send(f"{name} reporting for duty".encode(FORMAT))


def main():
    global client, history, write_area, radio1, radio2, radio3, radio4

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    client.connect((HOST, PORT))
    client.send(name.encode(FORMAT))
    print(f"{name} connected on port: {PORT}")

    window = tk.Tk()
    window.title("Smart Home")
    window.geometry("640x480")
    window.resizable(False, False)
    window_placement(window, WIDTH_B, HEIGHT_B)
    window.configure(bg=COLOR)

    top_frame = tk.Frame(window, bg=COLOR, width=640, height=110)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    top_frame_label = tk.Label(
        top_frame, text="Home Automation", font=("Arial", 30), bg=COLOR, fg="white"
    )
    top_frame_label.place(relx=0.55, rely=0.5, anchor=tk.CENTER)

    logo = PIL.Image.open("images/logo.png")
    logo = logo.resize((100, 100), PIL.Image.Resampling.LANCZOS)
    logo = PIL.ImageTk.PhotoImage(logo)
    logo_label = tk.Label(top_frame, image=logo, bg=COLOR)
    logo_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
    logo_label.pack(side=tk.LEFT, padx=20)

    middle_frame = tk.Frame(window, bg=COLOR, width=640, height=310)
    middle_frame.pack(side=tk.TOP, fill=tk.X)

    middle_frame_1 = tk.Frame(middle_frame, bg=COLOR, width=140, height=310)
    middle_frame_1.pack(side=tk.LEFT, fill=tk.X, expand=False)

    middle_frame_2 = tk.Frame(middle_frame, bg=COLOR, width=310, height=310)
    middle_frame_2.pack(side=tk.LEFT, fill=tk.X, expand=False)

    middle_frame_3 = tk.Frame(middle_frame, bg=COLOR, width=190, height=310)
    middle_frame_3.pack(side=tk.LEFT, fill=tk.X, expand=False)

    bottom_frame = tk.Frame(window, bg=COLOR, width=640, height=60)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    bottom_frame_label = tk.Label(
        bottom_frame,
        text=f"Server status: {connection}",
        font=("Arial", 15),
        bg=COLOR,
        fg="white",
        highlightthickness=0,
    )
    bottom_frame_label.place(relx=0.16, rely=0.5, anchor=tk.CENTER)

    history = tk.Text(
        middle_frame_3,
        bg=COLOR,
        fg="white",
        state=tk.DISABLED,
        font=("Arial", 10),
        wrap=tk.WORD,
        relief=tk.FLAT,
        borderwidth=0,
        highlightthickness=0,
    )
    history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    write_area = tk.Entry(
        middle_frame_3,
        bg="black",
        fg="white",
        font=("Arial", 18),
        relief=tk.FLAT,
        borderwidth=0,
        highlightthickness=0,
    )

    radio1 = tk.Radiobutton(
        middle_frame_1,
        text="Lights\nOn/Off",
        bg="blue",
        fg="white",
        width=15,
        height=5,
        indicatoron=False,
        command=lambda: radio_commands(1),
        value=1,
    )

    radio2 = tk.Radiobutton(
        middle_frame_1,
        text="Send History",
        bg="blue",
        fg="white",
        width=15,
        height=5,
        indicatoron=False,
        command=lambda: radio_commands(2),
        value=2,
    )

    radio3 = tk.Radiobutton(
        middle_frame_1,
        text="Update\nTemperature",
        bg="blue",
        fg="white",
        width=15,
        height=5,
        indicatoron=False,
        command=lambda: radio_commands(3),
        value=3,
    )

    radio4 = tk.Radiobutton(
        middle_frame_1,
        text="Active\nDevices",
        bg="blue",
        fg="white",
        width=15,
        height=5,
        indicatoron=False,
        command=lambda: radio_commands(4),
        value=4,
    )

    radio1.pack(side=tk.TOP, fill=tk.X, expand=True)
    radio2.pack(side=tk.TOP, fill=tk.X, expand=True)
    radio3.pack(side=tk.TOP, fill=tk.X, expand=True)
    radio4.pack(side=tk.TOP, fill=tk.X, expand=True)

    history_button = tk.Button(
        middle_frame_3,
        text="Who's home?",
        command=lambda: alive(),
    )
    send_button = tk.Button(
        middle_frame_3,
        text="Send Command",
        command=lambda: send_command(),
    )

    history_button.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
    send_button.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
    write_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    try:

        receiving_thread = threading.Thread(target=receive)
        receiving_thread.daemon = True
        receiving_thread.start()
    except Exception as e:
        print(e)

    window.mainloop()


if __name__ == "__main__":  # pragma: no cover
    main()
