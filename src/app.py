import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool, QTimer
from PySide6.QtGui import QPixmap, QImage, QWindow, QTransform
import pathlib # to get home
from captions import Captions
import PyVisualHelp
import keyboard # keyboard shortcuts
import MainUI
import transcribing_file
import MagnifierUI
from Worker import Worker
import os

data_location = pathlib.Path.home()._str.replace("\\","/") + "/.audiovisualhelp/"

if not os.path.exists(data_location):
    os.makedirs(data_location)

class MainWindow(QtWidgets.QMainWindow, MainUI.Ui_MainWindow):
    # init
    def __init__(self):
        super().__init__()
        self.screenshot_util = PyVisualHelp.Screenshot(data_location)
        keyboard.add_hotkey("ctrl+\\", self.screenshot_util.contrast_screenshot, args=()) #type: ignore
        self.magnify_util = PyVisualHelp.Magnify(data_location)
        self.setupUi(self)
        self.model = "base" # current model to transcribe with
        self.transcribe.clicked.connect(self.transcribe_item) # click transcribe button = transcription
        self.contrast.clicked.connect(self.screenshot_util.contrast_screenshot) # click contrast button = screenshot with contrast
        self.openMagnify.clicked.connect(self.open_magnify_dialog)
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
        self.action_set_small.triggered.connect(lambda triggered: self.set_model(triggered, 2))
        self.action_set_base.triggered.connect(lambda triggered: self.set_model(triggered, 1))
        self.action_set_medium.triggered.connect(lambda triggered: self.set_model(triggered, 3))
        self.action_set_large.triggered.connect(lambda triggered: self.set_model(triggered, 4))
        self.action_set_turbo.triggered.connect(lambda triggered: self.set_model(triggered, 5))
        
    # transcribe the file
    def transcribe_item(self):
        # Make a file dialog to select the file
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(file_dialog.FileMode.ExistingFile)
        file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home()._str + "/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))[0]
        
        # Show a dialog to start it
        self.transcribing = TranscribingDialog()
        worker = Worker(self.check_for_transcribe, file_name, self.model)
        # Show a dialog to start it
        self.transcribing.transcription_text.setText(f"Importing whisper...")
        self.threadpool.start(worker)
        self.transcribing.exec()

    def check_for_transcribe(self, file_name, model_name):
        try:
            self.transcribe_util
        except AttributeError: #attribute as opposed to name since it is an attribute
            from PyAudioTranscript import PyAudioTranscript
            self.transcribe_util = PyAudioTranscript()
        worker = Worker(self.caption_file, file_name, model_name)
        print("Worker")
        self.transcribing.transcription_text.setText(f"Transcribing \"{file_name.split("/")[-1]}\"...")
        worker.signals.finished.connect(self.show_done_transcript)
        self.threadpool.start(worker)

    
    def caption_file(self, file_name, model_name) -> bool:
        # Turn the file into a transcript
        temp: str = self.transcribe_util.turn_into_transcript(file_name, model_name)
        
        # get the base name
        file_split = file_name.split(".")
        file_split.pop(-1)
        
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
        
    def open_magnify_dialog(self):
        self.magnify_dialog = MagnifyDialog()
        self.magnify_dialog.magnify.clicked.connect(self.magnify)
        self.magnify_dialog.exec()
    
    def magnify(self):
        self.magnify_util.take_screenshot()
        magnify_window = MagnifyWin(data_location + "screenshot.png")
        print("showing full")
        print("show")

# The transcribing dialog. Opens from the QT Designer file.
class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# The magnifier window.
class MagnifyDialog(MagnifierUI.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MagnifyWin(QtWidgets.QMainWindow):
    def __init__(self, image):
        print("Init win")
        super().__init__()
        self.gv = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene()
        self.label = QtWidgets.QLabel()
        self.image = QImage(image)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.setCentralWidget(self.label)
        self.show()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()