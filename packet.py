import json


class Packet(object):
    def __init__(self, msg: str) -> None:
        self.__msg: str = msg
        self.recepient: int
        self.action: str
        self.payload: list
        
        if self.__msg != "":
            self._extend()

    def __str__(self) -> str:
        raw_msg = [self.recepient, self.action, *self.payload]
        return json.dumps(raw_msg)

    def __byte__(self) -> bytes:
        return str(self).encode("utf-8")

    def _extend(self) -> None:
        src = json.loads(self.__msg)
        self.recepient = src[0]
        self.action = src[1]
        self.payload = src[2:]
