import keyboard
import time
from PyVisualHelp import screenshot
from ffmpeg_manager import ffmpeg_manager
    
keyboard.add_hotkey('ctrl+\\', screenshot.take_and_show_screenshot)

ffmpeg_manager.download_ffmpeg()

path_to_vid = ffmpeg_manager.remove_video(input()) # demo for now, we will add actual file dialogs later.

from PyAudioTranscript import PyAudioTranscript

print(PyAudioTranscript.turn_into_transcript(path_to_vid))

while True:
    time.sleep(1)