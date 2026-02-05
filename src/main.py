import keyboard # keyboard shortcuts
import time # to wait before refreshing screen
from PyVisualHelp import screenshot # screenshotting
from ffmpeg_manager import ffmpeg_manager # ffmpeg managing
from transcript_window import TranscriptWindow # Transcript Window opener
from PyAudioTranscript import PyAudioTranscript # Getting transcript
import os # clearing the screen

is_active = False

def save_transcript():
    is_active = True
    try:
        file_dir = TranscriptWindow.show_file_dir()
        print("Transcribing...")
        with open(file_dir + "_transcript.txt", 'w') as file:
            file.write(PyAudioTranscript.turn_into_transcript(file_dir))
            file.close()
        print("DONE!")
        
        with open(file_dir + "_transcript.txt", 'r') as file:
            print(file.read())
            file.close()
        print("Press enter to continue...")
        keyboard.wait('enter')
    except:
        print("Error")
    is_active = False

keyboard.add_hotkey('ctrl+\\', screenshot.take_and_show_screenshot)
keyboard.add_hotkey('ctrl+shift+enter', callback=save_transcript) # type: ignore

ffmpeg_manager.download_ffmpeg()

while True:
    if not is_active:
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print("GUIDE:")
        print("Get Black-and-White Screenshot: Ctrl + \\")
        print("Get Transcript: Ctrl + Shift + Enter")
        time.sleep(1)