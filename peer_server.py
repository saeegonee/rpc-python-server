import logging

from websockets import ServerConnection
from options import Option
from packet import Packet
from peer import Peer


log = logging.getLogger(__name__)
opt = Option()


class PeerServer(object):
    def __init__(self, peers: dict) -> None:
        self.__peers: dict = peers

    async def auth(self, wsocket: ServerConnection, packet: Packet) -> None:
        if self.check_token(packet.payload[0]):
            idx = self.get_idx()
            peer = Peer(wsocket, idx)
            
            self.__peers[0].append(peer)
            self.__peers[idx] = peer
            
            rqst = Packet(f'["{peer.id}", "auth", "1"]')
            await peer.send(rqst)

    def check_token(self, token: str) -> bool:
        if token == opt.token():
            return True
        return False

    def get_idx(self) -> int:
        return len(self.__peers[0]) + 2
