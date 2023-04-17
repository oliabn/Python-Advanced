"""Task7
Створити простий чат на основі протоколу TCP,
який дасть змогу під'єднуватися кільком клієнтам
та обмінюватися повідомленнями.
"""

import socket
import threading

HOST, PORT = '127.0.0.1', 59999
CODE = 'utf-8'

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
print(f'Listen at {HOST}:{PORT}')
serv.listen()

clients = []
addresses = []
nicknames = []


def broadcast(msg, addr):
    """Send message to all others clients"""
    for client, address in zip(clients, addresses):
        if address == addr:
            continue
        client.send(msg)


def handle(client, addr):
    """Get message from certain client (in arg) and send it to all others clients"""
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, addr)
        except:
            index_of_removing_user = clients.index(client)
            clients.remove(client)
            client.close()
            nickname_of_removing_user = nicknames[index_of_removing_user]
            broadcast(f'{nickname_of_removing_user} left the chat'.encode(CODE), addr)
            nicknames.remove(nickname_of_removing_user)
            break


def receive_clients():
    """Receiving clients and start a handle_of_client thread for each"""
    while True:
        client, addr = serv.accept()
        print(f"{addr} was connected")

        client.send("Send me your NICKNAME".encode(CODE))
        nickname = client.recv(1024).decode(CODE)
        nicknames.append(nickname)
        clients.append(client)
        addresses.append(addr)

        print(f"Client's nickname: {nickname}")
        broadcast(f'{nickname} joined to chat'.encode(CODE), addr)
        client.send('You are joined to chat'.encode(CODE))

        handle_of_client = threading.Thread(target=handle, args=(client, addr,))
        handle_of_client.start()


if __name__ == "__main__":
    receive_clients()
