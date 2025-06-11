import logging
from client import Client
from packet import Packet
from stuff.messages import Message


lmsg = Message()
log = logging.getLogger(__name__)


class Room(object):
    def __init__(self, idx: str, handler) -> None:
        self.__idx: str = idx
        self.__clients: dict[int, Client] = {}
        self.__handler = handler

        log.info(lmsg.create_room(idx))

    def __del__(self) -> None:
        log.info(lmsg.destroy_room(self.__idx))

    @property
    def client_count(self) -> int:
        return len(self.__clients.keys())

    async def visit(self, client: Client) -> None:
        if client in self.__clients.values():
            return
        self.__clients[client.id] = client
        log.info(lmsg.visit_room(self.__idx, client.id))

    async def leave(self, client: Client) -> None:
        if not client in self.__clients.values():
            return
        del self.__clients[client.id]
        log.info(lmsg.leave_room(self.__idx, client.id))

    async def process(self, pck: Packet) -> None:
        try:
            trg = getattr(self.__handler, pck.action)
            trg(pck.payload)
        except Exception as err:
            log.info(lmsg.method_error(pck.action, err))

    async def message(self, pck: Packet) -> None:
        if pck.recepient == "0":
            await self._broadcast(pck)
            return
        target = pck.recepient
        self.__clients[target].send(pck)

    async def _broadcast(self, pck: Packet) -> None:
        for client in self.__clients.values():
            client.send(pck)
