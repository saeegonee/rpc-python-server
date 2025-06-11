import sys
import asyncio
import logging
from uuid import uuid4
import websockets
from room_handler import RoomHandlerCommon
from room import Room
from packet import Packet
from client import Client
from stuff.options import ADDRESS, PORT, ROOM_TIMEOUT
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
        self.__client_counter: int = 0
        self.__rooms: dict[str, Room] = {}

    async def _check_room_clients(self) -> None:
        for uuid, room in self.__rooms.items():
            if room.client_count == 0: 
                del self.__rooms[uuid]
                log.info(lmsg.destroy_room(uuid))

    async def _listen_room(self) -> None:
        while True:
            await asyncio.sleep(ROOM_TIMEOUT)
            await self._check_room_clients()

    async def _listen_socket(self, wsocket: websockets.ServerConnection) -> None:

        # Room
        uuid = str(uuid4())
        room_handle = RoomHandlerCommon()
        room = Room(uuid, room_handle)
        self.__rooms[uuid] = room
        
        # client
        idx = self.__client_counter + 1
        client = Client(idx, wsocket)
        self.__client_counter += 1
        await self.__rooms[uuid].visit(client)

        # Handler
        try:
            async for msg in wsocket:
                packet = Packet(msg)
                await room.process(packet)                

        except websockets.ConnectionClosed as err:
            await room.leave(client)
            log.warning(lmsg.disconnect(idx, err))

    async def _socket_run(self) -> None:
        log.info(lmsg.start_server())
        async with websockets.serve(self._listen_socket, ADDRESS, PORT):
            await asyncio.Future()

    async def start(self) -> None:
        task0 = asyncio.create_task(self._socket_run())
        task1 = asyncio.create_task(self._listen_room())
        
        await task0
        await task1

    def stop(self) -> None:
        """Force stop the server."""


if __name__ == "__main__":

    args = sys.argv[1:]
    if "-v" in args:
        logging.basicConfig(level=logging.INFO)

    serv = Server()
    asyncio.run(serv.start())
