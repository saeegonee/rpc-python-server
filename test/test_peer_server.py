import sys
sys.path.append("D:/_Others/rpc-python-server")

from peer_server import PeerServer
from options import Option


pserv = PeerServer()
opt = Option()


def test_rserv_method() -> None:
    token = opt.token()
    bad_token = "kektoken"

    assert pserv.auth(token)
    assert not pserv.auth(bad_token)
