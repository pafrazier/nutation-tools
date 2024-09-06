from PySide6.QtWidgets import(
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QToolButton,
    QLabel,
    QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QFont
from glob import glob
from pathlib import Path
from collections import deque

import _data as dat


# --------------------------------------------------------- Tool Panel
class ToolPanel(QVBoxLayout):

    
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)
        # ----------------------------------------------------- Browse
        self.brws = QToolButton()
        self.brws.setText('Browse')
        self.brws.setFixedSize(dat.SIZE.W,dat.SIZE.H)
        # ----------------------------------------------------- Record
        self.rcrd = QToolButton()
        self.rcrd.setText('Record')
        self.rcrd.setFixedSize(dat.SIZE.W,dat.SIZE.H)
        # ------------------------------------------------------- Edit
        self.edit = QToolButton()
        self.edit.setText('Edit')
        self.edit.setFixedSize(dat.SIZE.W,dat.SIZE.H)
        # ------------------------------------------------------- Save
        self.save = QToolButton()
        self.save.setText('Save')
        self.save.setFixedSize(dat.SIZE.W,dat.SIZE.H)
        # ----------------------------------------------------- Layout
        self.addSpacing(dat.SIZE.BIG)
        self.addWidget(self.brws)
        self.addWidget(self.rcrd)
        self.addWidget(self.edit)
        self.addWidget(self.save)
        self.addSpacing(dat.SIZE.BIG)
        self.setAlignment(Qt.AlignTop)


# -------------------------------------------------------------- Image
class Image(QLabel):
    
    
    # ----------------------------------------------------------------
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)
        # ------------------------------------------------------------
        self.pmp = QPixmap(1000,500)
        self.setPixmap(self.pmp)
    # ----------------------------------------------------------------
    def mousePressEvent(self, event: QMouseEvent) -> None:
        print('CLICKED')
        return super().mousePressEvent(event)        


# ------------------------------------------------------- Image Viewer
class ImageViewer(QHBoxLayout):

    
    # ----------------------------------------------------------------
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)
        # ------------------------------------------------------------
        self.img = Image()
        self.btn_sz = (
            dat.SIZE.H,
            self.img.pmp.height()
        )
        # ------------------------------------------------------------
        self.prev = QToolButton()
        self.prev.setText('⮜')
        self.prev.setFixedSize(*self.btn_sz)
        # ------------------------------------------------------------
        self.next = QToolButton()
        self.next.setText('⮞')
        self.next.setFixedSize(*self.btn_sz)
        # ------------------------------------------------------------
        self.addWidget(self.prev)
        self.addWidget(self.img)
        self.addWidget(self.next)
        self.setAlignment(Qt.AlignCenter)


# --------------------------------------------------------- Info Panel
class InfoPanel(QVBoxLayout):


    # ----------------------------------------------------------------
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)
        # ------------------------------------------------------------
        bold_font = QFont()
        bold_font.setBold(True)
        # ------------------------------------------------------------
        self.file = QLabel()
        self.file.setText('File')
        self.file.setFont(bold_font)
        self.file.setFixedWidth(dat.SIZE.W)
        self.file_info = QLabel()
        self.file_info.setText(f'name.ext\nx out of y')
        # ------------------------------------------------------------
        self.crsr = QLabel()
        self.crsr.setText('Cursor')
        self.crsr.setFont(bold_font)
        self.crsr_info = QLabel()
        self.crsr_info.setText(f'x: 0\ny: 0')
        # ------------------------------------------------------------
        self.size = QLabel()
        self.size.setText('Size')
        self.size.setFont(bold_font)
        self.size_info = QLabel()
        self.size_info.setText(f'width: 0\nheight: 0')
        # ------------------------------------------------------------
        self.addSpacing(dat.SIZE.BIG)
        self.addWidget(self.file)
        self.addWidget(self.file_info)
        self.addSpacing(dat.SIZE.MID)
        self.addWidget(self.crsr)
        self.addWidget(self.crsr_info)
        self.addSpacing(dat.SIZE.MID)
        self.addWidget(self.size)
        self.addWidget(self.size_info)
        self.addSpacing(dat.SIZE.BIG)
        self.setAlignment(Qt.AlignTop)