import sys
import constants
sys.path.append(constants.PROJECT_PATH)

from packet import Packet


def test_packet_dummy() -> None:
    msg = ''
    pck = Packet(msg)

    assert isinstance(pck, Packet)

def test_packet_convert() -> None:
    msg = '[0, "auth", "token"]'
    pck = Packet(msg)

    assert str(pck) == msg

def test_packet_func() -> None:
    msg = '[0, "auth"]'
    pck = Packet(msg)
    
    assert isinstance(pck.recepient, int)
    assert isinstance(pck.action, str)
    assert pck.recepient == 0
    assert pck.action == "auth"

def test_packet_payload() -> None:
    msg = '[0, "func", 1, "kek"]'
    pck = Packet(msg)

    assert pck.payload == [1, 'kek']
