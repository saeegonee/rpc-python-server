from asyncio.windows_events import _overlapped
import websockets
import asyncio
from options import Option


async def listen() -> None:

    opt = Option()
    url = f"ws://{opt.address()}:{opt.port()}"
    
    async with websockets.connect(url) as ws:
        await ws.send("PING")
        while True:
            msg = await ws.recv()
            print(f"Receive msg: {msg}")


asyncio.get_event_loop().run_until_complete(listen())
