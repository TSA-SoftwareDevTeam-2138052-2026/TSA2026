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
    # init
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = "base" # current model to transcribe with
        self.transcribe.clicked.connect(self.transcribe_item) # click transcribe button = transcription
        self.contrast.clicked.connect(Screenshot.take_and_show_screenshot) # click contrast button = screenshot with contrast
        self.threadpool = QThreadPool() # make a threadpool to run workers
        self.__setup_actions__() # setup the actoins
    
    # If i is not equal to the index selected, deactivate it. Else, activate it.
    def set_model(self, checked, model_index):
        for i in range(0, len(self.model_list)):
            if i == model_index:
                self.model_list[i].setChecked(True)
                self.model = self.model_map[i]
            else:
                self.model_list[i].setChecked(False)
    
    # setup the actions
    def __setup_actions__(self):
        self.model_list = [self.action_set_tiny, self.action_set_base, self.action_set_small, self.action_set_medium, self.action_set_large, self.action_set_turbo] # map the actions to call them from i
        self.model_map = ["tiny", "base", "small", "medium", "large", "turbo"] # the mappings
        
        # Below are all the buttons being mapped
        self.action_set_tiny.triggered.connect(lambda triggered: self.set_model(triggered, 0))
        self.action_set_small.triggered.connect(lambda triggered: self.set_model(triggered, 1))
        self.action_set_base.triggered.connect(lambda triggered: self.set_model(triggered, 2))
        self.action_set_medium.triggered.connect(lambda triggered: self.set_model(triggered, 3))
        self.action_set_large.triggered.connect(lambda triggered: self.set_model(triggered, 4))
        self.action_set_turbo.triggered.connect(lambda triggered: self.set_model(triggered, 5))
        
    # transcribe the file
    def transcribe_item(self):
        # Make a file dialog to select the file
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(file_dialog.FileMode.ExistingFile)
        file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home()._str + "/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))[0]
        
        # make a worker to transcribe the file and start it
        worker = Worker(self.caption_file, file_name, self.model)
        worker.signals.finished.connect(self.show_done_transcript)
        self.threadpool.start(worker)
        
        # Show a dialog to start it
        self.transcribing = TranscribingDialog()
        self.transcribing.transcription_text.setText(f"Transcribing \"{file_name.split("/")[-1]}\"...")
        self.transcribing.exec()
    
    def caption_file(self, file_name, model_name) -> bool:
        # Turn the file into a transcript
        temp: str = PyAudioTranscript.turn_into_transcript(file_name, model_name)
        
        # get the base name
        file_split = file_name.split(".")
        file_split.pop(-1)
        print(".".join(file_split))
        
        # Save the captions to a vtt
        with open(".".join(file_split) + ".vtt", "w") as file:
            try:
                file.write(Captions.convert_temp_to_captions(temp, "vtt"))
            except:
                print("ERROR")
            file.close()
        return True
    
    # Show the done dialog then close after 2 seconds.
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
    
    # Destroy the transcribing window and delete the timer.    
    def destroy_transcribing(self):
        self.transcribing.destroy()
        del self.timer

# The transcribing dialog. Opens from the QT Designer file.
class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()