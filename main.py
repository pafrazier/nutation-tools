from pathlib import Path
import PySide6.QtWidgets as psw
import PySide6.QtCore as psc
import constants as c
import sys
import widgets
import ui
import qdarktheme


# --------------------------------------------------------------------

class MainWidget(psw.QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QGridLayout Demo")
        
        control = ui.ControlPanel()
        navigation = ui.NavigationPanel()
        information = ui.InfoPanel()

        box = psw.QHBoxLayout()
        box.addLayout(control.box)
        box.addLayout(navigation.box)
        box.addLayout(information.box)
        box.setAlignment(psc.Qt.AlignCenter)
                
        self.setLayout(box)

# --------------------------------------------------------------------

class MainWindow(psw.QMainWindow):
    
    
    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainWidget())
        
# --------------------------------------------------------------------

if __name__ == '__main__':


    qdarktheme.enable_hi_dpi()
    app = psw.QApplication(sys.argv)
    qdarktheme.setup_theme(custom_colors=c.THEME_COLOURS)
    window = MainWindow()
    window.show()
    app.exec()

    