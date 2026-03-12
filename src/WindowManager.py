from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import main

class WindowManager:
    def __init__(self, main_win: main.MainWindow):
        self.main_win = main_win
    