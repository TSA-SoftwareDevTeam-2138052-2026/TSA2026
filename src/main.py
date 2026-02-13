print("Importing packages...")
import keyboard # keyboard shortcuts
import time # to wait before refreshing screen
print("If the program seems like it is frozen, wait a few moments.")
from PyVisualHelp import screenshot # screenshotting
from ffmpeg_manager import ffmpeg_manager # ffmpeg managing
from transcript_window import TranscriptWindow # Transcript Window opener
from PyAudioTranscript import PyAudioTranscript # Getting transcript
import threading # makes it faster

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
        with open(file_dir + "_transcript.txt", 'w') as file:
            file.write(str(PyAudioTranscript.turn_into_transcript(file_dir)))
            file.close()
        print("DONE!")
        
        with open(file_dir + "_transcript.txt", 'r') as file:
            print(file.read())
            file.close()
        print("Press enter to continue...")
        time.sleep(9999999)
    except:
        print("Error")

def handle_screenshot():
    global is_active
    is_active=True
    screenshot.take_and_show_screenshot()
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