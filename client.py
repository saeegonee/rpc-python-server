from websockets import ServerConnection
from packet import Packet
from stuff.permissions import *


class Client(object):
    def __init__(self, idx: int, wsocket: ServerConnection) -> None:
        self.__id: int = idx
        self.__socket: ServerConnection = wsocket
        self.__permission: list = common_permissions()

    def __str__(self) -> str:
        return f"<{self.__id}>"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def permission(self) -> list:
        return self.__permission

    async def send(self, pck: Packet) -> None:
        msg = str(pck)
        await self.__socket.send(msg)

    async def id_request(self) -> None:
        pck = Packet(f'[{self.__id},"id"]')
        await self.send(pck)
