import keyboard
import time
from PyVisualHelp import screenshot
from ffmpeg import ffmpeg
    
keyboard.add_hotkey('ctrl+\\', screenshot.take_and_show_screenshot)

ffmpeg_path = ffmpeg.download_ffmpeg()
print(ffmpeg_path)

ffmpeg.remove_video(input()) # demo for now, we will add actual file dialogs later.

while True:
    time.sleep(1)