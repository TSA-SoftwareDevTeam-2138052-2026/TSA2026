import sys
import os

# Needed for libraries to function
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool, QTimer, Qt
from PySide6.QtGui import QKeyEvent, QPixmap, QImage, QIcon
import pathlib # to get home
from captions import Captions
import PyVisualHelp
import keyboard # keyboard shortcuts
import pickle
from ffmpeg_manager import ffmpeg_manager

# Window Imports
import MainUI
import transcribing_file
import MagnifierUI
from Worker import Worker
import LicensesWindow
import ResetPrefDialog

is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

data_location = pathlib.Path.home().as_posix() + "/.audiovisualhelp"

if not os.path.exists(data_location):
    os.makedirs(data_location)

basedir = pathlib.Path(__file__).parent

if os.name == "nt":
    try:
        import ctypes
        app_id='org.huttoisdTSA2026.AudioVisualHelper'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    except ImportError:
        pass

class MainWindow(QtWidgets.QMainWindow, MainUI.Ui_MainWindow):
    # init
    def __init__(self) -> None:
        super().__init__()
        # initialize the libraries
        self.screenshot_util = PyVisualHelp.Screenshot(data_location)
        keyboard.add_hotkey("ctrl+\\", self.screenshot_util.contrast_screenshot, args=()) #type: ignore
        self.magnify_util = PyVisualHelp.Magnify(data_location)
        self.setupUi(self)
        # set the models
        self.model = "base" # current model to transcribe with
        self.model_index = 1
        # set button actions
        self.transcribe.clicked.connect(self.transcribe_item) # click transcribe button = transcription
        self.contrast.clicked.connect(self.screenshot_util.contrast_screenshot) # click contrast button = screenshot with contrast
        self.openMagnify.clicked.connect(self.open_magnify_dialog) # click magnify button = magnify dialog to magnify for screen
        self.threadpool = QThreadPool() # make a threadpool to run workers
        self.__setup_actions__() # setup the actions
        self.setWindowTitle("AudioVisual Helper")
        try:
            self.load_data()
        except FileNotFoundError:
            self.save_data()

    # dictionary has model key with index within a dictionary
    def save_data(self) -> None:
        self.save_dict = { 
            "model": {
                "index": self.model_index
            }
        }
        with open(data_location + "/preferences.pkl", "wb") as file:
            pickle.dump(self.save_dict, file)
            file.close()

    # self explanatory, loads data
    def load_data(self):
        self.save_dict = {}
        with open(data_location + "/preferences.pkl", "rb") as file:
            self.save_dict = pickle.load(file)
        
        # All the data to load, in dictionary sequential order.
        self.set_model(True, self.save_dict["model"]["index"])
    
    # internal delete directory function
    def __del_dir__(self, directory: str):
        for dirpath, dirnames, filenames in os.walk(directory):
            for dirname in dirnames:
                self.__del_dir__(os.path.join(dirpath, dirname))
            for name in filenames:
                os.remove(os.path.join(dirpath, name))
        os.removedirs(directory)
        
    # clears the model cache to save storage space
    def clear_model_cache(self):
        self.__del_dir__(pathlib.Path.home().as_posix() + "/.cache/whisper/")
            
        
    # If i is not equal to the index selected, deactivate it. Else, activate it.
    def set_model(self, checked, model_index: int) -> None:
        self.model_index = model_index
        for i in range(0, len(self.model_button_list)):
            if i == model_index:
                self.model_button_list[i].setChecked(True)
                self.model = self.model_map[i]
            else:
                self.model_button_list[i].setChecked(False)
        self.save_data()
    
    # confirm the user wants to reset data; don't wanna accidentally delete anything
    def reset_data_conf(self):
        self.confirm_dialog = ResetPref()
        self.confirm_dialog.buttonBox.accepted.connect(self.reset_data)
        self.confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.destroy)
        self.confirm_dialog.exec()
        
    # messy but works
    def reset_data(self):
        try:
            os.remove(data_location + "/preferences.pkl")
            self.timer = QTimer()
            self.timer.setInterval(5000)
            self.timer.timeout.connect(sys.exit)
            self.reset_dialog = QtWidgets.QDialog()
            self.reset_label = QtWidgets.QLabel()
            self.reset_label.setText("Data deleted. App will close in 5 seconds.")
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.reset_label)
            self.reset_dialog.setLayout(layout)
            self.confirm_dialog.buttonBox.setEnabled(False)
            self.timer.setSingleShot(True)
            self.reset_dialog.setWindowTitle("Reset Preferences")
            self.timer.start()
            self.reset_dialog.exec()
        except:
            return False
    # setup the actions
    def __setup_actions__(self) -> None:
        self.model_button_list = [self.action_set_tiny, self.action_set_base, self.action_set_small, self.action_set_medium, self.action_set_large, self.action_set_turbo] # map the actions to call them from i
        self.model_map = ["tiny", "base", "small", "medium", "large", "turbo"] # the mappings
        
        # Below are all the buttons being mapped
        self.action_set_tiny.triggered.connect(lambda triggered: self.set_model(triggered, 0))
        self.action_set_small.triggered.connect(lambda triggered: self.set_model(triggered, 2))
        self.action_set_base.triggered.connect(lambda triggered: self.set_model(triggered, 1))
        self.action_set_medium.triggered.connect(lambda triggered: self.set_model(triggered, 3))
        self.action_set_large.triggered.connect(lambda triggered: self.set_model(triggered, 4))
        self.action_set_turbo.triggered.connect(lambda triggered: self.set_model(triggered, 5))
        
        # Set the Help menu actions
        self.actionLicenses.triggered.connect(self.open_licenses)
        
        # Set other option actions
        self.actionReset_Preferences.triggered.connect(self.reset_data_conf)
        self.actionClear_Whisper_Model_Cache.triggered.connect(self.clear_model_cache)
    
    def open_licenses(self) -> None:
        self.credits = LicensesDialog()
        self.credits.exec()
        
    # transcribe the file
    def transcribe_item(self) -> None:
        # Make a file dialog to select the file
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(file_dialog.FileMode.ExistingFile)
        file_name = ""
        if pathlib.Path(pathlib.Path.home().as_posix() + "/Videos").exists():
            file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home().as_posix() + "/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))[0]
        elif pathlib.Path(pathlib.Path.home().as_posix() + "/OneDrive/Videos").exists(): # move to onedrive in case that is preventing videos from working
            file_name = file_dialog.getOpenFileName(self, self.tr("Open Video"), pathlib.Path.home().as_posix() + "/OneDrive/Videos", self.tr("Video files (*.mp4 *.webm *.mpg *.ogg *.avi *.mov *.flv)"))[0]

        
        # Show a dialog to start it
        self.transcribing = TranscribingDialog()
        worker = Worker(self.check_for_transcribe, file_name, self.model)
        
        # Show a dialog to start it
        self.threadpool.start(worker)
        self.transcribing.exec()

    def check_for_transcribe(self, file_name, model_name) -> None:
        try:
            self.transcribe_util
        except AttributeError: #attribute as opposed to name since it is an attribute
            self.transcribing.transcription_text.setText("Importing whisper...")
            from PyAudioTranscript import PyAudioTranscript
            self.transcribe_util = PyAudioTranscript()
        if file_name != "":
            worker = Worker(self.caption_file, file_name, model_name)
            self.transcribing.transcription_text.setText(f"Transcribing \"{file_name.split("/")[-1]}\"...")
            worker.signals.finished.connect(self.show_done_transcript)
            self.threadpool.start(worker)
        elif file_name == "":
            worker = Worker(self.wait_for_error)
            self.transcribing.transcription_text.setText(f"No video selected")
            worker.signals.finished.connect(self.destroy_transcribing)
            self.threadpool.start(worker)
    
    def wait_for_error(self):
        try:
            self.time_mod.sleep(0)
        except:
            import time
            self.time_mod = time
        self.time_mod.sleep(1)

    def caption_file(self, file_name, model_name) -> bool:
        ffmpeg_manager.download_ffmpeg()
        # Turn the file into a transcript
        temp: str = self.transcribe_util.turn_into_transcript(file_name, model_name)
        
        # get the base name
        file_split = file_name.split(".")
        file_split.pop(-1)
        
        # Save the captions to a vtt
        with open(".".join(file_split) + ".vtt", "w") as file:
            try:
                file.write(Captions.convert_temp_to_captions(temp, "vtt"))
            except Exception as e:
                print("ERROR")
                print(e)
            file.close()
        return True
    
    # Show the done dialog then close after 2 seconds.
    def show_done_transcript(self) -> None:
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
    def destroy_transcribing(self) -> None:
        self.transcribing.destroy()
        try:
            self.timer.timeout.disconnect(self.destroy_transcribing)
            del self.timer
        except:
            pass
        
    def open_magnify_dialog(self) -> None:
        self.magnify_dialog = MagnifyDialog()
        self.magnify_dialog.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.magnify_dialog.buttonBox.buttons()[0].pressed.connect(self.magnify_dialog.destroy)
        self.magnify_dialog.magnify.clicked.connect(self.wait_for_magnify)
        self.magnify_dialog.show()
        
    def wait_for_magnify(self) -> None:
        self.window_open = True
        self.magnify_dialog.magnify.clicked.disconnect(self.wait_for_magnify)
        self.magnify_dialog.destroy()
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.magnify)
        self.timer.setSingleShot(True)
        self.timer.start()
    
    def magnify(self) -> None:
        del self.magnify_dialog
        self.magnify_util.take_screenshot()
        self.magnify_window = MagnifyWin(data_location + "screenshot.png", self)
        self.magnify_window.showFullScreen()
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if getattr(self, "magnify_window", False):
            self.magnify_window.destroy()
            del self.magnify_window
        return super().keyPressEvent(event)

# The transcribing dialog. Opens from the QT Designer file.
class TranscribingDialog(transcribing_file.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Transcription")

# The magnifier window.
class MagnifyDialog(MagnifierUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Magnification")

# The licenses window.
class LicensesDialog(LicensesWindow.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        if is_pyinstaller:
            with open(basedir.as_posix() + "./licenses.md", "r", encoding='utf-8') as file:
                self.label.setText(file.read())
                file.close()
        else:
            with open(basedir.parent.as_posix() + "/licenses.md", 'r', encoding='utf-8') as file:
                self.label.setText(file.read())
                file.close()
        self.label.setWordWrap(True)
        self.scrollArea.setWidgetResizable(True)
        self.label.setOpenExternalLinks(True)
        self.setWindowTitle("Licenses")

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
    def __init__(self, image, window_instance: MainWindow) -> None:
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if is_pyinstaller:
        app.setWindowIcon(QIcon(os.path.join(basedir, 'icon', 'icon.ico')))
    else:
        app.setWindowIcon(QIcon(os.path.join(basedir.parent, 'icon', 'icon.ico')))
    app.exec()