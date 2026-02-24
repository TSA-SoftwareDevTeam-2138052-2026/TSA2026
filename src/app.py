import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool, QTimer
import pathlib # to get home
from PyAudioTranscript import PyAudioTranscript
from captions import Captions
from PyVisualHelp import Screenshot

from MainUI import Ui_MainWindow
import transcribing_file
from Worker import Worker

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.transcribe.clicked.connect(self.transcribe_item)
        self.contrast.clicked.connect(Screenshot.take_and_show_screenshot)
        self.threadpool = QThreadPool()
        
    def transcribe_item(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(file_dialog.FileMode.ExistingFile)
        file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home()._str + "/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))[0]
        worker = Worker(self.caption_file, file_name, "base")
        worker.signals.finished.connect(self.show_done_transcript)
        self.threadpool.start(worker)
        self.transcribing = TranscribingDialog()
        self.transcribing.transcription_text.setText(f"Transcribing \"{file_name}\"...")
        self.transcribing.exec()
    
    def caption_file(self, file_name, model_name) -> bool:
        print("Beginning")
        temp: str = PyAudioTranscript.turn_into_transcript(file_name, model_name)
        file_split = file_name.split(".")
        file_split.pop(-1)
        print(".".join(file_split))
        with open(".".join(file_split) + ".vtt", "w") as file:
            try:
                file.write(Captions.convert_temp_to_captions(temp, "vtt"))
            except:
                print("ERROR")
            file.close()
        return True
    
    def show_done_transcript(self, s):
        print("DONE!", s)
        self.transcribing.transcription_text.setText("Done!")
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.destroy_transcribing)
        self.transcribing.progressBar.setMaximum(1)
        self.transcribing.progressBar.setMinimum(0)
        self.transcribing.progressBar.setValue(1)
        self.timer.start()
        
    def destroy_transcribing(self):
        self.transcribing.destroy()
        del self.timer
class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()