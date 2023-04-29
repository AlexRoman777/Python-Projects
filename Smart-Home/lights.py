import socket
import sys
import threading
import tkinter as tk

from logic import COLOR, FORMAT, HOST, OFF, ON, PORT, window_placement

name = "Full House"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((HOST, PORT))
print("Connected to server")
client.send(name.encode(FORMAT))


window = tk.Tk()
window.title("Home Appliances")
window.geometry("640x480")
window.resizable(False, False)
window_placement(window, 640, 480)
window.configure(bg=COLOR)


top_frame = tk.Frame(window, bg=COLOR, width=640, height=160)
top_frame.pack(side=tk.TOP, fill=tk.X)

led_1 = tk.Frame(top_frame, bg=ON, width=140, height=140, highlightthickness=0)
led_1.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

led_2 = tk.Frame(top_frame, bg=ON, width=140, height=140, highlightthickness=0)
led_2.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

led_3 = tk.Frame(top_frame, bg=ON, width=140, height=140, highlightthickness=0)
led_3.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

led_4 = tk.Frame(top_frame, bg=ON, width=140, height=140, highlightthickness=0)
led_4.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

middle_frame = tk.Frame(window, bg=COLOR, width=640, height=160)
middle_frame.pack(side=tk.TOP, fill=tk.X)

speaker_1 = tk.Frame(middle_frame, bg=ON, width=140, height=140, highlightthickness=0)
speaker_1.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

speaker_2 = tk.Frame(middle_frame, bg=ON, width=140, height=140, highlightthickness=0)
speaker_2.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

speaker_3 = tk.Frame(middle_frame, bg=ON, width=140, height=140, highlightthickness=0)
speaker_3.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

speaker_4 = tk.Frame(middle_frame, bg=ON, width=140, height=140, highlightthickness=0)
speaker_4.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

bottom_frame = tk.Frame(window, bg=COLOR, width=640, height=90)
bottom_frame.pack(side=tk.TOP, fill=tk.X)

door = tk.Frame(bottom_frame, bg=ON, width=140, height=140, highlightthickness=0)
door.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

window = tk.Frame(bottom_frame, bg=ON, width=140, height=140, highlightthickness=0)
window.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

garage = tk.Frame(bottom_frame, bg=ON, width=140, height=140, highlightthickness=0)
garage.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

vacuum = tk.Frame(bottom_frame, bg=ON, width=140, height=140, highlightthickness=0)
vacuum.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)


# Write thte names of the appliances in the middle of the frames
def write_appliance_names():
    led_1_name = tk.Label(led_1, text="LED 1", bg=COLOR)
    led_1_name.pack(expand=True)

    led_2_name = tk.Label(led_2, text="LED 2", bg=COLOR)
    led_2_name.pack(expand=True)

    led_3_name = tk.Label(led_3, text="LED 3", bg=COLOR)
    led_3_name.pack(expand=True)

    led_4_name = tk.Label(led_4, text="LED 4", bg=COLOR)
    led_4_name.pack(expand=True)

    speaker_1_name = tk.Label(speaker_1, text="Speaker 1", bg=COLOR)
    speaker_1_name.pack(expand=True)

    speaker_2_name = tk.Label(speaker_2, text="Speaker 2", bg=COLOR)
    speaker_2_name.pack(expand=True)

    speaker_3_name = tk.Label(speaker_3, text="Speaker 3", bg=COLOR)
    speaker_3_name.pack(expand=True)

    speaker_4_name = tk.Label(speaker_4, text="Speaker 4", bg=COLOR)
    speaker_4_name.pack(expand=True)

    door_name = tk.Label(door, text="Door", bg=COLOR)
    door_name.pack(expand=True)

    window_name = tk.Label(window, text="Window", bg=COLOR)
    window_name.pack(expand=True)

    garage_name = tk.Label(garage, text="Garage", bg=COLOR)
    garage_name.pack(expand=True)

    vacuum_name = tk.Label(vacuum, text="Vacuum", bg=COLOR)
    vacuum_name.pack(expand=True)


def receive():
    while True:
        message = client.recv(1024).decode(FORMAT)

        messages_dict = {
            "led 1 on": lambda: led_1.configure(bg=ON),
            "led 2 on": lambda: led_2.configure(bg=ON),
            "led 3 on": lambda: led_3.configure(bg=ON),
            "led 4 on": lambda: led_4.configure(bg=ON),
            "speaker 1 on": lambda: speaker_1.configure(bg=ON),
            "speaker 2 on": lambda: speaker_2.configure(bg=ON),
            "speaker 3 on": lambda: speaker_3.configure(bg=ON),
            "speaker 4 on": lambda: speaker_4.configure(bg=ON),
            "door": lambda: door.configure(bg=ON),
            "window": lambda: window.configure(bg=ON),
            "garage": lambda: garage.configure(bg=ON),
            "vacuum": lambda: vacuum.configure(bg=ON),
            "led 1 off": lambda: led_1.configure(bg=OFF),
            "led 2 off": lambda: led_2.configure(bg=OFF),
            "led 3 off": lambda: led_3.configure(bg=OFF),
            "led 4 off": lambda: led_4.configure(bg=OFF),
            "speaker 1 off": lambda: speaker_1.configure(bg=OFF),
            "speaker 2 off": lambda: speaker_2.configure(bg=OFF),
            "speaker 3 off": lambda: speaker_3.configure(bg=OFF),
            "speaker 4 off": lambda: speaker_4.configure(bg=OFF),
            "door off": lambda: door.configure(bg=OFF),
            "window off": lambda: window.configure(bg=OFF),
            "garage off": lambda: garage.configure(bg=OFF),
            "vacuum off": lambda: vacuum.configure(bg=OFF),
        }

        if message in messages_dict:
            print("Executing: " + message)
            messages_dict[message]()
        elif message == "alive":
            client.send(f"{name} is alive also...\n".encode(FORMAT))

        elif message == "turn lamps on":
            for i in [led_1, led_2, led_3, led_4]:
                i.configure(bg=ON)
        elif message == "turn lamps off":
            for i in [led_1, led_2, led_3, led_4]:
                i.configure(bg=OFF)
        elif message == "turn speakers on":
            for i in [speaker_1, speaker_2, speaker_3, speaker_4]:
                i.configure(bg=ON)
        elif message == "turn speakers off":
            for i in [speaker_1, speaker_2, speaker_3, speaker_4]:
                i.configure(bg=OFF)

        else:
            print(message)


receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()
if not receive_thread.is_alive():
    print("Thread is dead")
    client.close()
    window.destroy()
    sys.exit()

window.mainloop()


def main():
    pass


if __name__ == "__main__":
    main()
