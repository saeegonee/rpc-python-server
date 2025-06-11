import sys
import constants
sys.path.append(constants.PROJECT_PATH)

from packet import Packet
from peer_server import PeerServer
from options import Option
from websockets import ServerConnection


broadcast = {}
pserv = PeerServer(broadcast)
opt = Option()


def test_rserv_method() -> None:
    wsocket = ServerConnection(None, None)
    st = f'[0, "auth", {opt.token()}]'
    st_bad = '[0, "auth", "kektoken"]'
    pck = Packet(st)
    pck_bad = Packet(st_bad)

    assert pserv.auth(wsocket, pck)
    assert not pserv.auth(wsocket, pck_bad)
