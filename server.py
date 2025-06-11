import sys
import asyncio
import logging
from uuid import uuid4
import websockets
from room import Room
from packet import Packet
from client import Client
from stuff.options import Option
from stuff.messages import Message


lmsg = Message()
log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d][%(levelname)s] %(message)s",
)


class Server(object):
    def __init__(self) -> None:
        self.__client_counter: int = 2
        self.__rooms: dict[str, Room] = {}

    async def _listen_socket(self, wsocket: websockets.ServerConnection) -> None:

        # Room
        uuid = str(uuid4())
        room = Room(uuid)
        self.__rooms[uuid] = room
        
        # client
        idx = self.__client_counter + 1
        client = Client(idx, wsocket)
        self.__rooms[uuid].visit(client)
        self.__client_counter += 1

        # Handler
        try:
            async for msg in wsocket:
                packet = Packet(msg)
                packet.extend()

                log.info(lmsg.receive_msg(str(packet)))

        except websockets.ConnectionClosed as err:
            room.leave(client)
            log.warning(lmsg.disconnect(idx, err))

    async def _task(self, addr: str, port: int) -> None:
        log.info(lmsg.start_server())

        async with websockets.serve(self._listen_socket, addr, port):
            await asyncio.Future()

    async def start(self) -> None:
        opt = Option()
        addr = opt.address()
        port = opt.port()

        task0 = asyncio.create_task(self._task(addr, port))
        await task0

    def stop(self) -> None:
        """Force stop the server."""


if __name__ == "__main__":

    args = sys.argv[1:]
    if "-v" in args:
        logging.basicConfig(level=logging.INFO)

    serv = Server()
    asyncio.run(serv.start())
