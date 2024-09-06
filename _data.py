from enum import Enum
from dataclasses import dataclass
from typing import NamedTuple


'''
# --------------------------------------------------------------------
def _dark(val: int = 75) -> int:
    return val

def _light(less: float=.5*_dark(), dark: int=_dark()) -> int:
    return 255 - int(less)

def _incr(scale: int=16, light: int=_light()) -> float:
    return light/scale

def _mid(times: int=1, increment: float=_incr(), dark: int=_dark()):
    return dark + times*increment


# --------------------------------------------------------------------
class COLOUR(Enum):


    FRAME = _dark(),_dark(),_dark()
    TB = _dark(),_dark(),_dark()
    BODY = FRAME
    BTN = TB
    BTN_DN = _mid(),_mid(),_dark()
    BDR = _mid(4),_mid(4),_mid(4)
    HVR = _mid(),_mid(2),_dark()
    LBL = _light(),_light(),_light()
'''


# --------------------------------------------------------------------
@dataclass
class SIZE:


    W: int = 90
    H: int = 33
    BIG: int = 20
    MID: int = 10
    SML: int = 5


# --------------------------------------------------------------------
class Datum(NamedTuple):
    name: str
    width: int
    height: int
    x: int
    y: int