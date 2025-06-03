import asyncio
import logging
import websockets
from options import Option
from messages import Message


peers = set()


async def proc(socket) -> None:
    """Server func."""

    msg = Message()

    try:
        async for msg in socket:
            print(msg.receive_msg(msg))
            await socket.send(msg)

    except websockets.ConnectionClosed as err:
        print(msg.disconnect(err))


async def server_task(addr: str, port: int) -> None:
    """Main server task."""

    msg = Message()
    print(msg.start_server(addr, port))

    async with websockets.serve(proc, addr, port):
        await asyncio.Future()


async def main() -> None:
    """Task handler."""

    opt = Option()
    addr = opt.address()
    port = opt.port()

    task0 = asyncio.create_task(server_task(addr, port))
    await task0


if __name__ == "__main__":
    asyncio.run(main())
