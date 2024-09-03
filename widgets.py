import PySide6.QtWidgets as psw
import PySide6.QtGui as psg
import constants as c

# --------------------------------------------------------------------

class Button(psw.QPushButton):
    
    
    def __init__(
            self, text: str = '', 
            min_size: tuple = c.SZ_BTN,
            max_size: tuple = c.SZ_BTN,
        ):
        super().__init__()
        
        self.setMinimumSize(*min_size)
        self.setMaximumSize(*max_size)
        self.setText(text)

# --------------------------------------------------------------------

class Image(psw.QLabel):


    def __init__(self):
        super().__init__()
       
        self.pmap = psg.QPixmap('0.jpg')
        self.setPixmap(self.pmap)

# --------------------------------------------------------------------

class InfoLabel(psw.QLabel):


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.setMinimumWidth(c.SZ_BTN[0])

