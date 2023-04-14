import socket
import sys
import threading
from random import randint

from logic import FORMAT, HOST, PORT

devices = []
names = []


def device_alive():
    devices_alive = f"Devices connected: {len(names)}\n"
    return devices_alive


def receive_history(device_socket):
    try:
        with open(f"received/history{randint(1, 300)}.csv", "wb") as file:
            data = device_socket.recv(1024)
            while data:
                file.write(data)
                data = device_socket.recv(1024)
            file.close()
    except Exception as e:
        print(e)

    print("History received")


def device_thread(device_socket, name):
    try:
        while True:
            sock_data = device_socket.recv(1024).decode(FORMAT)
            print(f"{name} sent: {sock_data if sock_data else 'Goodbye'}")

            if sock_data == "devices":
                device_socket.send(device_alive().encode(FORMAT))
                print(f"Devices connected: {len(names)}")
            elif sock_data == "history":
                receive_history(device_socket)
                print("History received")
            elif sock_data == "alive":
                device_socket.send("Server always on duty".encode(FORMAT))
                for device in devices:
                    device.send("alive".encode(FORMAT))

            else:
                for device in devices:
                    device.send(sock_data.encode(FORMAT))

            if not sock_data:
                devices.remove(device_socket)
                names.remove(name)
                # print(f"{name} disconnected")

                for device in devices:
                    device.send(f"{name} disconnected".encode(FORMAT))
                break

        device_socket.close()
    except Exception as e:
        print(e)


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server is listening on port " + str(PORT))

    while True:
        try:
            device_socket, device_adress = server_socket.accept()
            name = device_socket.recv(1024).decode(FORMAT)
            devices.append(device_socket)
            names.append(name)

            print(f"{name} connected on port {device_adress[1]}")
            device_socket.send(
                "Server Message: Connection confirmed".encode(FORMAT))

            server_threading = threading.Thread(
                target=device_thread, args=(device_socket, name)
            )
            server_threading.daemon = True
            server_threading.start()

        except KeyboardInterrupt:
            sys.stdout.write("\x1b[1A\x1b[2K")
            print("\nServer is down, no more connections")
            server_socket.close()
            break

        except Exception as e:
            print(e)
            break

    server_socket.close()


if __name__ == "__main__":
    main()
