import sys
sys.path.append("D:/_Others/rpc-python-server")

from peer import Peer
from permissions import Permission


def test_peer() -> None:

    permission = Permission()
    socket = ""
    idx = 2

    peer = Peer(socket, idx)
    
    assert peer.id == 2
    assert peer.permission == permission.common()
