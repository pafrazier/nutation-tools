import widgets
import constants as c
import PySide6.QtWidgets as psw
import PySide6.QtCore as psc

# --------------------------------------------------------------------

class ControlPanel:
    
    
    def __init__(self) -> None:
        
        self.browse = widgets.Button('Browse')
        self.record = widgets.Button('Record')
        self.edit   = widgets.Button('Edit')
        self.save   = widgets.Button('Save')
                
        self.box = psw.QVBoxLayout()
        self.box.addWidget(self.browse)
        self.box.addWidget(self.record)
        self.box.addWidget(self.edit)
        self.box.addWidget(self.save)
        self.box.setAlignment(psc.Qt.AlignTop)

# --------------------------------------------------------------------

class NavigationPanel:


    def __init__(self) -> None:

        self.img = widgets.Image()
        btn_sz = (
            c.SZ_NAV_W,
            self.img.pmap.height())
        
        self.prev = widgets.Button(
            c.LBL_PREV, btn_sz, btn_sz
        )
        
        self.next = widgets.Button(
            c.LBL_NEXT, btn_sz, btn_sz
            
        )

        self.box = psw.QHBoxLayout()
        self.box.addWidget(self.prev)
        self.box.addWidget(self.img)
        self.box.addWidget(self.next)
        self.box.setAlignment(psc.Qt.AlignCenter)

# --------------------------------------------------------------------

class InfoPanel:

    
    def __init__(self) -> None:
        self.file = widgets.InfoLabel('File')
        self.name = widgets.InfoLabel('')
        self.nmbr = widgets.InfoLabel('')
        self.crsr = widgets.InfoLabel('Cursor')
        self.pxlx = widgets.InfoLabel('')
        self.pxly = widgets.InfoLabel('')
        self.size = widgets.InfoLabel('Size')
        self.wdth = widgets.InfoLabel('')
        self.hght = widgets.InfoLabel('')

        self.box = psw.QVBoxLayout()
        self.box.addWidget(self.file)
        self.box.addWidget(self.name)
        self.box.addWidget(self.nmbr)
        self.box.addWidget(self.crsr)
        self.box.addWidget(self.pxlx)
        self.box.addWidget(self.pxly)
        self.box.addWidget(self.size)
        self.box.addWidget(self.wdth)
        self.box.addWidget(self.hght)
        self.box.setAlignment(psc.Qt.AlignTop)