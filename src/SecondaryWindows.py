import transcribing_file
import MagnifierUI
import LicensesWindow
import ResetPrefDialog

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QKeyEvent, QPixmap, QImage
import main

import sys
import os
import pathlib

import DataTools

# Needed for libraries to function
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

basedir = pathlib.Path(__file__).parent

class DataToolsSuper:
    def __init__(self):
        self.datatools = DataTools.DataTools(main.basedir, main.data_location, main.MainWindow(), main.is_pyinstaller)

# The transcribing dialog. Opens from the QT Designer file.
class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog, DataToolsSuper):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Transcription")

# The magnifier window.
class MagnifyDialog(MagnifierUI.Ui_MainWindow, QtWidgets.QMainWindow, DataToolsSuper):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Magnification")

# The licenses window.
class TextReadDialog(LicensesWindow.Ui_Dialog, QtWidgets.QDialog, DataToolsSuper):
    def __init__(self, file_to_read) -> None:
        super().__init__()
        self.setupUi(self)
        self.label.setText(self.datatools.load_file_from_self(file_to_read, False))
        self.label.setWordWrap(True)
        self.scrollArea.setWidgetResizable(True)
        self.label.setOpenExternalLinks(True)

class ResetPref(QtWidgets.QDialog, ResetPrefDialog.Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Reset Preferences")

# The actual image display for zooming
class ImageDialog(QtWidgets.QGraphicsView):
    def __init__(self, image) -> None:
        super().__init__()
        self.graph_scene = QtWidgets.QGraphicsScene()
        self.image = QtWidgets.QGraphicsPixmapItem()
        self.image.setPixmap(QPixmap.fromImage(QImage(image)))
        self.graph_scene.addItem(self.image)
        self.setScene(self.graph_scene)

# The magnifier window that holds ImageDialog
class MagnifyWin(QtWidgets.QMainWindow):
    def __init__(self, image, window_instance: "main.MainWindow") -> None:
        super().__init__()
        self.gv = ImageDialog(image)
        self.setCentralWidget(self.gv)
        self.timer = QTimer()
        self.timer.setInterval(25)
        self.timer.timeout.connect(self.pre_load)
        self.timer.start()
        self.gv.setTransformationAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.gv.setResizeAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.gv.scale(1.5,1.5)
        self.setStyleSheet("border: none;")
        self.gv.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gv.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.main_win = window_instance
        
    def pre_load(self) -> None:
        self.gv.fitInView(self.gv.image, Qt.AspectRatioMode.KeepAspectRatio)
        self.gv.scale(1.5,1.5)


    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.destroy()
        self.timer.stop()
        self.main_win.open_magnify_dialog()