import pathlib
import os
import main
import pickle
import sys

class DataTools:
    def __init__(self, basedir, datadir, mainwindow: "main.MainWindow") -> None:
        self.basedir = basedir
        self.datadir = datadir
        self.main = mainwindow
    
    # dictionary has model key with index within a dictionary
    def save_data(self) -> None:
        self.save_dict = { 
            "model": {
                "index": self.main.model_index
            }
        }
        with open(self.datadir + "/preferences.pkl", "wb") as file:
            pickle.dump(self.save_dict, file)
            file.close()

    # self explanatory, loads data
    def load_data(self):
        self.save_dict = {}
        with open(self.datadir + "/preferences.pkl", "rb") as file:
            self.save_dict = pickle.load(file)
        
        # All the data to load, in dictionary sequential order.
        self.main.set_model(True, self.save_dict["model"]["index"])
    
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
    
    # messy but works
    def reset_data(self):
        try:
            os.remove(self.datadir + "/preferences.pkl")
            self.timer = main.QTimer()
            self.timer.setInterval(5000)
            self.timer.timeout.connect(sys.exit)
            self.reset_dialog = main.QtWidgets.QDialog()
            self.reset_label = main.QtWidgets.QLabel()
            self.reset_label.setText("Data deleted. App will close in 5 seconds.")
            layout = main.QtWidgets.QVBoxLayout()
            layout.addWidget(self.reset_label)
            self.reset_dialog.setLayout(layout)
            self.main.confirm_dialog.buttonBox.setEnabled(False)
            self.timer.setSingleShot(True)
            self.reset_dialog.setWindowTitle("Reset Preferences")
            self.timer.start()
            self.reset_dialog.exec()
        except:
            return False
    
    def load_file_from_self(self, filename: str):
        pathlib.Path