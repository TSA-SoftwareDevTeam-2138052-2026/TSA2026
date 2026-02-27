print("Importing packages...")
import keyboard # keyboard shortcuts
import time # to wait before refreshing screen
print("If the program seems like it is frozen, wait a few moments.")
from PyVisualHelp import Screenshot # screenshotting
from ffmpeg_manager import ffmpeg_manager # ffmpeg managing
from transcript_window import TranscriptWindow # Transcript Window opener
from PyAudioTranscript import PyAudioTranscript # Getting transcript
import threading # makes it faster
from captions import Captions
import os # to auto delete temp

is_active = False

print("Testing for GUI...")
isGUI = True
try:
    import pyautogui
    import pygetwindow as gw
    del pyautogui # delete the imports
    del gw # delete the imports
    print("GUI GOOD")
except:
    isGUI = False
    print("GUI CHECK FAILED")

def save_transcript():
    try:
        file_dir = TranscriptWindow.show_file_dir()
        print("Transcribing...")
        
        auto_find = file_dir.split("/")[-1].split(".")[0]
        file_dir2 = file_dir.split("/").copy()
        file_dir2[-1] = auto_find
        auto_find_dir = "/".join(file_dir2)
        
        with open(file_dir + ".txt", 'w') as file:
            file.write(str(PyAudioTranscript.turn_into_transcript(file_dir)))
            file.close()
        print("DONE!")
        
        choice = TranscriptWindow.ask_for_subtitle_type().lower()
        
        ext = ""
        
        if choice == "v":
            ext = "vtt"
        elif choice == "s":
            ext = "srt"
        else:
            ext = "srt"
        
        with open(file_dir + ".txt", 'r') as file:
            with open(auto_find_dir  + "." + ext, "w") as caption_file:
                caption_file.write(Captions.convert_temp_to_captions(file.read(), ext))
                caption_file.close()
            file.close()
        
        os.remove(file_dir + ".txt")
        print("returning...")
        time.sleep(2)
    except:
        print("Error")

def handle_screenshot():
    global is_active
    is_active=True
    Screenshot.contrast_screenshot()
    is_active=False

def handle_transcript():
    global is_active
    is_active=True
    save_transcript()
    is_active=False

if isGUI:
    keyboard.add_hotkey('ctrl+\\', handle_screenshot)
    keyboard.add_hotkey('ctrl+shift+enter', handle_transcript) # type: ignore


ffmpeg_manager.download_ffmpeg()

while True:
    if not is_active:
        #if os.name == "nt":
        #    os.system('cls')
        #else:
        #    os.system('clear')
        print("\033c") # Clears the screen
        print("GUIDE:")
        if isGUI:
            print("Get Black-and-White Screenshot: Ctrl + \\")
            print("Get Transcript: Ctrl + Shift + Enter")
            time.sleep(1)
        else:
            print("Get Black-and-White Screenshot: UNAVALIABLE")
            print("Get Transcript: type \"transcript\" into terminal")
            if input("> ").lower() == "transcript":
                handle_transcript()
            time.sleep(1)
    elif is_active:
        time.sleep(1)