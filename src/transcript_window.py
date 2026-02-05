import tkinter.filedialog as dialog
import threading
import pygetwindow as gw
import time

import tkinter as tk

def switch_item_thread():
    time.sleep(1)
    windows = gw.getWindowsWithTitle("Open")
    # Switch to the window
    if windows != []:
        window = windows[0]
        try:
            window.activate()
        except Exception as e:
            try:
                window.minimize()
                window.maximize()
            except Exception as e:
                print("Error opening window:", e)

class TranscriptWindow:
    
    @classmethod
    def show_file_dir(cls) -> str:
        thread = threading.Thread(target=switch_item_thread)
        thread.start()
        return dialog.askopenfilename(filetypes=[("Video files", ".mp4 .webm .mpg .ogg .avi .mov .flv")]) # get the file name

    @classmethod
    def show_transcript(cls, transcript_dir):
        pass # we'll get 'em next time