from PyQt6 import QtWidgets
import sys

class ZoomWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Magnifying Glass")
        text = QtWidgets.QPushButton("Press Me!")
        

def display_gui():
    app = QtWidgets.QApplication([sys.argv])
    
    window = ZoomWindow()
    window.show()
    
    app.exec()