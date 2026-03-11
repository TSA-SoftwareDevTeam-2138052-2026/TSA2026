import SecondaryWindows

class HelpWin:
    def __init__(self) -> None:
        pass
        
    def open_licenses(self) -> None:
        self.licenses = SecondaryWindows.TextReadDialog("./licenses.md")
        self.licenses.setWindowTitle("Licenses")
        self.licenses.exec()
    
    def open_credits(self) -> None:
        self.credits = SecondaryWindows.TextReadDialog("./credits.md")
        self.credits.setWindowTitle("Credits")
        self.credits.exec()
    
    def open_help(self) -> None:
        self.credits = SecondaryWindows.TextReadDialog("./help.md")
        self.credits.setWindowTitle("Help")
        self.credits.exec()