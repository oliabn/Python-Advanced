"""Task2
Створіть UDP-сервер, який очікує на повідомлення про
нові пристрої в мережі. Він приймає повідомлення певного
формату, де буде ідентифікатор пристрою, і друкує нові
під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме
унікальний ідентифікатор пристрою на сервер, повідомляючи про
свою присутність.
"""


import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 9999
CODE = "utf-8"


def listen(sock: socket.socket):
    """Getting messages from server and print them"""
    while True:
        msg = sock.recv(65535)
        print(f'\r\r{msg.decode(CODE)}\n'
              f'you: ', end='')


def send(sock: socket.socket):
    """Enter messages and sending them to servet"""
    while True:
        msg = input('you: ')
        sock.send(msg.encode(CODE))


def connect(host: str = HOST, port: int = PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))

    # send 'join' to server for join
    sock.send('__join__'.encode(CODE))

    # getting messages endlessly
    receiving_msg_thread = threading.Thread(target=listen, args=(sock,))
    # sending messages endlessly
    sending_msg_thread = threading.Thread(target=send, args=(sock,))

    receiving_msg_thread.start()
    sending_msg_thread.start()
    while True:
        pass


if __name__ == '__main__':
    # os.system('cls')
    connect()
