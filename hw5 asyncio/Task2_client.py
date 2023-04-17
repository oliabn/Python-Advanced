import asyncio
from aioconsole import ainput

HOST, PORT = '127.0.0.1', 59997
CODE = 'utf-8'


async def run_client() -> None:
    reader, writer = await asyncio.open_connection(HOST, PORT)
    message = "I've connected"
    writer.write(message.encode(CODE))
    await writer.drain()

    print('Enter <quit> for exit')
    while message != 'quit':
        try:
            message = await ainput(">> ")
            if message:
                writer.write(message.encode(CODE))
                await writer.drain()
        except Exception:
            writer.close()
    if writer:
        writer.close()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_client())


# import socket
#
# HOST, PORT = '127.0.0.1', 59999
# CODE = 'utf-8'
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# sock.connect((HOST, PORT))
# sock.send(b"I've connected")
#
# message = None
# print('Enter <quit> for exit')
# while message != 'quit':
#     try:
#         message = input('>> ')
#         if message:
#             sock.send(message.encode(CODE))
#     except KeyboardInterrupt:
#         sock.close()
#         break
