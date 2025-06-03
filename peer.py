class Peer(object):
    def __init__(self, websocket, idx: int) -> None:
        self.__websocket = websocket
        self.__id: int = idx
        self.__permission: list = ["msg"]

    @property
    def id(self) -> int:
        return self.__id

    @property
    def permission(self) -> list:
        return self.__permission

    async def send(self) -> None:
        await self.__websocket.send("PONG")
