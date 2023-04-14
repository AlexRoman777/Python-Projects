import socket
import threading
import tkinter

from logic import FORMAT, HOST, PORT

name = "Switch"


class Lamp:
    def __init__(self, connection):
        self.connection = connection
        self.window = tkinter.Tk()
        self.window.title("Switch")
        self.window.geometry("200x200")
        self.window.configure(bg="dark slate gray")
        self.window.resizable(False, False)
        self.button = tkinter.Button(
            self.window, text="ON/OFF", command=self.turn_on)
        self.button.pack(fill=tkinter.BOTH, expand=True)
        self.label = tkinter.Label(self.window, text="OFF", font=("Arial", 50))
        self.label.pack(fill=tkinter.BOTH, expand=True)
        self.window.mainloop()

    def turn_on(self):
        if self.label["text"] == "OFF":
            self.label["text"] = "ON"
            self.window.configure(bg="light yellow")
            self.connection.send("turn all on")
        else:
            self.label["text"] = "OFF"
            self.window.configure(bg="dark slate gray")
            self.connection.send("turn all off")

    def turn_off(self):
        self.label["text"] = "OFF"
        self.window.configure(bg="dark slate gray")
        self.connection.send("turn all off")

    def close(self):
        self.connection.close()
        self.window.destroy()

    def receive(self):
        while True:
            message = self.connection.receive()
            if message == "turn lamp on":
                self.turn_on()
            elif message == "turn lamp off":
                self.turn_off()
            elif message == "alive":
                self.connection.send("Hej you scared me...\n".encode(FORMAT))
            elif message == "close":
                self.close()
                break


class Connection:
    def __init__(self, host, port, format):
        self.host = host
        self.port = port
        self.format = format
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connected = False
        self.connect()

    def connect(self):
        while not self.connected:
            try:
                self.client.connect((self.host, self.port))
                print(f"{name} connected on port: {self.port}")
                self.client.send(name.encode(self.format))
                self.connected = True
            except ConnectionRefusedError:
                pass

    def send(self, message):
        self.client.send(message.encode(self.format))

    def receive(self):
        return self.client.recv(1024).decode(self.format)

    def close(self):
        self.client.close()


def main():
    try:
        connection = Connection(HOST, PORT, FORMAT)
        lamp = Lamp(connection)
        receive_thread = threading.Thread(target=lamp.receive)
        receive_thread.daemon = True
        receive_thread.start()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
