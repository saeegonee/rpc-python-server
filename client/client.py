import asyncio
import websockets


async def listen() -> None:
    url = "ws://127.0.0.1:1909"
    async with websockets.connect(url) as ws:
        while True:
            inp = input("<target>,<func>,<payload>: ")
            l_pack = inp.split(",")

            await ws.send(f'[{l_pack[0]},"{l_pack[1]}","{l_pack[2]}"]')
            msg = await ws.recv()
            print(f"Get msg: {msg}")


asyncio.get_event_loop().run_until_complete(listen())
