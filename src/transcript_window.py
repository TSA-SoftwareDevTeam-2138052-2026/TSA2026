import tkinter.filedialog as dialog
import threading
import time
isGUI = True
try:
    import pygetwindow as gw
except:
    isGUI = False
    print("ERROR IMPORTING GUI FOR TRANSCRIPT WINDOW.")
import tkinter as tk

def switch_item_thread():
    time.sleep(1)
    if isGUI:
        try:
            windows = gw.getWindowsWithTitle("Open") # type: ignore
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
        except:
            print("N/A")

class TranscriptWindow:
    
    @classmethod
    def show_file_dir(cls) -> str:
        thread = threading.Thread(target=switch_item_thread)
        thread.start()
        try:
            return dialog.askopenfilename(filetypes=[("Video files", ".mp4 .webm .mpg .ogg .avi .mov .flv")]) # get the file name
        except: # in case gui is not available.
            return input("Paste file directory for video to transcribe here:\n> ")
    @classmethod
    def show_transcript(cls, transcript_dir):
        pass # we'll get 'em next time