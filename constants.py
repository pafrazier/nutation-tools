import data as dat

def _rgb2hex(col: tuple = (int,int,int)): 
    return '#%02x%02x%02x'%col
# --------------------------------------------------------------------

# ------------------------------------------------------------ Colours
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

THEME_COLOURS = {
    'background': _rgb2hex(COL_FRAME),
    'primary':    _rgb2hex(COL_LBL),
    'foreground': _rgb2hex(COL_LBL),
    'border':     _rgb2hex(COL_BDR),
    'primary>button.hoverBackground':  _rgb2hex(COL_HVR),
    'primary>button.activeBackground': _rgb2hex(COL_BTN_DN),
}
# --------------------------------------------------------------------

# -------------------------------------------------------------- Sizes 
SZ_BTN: tuple     = (90,33)
SZ_NAV_W: int     = 33
SZ_HVR: int       = 1 
SZ_SPACER_BG: int = 22
SZ_SPACER_SM: int = 3
# --------------------------------------------------------------------

# ------------------------------------------------------------- Labels
LBL_MIN: str      = 'ー'
LBL_MAX: str      = '🡥' 
LBL_UNMAX: str    = '🡧' 
LBL_CLS: str      = '⤫' 
LBL_PREV: str     = '⮜'
LBL_NEXT: str     = '⮞'
# --------------------------------------------------------------------

# --------------------------------------------------------- Parameters
PARAMS_TOOLS = [
    dat.Btn_Dc('browse', 'Browse', SZ_BTN, 0),
    dat.Btn_Dc('record', 'Record', SZ_BTN, 1),
    dat.Btn_Dc('edit', 'Edit', SZ_BTN, 1),
    dat.Btn_Dc('save', 'Save', SZ_BTN, 0),
]
# --------------------------------------------------------------------