import asyncio
import logging
import websockets
from options import Option
from messages import Message


log = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d][%(levelname)s] %(message)s",
        )


peers = set()


async def proc(socket) -> None:
    """Server func."""

    msg = Message()

    try:
        async for msg in socket:
            log.info(msg.receive_msg(msg))
            await socket.send(msg)

    except websockets.ConnectionClosed as err:
        log.warning(msg.disconnect(err))


async def server_task(addr: str, port: int) -> None:
    """Main server task."""

    msg = Message()
    log.info(msg.start_server(addr, port))

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
