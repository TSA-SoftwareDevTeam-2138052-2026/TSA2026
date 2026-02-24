import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool
from PyAudioTranscript import PyAudioTranscript
from captions import Captions
import pathlib # to get home

from MainUI import Ui_MainWindow
import transcribing_file
from Worker import Worker

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.transcribe.clicked.connect(self.transcribe_item)
        self.threadpool = QThreadPool()
        
    def transcribe_item(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(file_dialog.FileMode.ExistingFile)
        file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home()._str + "/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))
        worker = Worker(PyAudioTranscript.turn_into_transcript, file_name, "base")
        worker.signals.finished.connect(self.show_done_transcript)
        self.transcribing = TranscribingDialog()
        self.transcribing.exec()
    
    def caption_file(self, file_name):
        temp: str = PyAudioTranscript.turn_into_transcript(file_name)
        return Captions.convert_temp_to_captions(temp)
        
    
    def show_done_transcript(self, s):
        print("DONE!", s)
        self.transcribe.destroy()

class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()