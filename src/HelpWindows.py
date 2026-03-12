from typing import TYPE_CHECKING

import SecondaryWindows

if TYPE_CHECKING:
    import main

class HelpWin:
    def __init__(self, main_win: main.MainWindow) -> None:
        self.main = main_win
        
    def open_licenses(self) -> None:
        self.licenses = SecondaryWindows.TextReadDialog("./licenses.md", self.main.datatools)
        self.licenses.setWindowTitle("Licenses")
        self.licenses.exec()
    
    def open_credits(self) -> None:
        self.credits = SecondaryWindows.TextReadDialog("./credits.md", self.main.datatools)
        self.credits.setWindowTitle("Credits")
        self.credits.exec()
    
    def open_help(self) -> None:
        self.credits = SecondaryWindows.TextReadDialog("./help.md", self.main.datatools)
        self.credits.setWindowTitle("Help")
        self.credits.exec()