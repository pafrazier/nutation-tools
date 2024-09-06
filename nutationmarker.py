from pathlib import Path
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import Qt
import _layouts as lay
import _data as dat
import sys


# --------------------------------------------------------------------
class MainWidget(QWidget):


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setWindowTitle('Nutation Marker')
        self.filepaths = []
        # ------------------------------------------------------------
        self.tool_panel = lay.ToolPanel()
        hbox = QHBoxLayout()
        hbox.addSpacing(dat.SIZE.MID)
        hbox.addLayout(self.tool_panel)
        hbox.addSpacing(dat.SIZE.MID)
        self.tool_panel.brws.clicked.connect(self.on_brws)
        self.tool_panel.rcrd.clicked.connect(self.on_rcrd)
        self.tool_panel.edit.clicked.connect(self.on_edit)
        self.tool_panel.save.clicked.connect(self.on_save)
        # ------------------------------------------------------------
        self.image_viewer = lay.ImageViewer()
        vbox = QVBoxLayout()
        vbox.addSpacing(dat.SIZE.BIG)
        vbox.addLayout(self.image_viewer)
        vbox.addSpacing(dat.SIZE.BIG)
        hbox.addLayout(vbox)
        # ------------------------------------------------------------
        self.info_panel = lay.InfoPanel()
        hbox.addSpacing(dat.SIZE.MID)
        hbox.addLayout(self.info_panel)
        hbox.addSpacing(dat.SIZE.MID)
        self.setLayout(hbox)
    # ----------------------------------------------------------------
    def on_brws(self, e):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dlg.setLabelText(QFileDialog.DialogLabel.FileName,'Select Image Files')
        dlg.setNameFilter('Images (*.png *.jpg)')
        dlg.setViewMode(QFileDialog.ViewMode.List)
        if dlg.exec():
            files = dlg.selectedFiles()
            if files:
               self.filepaths.extend(files)
               

    def on_rcrd(self, e):
        print('Record')
    
    def on_edit(self, e):
        print('Edit')
    
    def on_save(self, e):
        print('Save')

        
        


# --------------------------------------------------------------------
class MainWindow(QMainWindow):


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setCentralWidget(MainWidget())


# --------------------------------------------------------------------
def main():


    app = QApplication(sys.argv)
    app.setStyleSheet(Path('_style.qss').read_text())
    window = MainWindow()
    window.show()
    app.exec()


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()