from pathlib import Path
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow
from PySide6.QtCore import Qt
import layouts as lay
import sys

# ------------------------------------------------------------- Widget
class MainWidget(QWidget):
# --------------------------------------------------------------------

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
       
        self.setWindowTitle('Nutation Marker')
        self.setLayout(lay.NutationMarkerLayout())

# ------------------------------------------------------------- Widget
class MainWindow(QMainWindow):
# --------------------------------------------------------------------

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.setCentralWidget(MainWidget())

# --------------------------------------------------------------- Main
def main():
# --------------------------------------------------------------------

    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()