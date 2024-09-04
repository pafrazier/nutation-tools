from PySide6.QtWidgets import QFileDialog

import data as dat
import widgets as wid
import constants as con
import functions as fun

# ----------------------------------------------------------- Handlers
def on_browse():
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.FileMode.ExistingFiles)
    dlg.setLabelText(QFileDialog.DialogLabel.FileName,'Select Image Files')
    dlg.setNameFilter("Images (*.png *.jpg)")
    dlg.setViewMode(QFileDialog.ViewMode.List)
    if dlg.exec():
        files = dlg.selectedFiles()
        if files:
            pass
# --------------------------------------------------------------------
def on_record():
    pass
# --------------------------------------------------------------------
def on_edit():
    pass
# --------------------------------------------------------------------
def on_save():
    pass
# --------------------------------------------------------------------
def on_prev():
    pass
# --------------------------------------------------------------------
def on_next():
    pass
# -------------------------------------------------- Set Btn Functions
def make_btn(obj: object, btn_dc: dat.Btn_Dc) -> None:
    _name = f'{btn_dc.name}'.lower()
    _value = wid.Button(btn_dc.label,btn_dc.size,btn_dc.toggle)
    setattr(obj,_name,_value)
# --------------------------------------------------------------------
def put_btn_in_layout(obj: object, btn_dc: dat.Btn_Dc) -> None:
    _name = f'{btn_dc.name}'.lower()
    _widget = getattr(obj,_name)
    obj.addWidget(_widget)
# --------------------------------------------------------------------
def connect_btn_to_handler(obj: object, btn_dc: dat.Btn_Dc) -> None:
    _btn_name = f'{btn_dc.name}'.lower()
    _handler_name = f'on_{btn_dc.name}'.lower()
    _handler = getattr(fun,_handler_name)
    getattr(obj,_btn_name).clicked.connect(_handler)
# --------------------------------------------------------------------
def setup_one_btn(obj: object, btn_dc = dat.Btn_Dc) -> None:
    make_btn(obj=obj,btn_dc=btn_dc)
    put_btn_in_layout(obj=obj,btn_dc=btn_dc)
    connect_btn_to_handler(obj=obj,btn_dc=btn_dc)
# --------------------------------------------------------------------
def setup_all_btn(obj: object, btn_dc_list = con.PARAMS_TOOLS) -> None:
    for btn_dc in btn_dc_list:
        setup_one_btn(obj=obj,btn_dc=btn_dc)
        obj.addSpacing(con.SZ_SPACER_SM)