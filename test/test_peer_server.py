import sys
import constants
sys.path.append(constants.PROJECT_PATH)

from peer_server import PeerServer
from options import Option


broadcast = set()
pserv = PeerServer(broadcast)
opt = Option()


def test_rserv_method() -> None:
    token = opt.token()
    bad_token = "kektoken"

    assert pserv.auth(token)
    assert not pserv.auth(bad_token)
