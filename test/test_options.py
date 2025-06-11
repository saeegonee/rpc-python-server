import sys
import constants
sys.path.append(constants.PROJECT_PATH)


import stuff.options as opt


def test_options_type() -> None:
    assert isinstance(opt.ADDRESS, str)
    assert isinstance(opt.PORT, int)
    assert isinstance(opt.TOKEN, str)
    assert isinstance(opt.ROOM_TIMEOUT, int)

def test_options_address() -> None:
    l_addr = opt.ADDRESS.split(".")
    assert len(opt.ADDRESS) > 0
    assert len(l_addr) == 4
    for i in l_addr:
        assert isinstance(int(i), int)

def test_options_port() -> None:
    forbiden = [7, 20, 21, 22, 23, 25, 53, 69, 80, 88, 102, 110, 135, 137, 139, 143, 443, 993]
    assert opt.PORT > 0
    assert not opt.PORT in forbiden

def test_options() -> None:
    assert len(opt.TOKEN) > 0
    assert opt.ROOM_TIMEOUT > 20
