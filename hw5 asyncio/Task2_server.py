""""Task2
Розробіть сокет-сервер на основі бібліотеки asyncio.
"""

import socket
import asyncio

HOST, PORT = '127.0.0.1', 59997
CODE = 'utf-8'


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    """Get message from client and print it"""

    data = None
    while data != b'quit':
        try:
            data = await reader.read(255)
            message = data.decode(CODE)
            if data:
                addr, port = writer.get_extra_info("peername")
                print(f'{addr}:{port}: {message}')
        except Exception as err:
            print(err)
            writer.close()
            break

    writer.close()
    await writer.wait_closed()


async def run_server():
    print('Server starts')
    while True:
        serv = await asyncio.start_server(handle_client, HOST, PORT)
        async with serv:
            await serv.serve_forever()


if __name__ == "__main__":
    asyncio.run(run_server())
