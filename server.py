import sys
import asyncio
import logging
import websockets
from options import Option
from messages import Message
from packet import Packet
from peer_server import PeerServer


msg = Message()
log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d][%(levelname)s] %(message)s",
)


peers = {0: set()}
serv_peer = PeerServer(peers)
peers[1] = serv_peer


async def echo(socket) -> None:
    """Server func."""

    # idx = len(peers[0]) + 2
    # peer = Peer(socket, idx)
    # peers[0].add(peer)
    # peers[idx] = peer
    # log.info(msg.connect(idx))

    try:
        async for ws in socket:
            packet = Packet(ws)
            packet.extend()

            if hasattr(peers[packet.recepient], packet.action):
                # TODO. call action by name
                pass

            else:
                # TODO. send pity request
                pass

            log.info(msg.receive_msg(str(packet)))

    except websockets.ConnectionClosed as err:
        # peers[0].remove(peer)
        # del peers[idx]

        log.warning(msg.disconnect(-1, err))


async def server_task(addr: str, port: int) -> None:
    """Main server task."""

    log.info(msg.start_server(addr, port))

    async with websockets.serve(echo, addr, port):
        await asyncio.Future()


async def main() -> None:
    """Task handler."""

    opt = Option()
    addr = opt.address()
    port = opt.port()

    task0 = asyncio.create_task(server_task(addr, port))
    await task0


if __name__ == "__main__":

    args = sys.argv[1:]
    if "-v" in args:
        logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
