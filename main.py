import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QBoxLayout, QToolButton
from PySide6.QtGui import QMouseEvent, QPixmap, QKeyEvent
from PySide6.QtCore import Qt
from glob import glob
from pathlib import Path
from collections import deque

class MainWidget(QWidget):
    
    
    def __init__(self):
        super().__init__()
        
        # CONTROL PANEL
        # Browse Button # get files
        # Record Button
        # Edit Button
        # Save Button
        # File List

        # IMAGE DISPLAY
        img_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        #  Prev Button
        prev_btn = QToolButton(self)
        img_layout.addWidget(prev_btn)
        #prev_btn.clicked.connect(self.backward)
        #  Image
        #   files
        self.files = glob(f'{Path().cwd()}/*.jpg')
        self.files.sort()
        self.deq = deque(self.files)
        #   img
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap(self.deq.popleft()))
        img_layout.addWidget(self.lbl)
        #  Next Button
        next_btn = QToolButton(self)
        img_layout.addWidget(next_btn)
        #prev_btn.clicked.connect(self.forward)

        # INFO PANEL
        #  Image:
        
        #   file name
        #   out of
        #  Cursor:
        #   x
        #   y
        #  Size:
        #   width
        #   height

        
        
        

        box = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        box.addLayout(img_layout)
        
        self.setLayout(box)

    def forward(self):
        try:
            self.lbl.setPixmap(QPixmap(self.deq.popleft()))
        except:
            self.deq = deque(self.files)
            self.lbl.setPixmap(QPixmap(self.deq.popleft()))
    def backward(self):
        try:
            self.lbl.setPixmap(QPixmap(self.deq.pop()))
        except:
            self.deq = deque(self.files)
            self.lbl.setPixmap(QPixmap(self.deq.pop()))        

    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.forward()
        return super(QLabel, self.lbl).mousePressEvent(event)  
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Right:
            self.forward()
        elif event.key() == Qt.Key.Key_Left:
            self.backward()
        else: 
            pass

   
app = QApplication(sys.argv)

widget = MainWidget()
widget.show()

app.exec()