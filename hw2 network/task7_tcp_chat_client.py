"""Task7
Створити простий чат на основі протоколу TCP,
який дасть змогу під'єднуватися кільком клієнтам
та обмінюватися повідомленнями.
"""

import socket
import threading

HOST, PORT = '127.0.0.1', 59999
CODE = 'utf-8'

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    """Receiving messages from server and print them"""
    while True:
        try:
            msg = client.recv(1024).decode(CODE)

            if msg == 'Send me your NICKNAME':
                client.send(nickname.encode(CODE))
            else:
                print('\r' + msg + '\nyou: ', end='')
        except:
            print("Some error.")
            client.close()
            break


def send():
    """Sending messages from client"""
    while True:
        msg = input('\ryou: ')
        msg = f'{nickname}: {msg}'
        client.send(msg.encode(CODE))


def start_client():
    """Start the threads of receiving and sending"""
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()


if __name__ == '__main__':
    start_client()
