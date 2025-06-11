import sys
import asyncio
import logging
from client import Client
from modifier import Workshop
import websockets
from options import Option
from messages import Message
from packet import Packet

# from peer_server import PeerServer


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
        self.__clients: dict = {1: Workshop()}

    async def _listen_socket(self, wsocket: websockets.ServerConnection) -> None:
        idx = self.__client_counter + 1
        client = Client(idx, wsocket)
        self.__clients[idx] = client
        self.__client_counter += 1
        log.info(lmsg.connect(idx))

        try:
            async for msg in wsocket:
                packet = Packet(msg)
                packet.extend()

                # TODO. call action by name
                # if hasattr(peers[packet.recepient], packet.action):

                # TODO. send pity request to client
                # else:

                log.info(lmsg.receive_msg(str(packet)))

        except websockets.ConnectionClosed as err:
            del self.__clients[idx]
            log.warning(lmsg.disconnect(idx, err))

    async def _task(self, addr: str, port: int) -> None:
        log.info(lmsg.start_server(addr, port))

        async with websockets.serve(self._listen_socket, addr, port):
            await asyncio.Future()

    async def start(self) -> None:
        opt = Option()
        addr = opt.address()
        port = opt.port()

        task0 = asyncio.create_task(self._task(addr, port))
        await task0


if __name__ == "__main__":

    args = sys.argv[1:]
    if "-v" in args:
        logging.basicConfig(level=logging.INFO)

    serv = Server()
    asyncio.run(serv.start())
