# -------------------------------- Colours

_dark = 75
_lite = int(255 - _dark/2)
_incr = int(_lite/16)
_mid1 = _dark + _incr
_mid2 = _dark + _incr*2
_mid3 = _dark + _incr*3
_mid4 = _dark + _incr*4
_mid5 = _dark + _incr*5
_mid6 = _dark + _incr*6
_mid7 = _dark + _incr*7

COL_FRAME: tuple  = (_dark,_dark,_dark)
COL_TB: tuple     = (_dark,_dark,_dark)
COL_BODY: tuple   = COL_FRAME
COL_BTN: tuple    = COL_TB
COL_BTN_DN: tuple = (_mid1,_mid1,_dark)
COL_BDR: tuple    = (_mid4,_mid4,_mid4)
COL_HVR: tuple    = (_mid1,_mid2,_dark)
COL_LBL: tuple    = (_lite,_lite,_lite)

def rgb2hex(col: tuple): 
    return '#%02x%02x%02x'%col

THEME_COLOURS = {
    'background': rgb2hex(COL_FRAME),
    'primary':    rgb2hex(COL_LBL),
    'foreground': rgb2hex(COL_LBL),
    'border':     rgb2hex(COL_BDR),
    'primary>button.hoverBackground':  rgb2hex(COL_HVR),
    'primary>button.activeBackground': rgb2hex(COL_BTN_DN),
}

# -------------------------------- Sizes 

SZ_BTN: tuple     = (90,33)
SZ_NAV_W: int     = 33
SZ_HVR: int       = 1 
SZ_SPACER_BG: int = 22
SZ_SPACER_SM: int = 3

# -------------------------------- Labels

LBL_MIN: str      = 'ー'                # Minimise
LBL_MAX: str      = '🡥'                # Maximise 
LBL_UNMAX: str    = '🡧'                # Unmaximise 
LBL_CLS: str      = '⤫'                # Close 
LBL_PREV: str     = '⮜'                # Minimise
LBL_NEXT: str     = '⮞'                # Minimise