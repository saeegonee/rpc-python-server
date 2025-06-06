import sys
import constants
sys.path.append(constants.PROJECT_PATH)

from options import Option


def test_options() -> None:
    
    opt = Option()

    assert len(opt.address()) > 0
    assert opt.port() > 0
    assert len(opt.token()) > 0

    assert isinstance(opt.address(), str)
    assert isinstance(opt.port(), int)
    assert isinstance(opt.token(), str)
