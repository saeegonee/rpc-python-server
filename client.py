from websockets import ServerConnection
from packet import Packet
from stuff.permissions import *


class Client(object):
    def __init__(self, idx: int, wsocket: ServerConnection) -> None:
        self.__id: int = idx
        self.__socket: ServerConnection = wsocket
        self.__permission: list = common_permissions()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def permission(self) -> list:
        return self.__permission

    def send(self, pck: Packet) -> None:
        """ Send message to client."""
        msg = str(pck)
        self.__socket.send(msg)

    def disconnect(self) -> None:
        """ Force disconnect from server. """
