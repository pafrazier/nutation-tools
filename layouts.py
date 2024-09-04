from dataclasses import astuple
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget
from PySide6.QtCore import Qt

import widgets   as wid
import constants as con
import data      as dat
import functions as fun

# --------------------------------------------------------------------
class ToolPanel(QVBoxLayout):
# --------------------------------------------------------------------
    
    def __init__(self, params = con.PARAMS_TOOLS, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.addSpacing(con.SZ_SPACER_BG)
        fun.setup_all_btn(self, params)
        self.setAlignment(Qt.AlignTop)
        self.addSpacing(con.SZ_SPACER_BG)

# --------------------------------------------------------------------
class ImageViewer(QHBoxLayout):
# --------------------------------------------------------------------

    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.img = wid.Image()
        btn_sz = (con.SZ_NAV_W,self.img.pmap.height())
        
        prev_param = dat.Btn_Dc('prev', con.LBL_PREV, btn_sz, 0)
        next_param = dat.Btn_Dc('next', con.LBL_NEXT, btn_sz, 0)

        fun.setup_one_btn(self,prev_param)
        self.addWidget(self.img)
        fun.setup_one_btn(self,next_param)
        
        self.setAlignment(Qt.AlignCenter)
        
# --------------------------------------------------------------------
class InfoPanel(QVBoxLayout):
# --------------------------------------------------------------------
    
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.file = wid.InfoLabel('File')
        self.name = wid.InfoLabel('')
        self.nmbr = wid.InfoLabel('')
        self.crsr = wid.InfoLabel('Cursor')
        self.pxlx = wid.InfoLabel('')
        self.pxly = wid.InfoLabel('')
        self.size = wid.InfoLabel('Size')
        self.wdth = wid.InfoLabel('')
        self.hght = wid.InfoLabel('')

        self.addSpacing(con.SZ_SPACER_BG)
        self.addWidget(self.file)
        self.addWidget(self.name)
        self.addWidget(self.nmbr)
        self.addWidget(self.crsr)
        self.addWidget(self.pxlx)
        self.addWidget(self.pxly)
        self.addWidget(self.size)
        self.addWidget(self.wdth)
        self.addWidget(self.hght)
        self.addSpacing(con.SZ_SPACER_BG)
        self.setAlignment(Qt.AlignTop)

# --------------------------------------------------------------------
class NutationMarkerLayout(QHBoxLayout):
# --------------------------------------------------------------------

    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        vbox = QVBoxLayout()
        vbox.addSpacing(con.SZ_SPACER_BG)
        vbox.addLayout(ImageViewer())
        vbox.addSpacing(con.SZ_SPACER_BG)

        self.addSpacing(con.SZ_SPACER_SM)
        self.addLayout(ToolPanel())
        self.addSpacing(con.SZ_SPACER_SM)
        self.addLayout(vbox)
        self.addSpacing(con.SZ_SPACER_SM)
        self.addLayout(InfoPanel())
        self.addSpacing(con.SZ_SPACER_SM)