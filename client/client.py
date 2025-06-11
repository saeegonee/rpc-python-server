import asyncio
import websockets


async def listen() -> None:
    url = "ws://127.0.0.1:1909"
    async with websockets.connect(url) as ws:
        while True:
            await ws.send(f'[1,"auth","token"]')
            await asyncio.sleep(0.4)


asyncio.get_event_loop().run_until_complete(listen())
