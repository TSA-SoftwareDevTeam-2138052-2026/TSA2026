import sys
import os

# Needed for libraries to function
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool, QTimer, Qt
from PySide6.QtGui import QKeyEvent, QIcon
import pathlib # to get home
from captions import Captions
import PyVisualHelp
import keyboard # keyboard shortcuts
from ffmpeg_manager import ffmpeg_manager

# Window Imports
import MainUI
from Worker import Worker
import SecondaryWindows
import DataTools
import HelpWindows

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
        keyboard.add_hotkey("ctrl+shift+enter", self.transcribe_item)
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
        self.datatools = DataTools.DataTools(basedir, data_location, self, is_pyinstaller)
        self.help_win = HelpWindows.HelpWin(self)
        self.__setup_actions__() # setup the actions
        self.setWindowTitle("AudioVisual Helper")
        try:
            self.datatools.load_data()
        except FileNotFoundError:
            self.datatools.save_data()
            
        
    # If i is not equal to the index selected, deactivate it. Else, activate it.
    def set_model(self, checked, model_index: int) -> None:
        self.model_index = model_index
        for i in range(0, len(self.model_button_list)):
            if i == model_index:
                self.model_button_list[i].setChecked(True)
                self.model = self.model_map[i]
            else:
                self.model_button_list[i].setChecked(False)
        self.datatools.save_data()
    
    # confirm the user wants to reset data; don't wanna accidentally delete anything
    def reset_data_conf(self):
        self.confirm_dialog = SecondaryWindows.ResetPref()
        self.confirm_dialog.buttonBox.accepted.connect(self.datatools.reset_data)
        self.confirm_dialog.buttonBox.rejected.connect(self.confirm_dialog.destroy)
        self.confirm_dialog.exec()
        
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
        self.actionLicenses.triggered.connect(self.help_win.open_licenses)
        self.actionCredits.triggered.connect(self.help_win.open_credits)
        self.actionShortcuts.triggered.connect(self.help_win.open_help)
        
        # Set other option actions
        self.actionReset_Preferences.triggered.connect(self.reset_data_conf)
        self.actionClear_Whisper_Model_Cache.triggered.connect(self.datatools.clear_model_cache)
        
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
        self.transcribing = SecondaryWindows.TranscribingDialog()
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
            worker.signals.finished.connect(self.transcribing.show_done_transcript)
            self.threadpool.start(worker)
        elif file_name == "":
            worker = Worker(self.wait_for_error)
            self.transcribing.transcription_text.setText("No video selected")
            worker.signals.finished.connect(self.transcribing.destroy_transcribing)
            self.threadpool.start(worker)
    
    def wait_for_error(self):
        try:
            self.time_mod.sleep(0)
        except:
            import time
            self.time_mod = time
        self.time_mod.sleep(5)

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

        
    def open_magnify_dialog(self) -> None:
        self.magnify_dialog = SecondaryWindows.MagnifyDialog()
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
        self.magnify_window = SecondaryWindows.MagnifyWin(data_location + "screenshot.png", self)
        self.magnify_window.showFullScreen()
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if getattr(self, "magnify_window", False):
            self.magnify_window.destroy()
            del self.magnify_window
        return super().keyPressEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if is_pyinstaller:
        app.setWindowIcon(QIcon(os.path.join(basedir, 'icon', 'icon.ico')))
    else:
        app.setWindowIcon(QIcon(os.path.join(basedir.parent, 'icon', 'icon.ico')))
    app.exec()