import logging
from options import Option


log = logging.getLogger(__name__)
opt = Option()


class PeerServer(object):
    def __init__(self, broadcast: set) -> None:
        self.__broadcast: set = broadcast

    def auth(self, token: str) -> bool:
        if token == opt.token():
            return True
        return False

    def get_idx(self) -> int:
        return len(self.__broadcast) + 2
