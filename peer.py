# from websockets import ServerConnection
# from packet import Packet
# from permissions import Permission
#
#
# permission = Permission()
#
#
# class Peer(object):
#     def __init__(self, websocket: ServerConnection, idx: int) -> None:
#         self.__websocket = websocket
#         self.__id: int = idx
#         self.__permission: list = permission.common()
#
#     @property
#     def id(self) -> int:
#         return self.__id
#
#     @property
#     def permission(self) -> list:
#         return self.__permission
#
#     async def send(self, packet: Packet) -> None:
#         await self.__websocket.send(str(packet))
