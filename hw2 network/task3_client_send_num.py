import socket

HOST, PORT = '127.0.0.1', 8888


def verify_data(data):
    try:
        num = list(map(float, data.strip().split(',')))
        return len(num) == 2
    except ValueError:
        return False


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Connect', (HOST, PORT))

while True:
    # get numbers
    numbers = input('Enter 2 numbers by comma, e.g: 2.5,10 -> ')

    if not verify_data(numbers):
        print('Incorrect input. Try again')
        continue

    try:
        # send numbers
        client.sendto(numbers.encode('utf-8'), (HOST, PORT))
    except KeyboardInterrupt:
        client.close()
        exit()
    else:
        # get numbers
        msg = client.recv(1024)
        print(msg.decode('utf-8'))
