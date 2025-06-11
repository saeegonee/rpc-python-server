import sys
import constants
sys.path.append(constants.PROJECT_PATH)

from packet import Packet

MSG = '[0, "auth", "token"]'
pck = Packet(MSG)
pck.extend()

def test_packet_method() -> None:
    assert str(pck) == MSG

def test_packet_content() -> None:
    assert isinstance(pck.recepient, int)
    assert isinstance(pck.action, str)
    assert isinstance(pck.payload, list)
