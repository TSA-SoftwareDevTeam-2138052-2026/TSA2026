import keyboard
import time
from PyVisualHelp import screenshot
from ffmpegManager import ffmpeg_manager
    
keyboard.add_hotkey('ctrl+\\', screenshot.take_and_show_screenshot)

ffmpeg_path = ffmpeg_manager.download_ffmpeg()
print(ffmpeg_path)

while True:
    time.sleep(1)