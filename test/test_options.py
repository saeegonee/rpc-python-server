import sys
import constants
sys.path.append(constants.PROJECT_PATH)


import stuff.options as opt


def test_options_type() -> None:
    assert isinstance(opt.ADDRESS, str)
    assert isinstance(opt.PORT, int)
    assert isinstance(opt.TOKEN, str)
    assert isinstance(opt.ROOM_TIMEOUT, int)

def test_options() -> None:
    assert len(opt.ADDRESS) > 0
    assert opt.PORT > 0
    assert len(opt.TOKEN) > 0
    assert opt.ROOM_TIMEOUT > 20
