"""Task2
Створіть UDP-сервер, який очікує на повідомлення про
нові пристрої в мережі. Він приймає повідомлення певного
формату, де буде ідентифікатор пристрою, і друкує нові
під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме
унікальний ідентифікатор пристрою на сервер, повідомляючи про
свою присутність.
"""

import socket

HOST = '127.0.0.1'
PORT = 9999
CODE = "utf-8"

clients = []


def listen(host: str = HOST, port: int = PORT):
    """Listen all clients and sending an incoming message to all another"""

    def broadcast(addr, msg):
        """Send msg to all another clients"""
        for client in clients:
            if client == addr:
                continue
            server.sendto(msg.encode(CODE), client)

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f'Listen at {host}:{port}')

    while True:
        try:
            msg, addr = server.recvfrom(65535)
        except ConnectionResetError as ex:
            print(ex)

        if addr not in clients:
            clients.append(addr)

        if not msg:
            continue

        client_id = f'{addr[0]}:{addr[1]}'
        # join new client if his msg -> 'join'
        if msg.decode(CODE) == '__join__':
            print(f'Client {client_id} joined')
            continue

        # send msg to all another clients
        msg = f'{client_id}: {msg.decode(CODE)}'
        broadcast(addr, msg)


if __name__ == '__main__':
    listen()
