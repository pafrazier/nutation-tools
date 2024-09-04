from dataclasses import dataclass,field,fields,astuple
from pathlib import Path

# --------------------------------------------------------------------
@dataclass
class Image_Dc:
# --------------------------------------------------------------------

    name: Path
    width: int
    height: int
    x: int
    y: int

# --------------------------------------------------------------------
@dataclass
class Files_Dc:
# --------------------------------------------------------------------

    path:  Path = Path().cwd()
    files: list[Path] = field(default_factory=list)
 
# --------------------------------------------------------------------
@dataclass
class Local_Dc:
# --------------------------------------------------------------------

    browse: bool = False
    record: bool = False
    edit: bool = False
    save: bool = False
    prev: bool = False
    next: bool = False

# --------------------------------------------------------------------
@dataclass
class Global_Dc:
# --------------------------------------------------------------------

    view: Local_Dc = Local_Dc()
    user: Local_Dc = Local_Dc()

    def get_tasks(self) -> tuple:
        flds = [i.default for i in fields(self)]
        tpls = [astuple(i) for i in flds]
        zp   = zip(*tpls)
        return tuple(i!=j for i,j in zp)

# --------------------------------------------------------------------
@dataclass
class Task_Dc:
# --------------------------------------------------------------------
    
    browse: bool
    record: bool
    edit: bool
    save: bool
    prev: bool
    next: bool

# --------------------------------------------------------------------
@dataclass
class Btn_Dc:
# --------------------------------------------------------------------

    name: str
    label: str
    size: tuple
    toggle: bool