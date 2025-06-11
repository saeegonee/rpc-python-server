import asyncio
import websockets
from options import Option


async def listen() -> None:

    opt = Option()
    url = f"ws://{opt.address()}:{opt.port()}"
    
    async with websockets.connect(url) as ws:
        while True:
            await ws.send(f'[0,"auth","token"]')
            # await ws.recv()
            await asyncio.sleep(0.4)


asyncio.get_event_loop().run_until_complete(listen())
