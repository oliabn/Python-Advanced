"""Task3
Створіть сокет, який приймає повідомлення з двома числами,
що розділені комою. Сервер має конвертувати рядкове повідомлення
у два числа й обчислювати його суму. Після успішного обчислення
повертати відповідь клієнту.
"""

import socket

HOST, PORT = '127.0.0.1', 8888


def get_sum(data):
    """Return str with sum of received numbers"""
    numbers = data.decode('utf-8')
    numbers = list(map(float, numbers.strip().split(',')))
    return str(sum(numbers))


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
server.bind((HOST, PORT))
print(f'Listen at {HOST}:{PORT}')


while True:

    # received_data = server.recv(1024)
    received_data, addr = server.recvfrom(65535)
    if received_data.decode('utf-8') == 'Connect':
        print(f"{addr} is connected")
        continue

    if not received_data:
        continue

    print('Received data:', received_data.decode('utf-8'))

    # send sum of numbers
    msg = get_sum(received_data)
    server.sendto(msg.encode('utf-8'), addr)
