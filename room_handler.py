class RoomHandlerCommon(object):
    def auth(self, token: str) -> bool:
        return True

    def msg(self, txt: str) -> bool:
        return True
