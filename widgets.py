import PySide6.QtWidgets as psw
import PySide6.QtGui as psg
import constants as con

# --------------------------------------------------------------------

class Button(psw.QToolButton):
    
    
    def __init__( 
            self, 
            text: str = '',
            size: tuple = con.SZ_BTN,
            toggle: bool = 0, 
            *args, **kw
        ):
        super().__init__(*args, **kw)
        
        self.setText(text)
        self.setFixedSize(*size)
        self.isCheckable() if toggle else None

# --------------------------------------------------------------------

class Image(psw.QLabel):


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
       
        self.pmap = psg.QPixmap('0.jpg')
        self.setPixmap(self.pmap)

# --------------------------------------------------------------------

class InfoLabel(psw.QLabel):


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.setMinimumWidth(con.SZ_BTN[0])



