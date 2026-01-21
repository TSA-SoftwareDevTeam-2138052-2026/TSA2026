import keyboard
import time
import PyVisualHelp
import FFMPEG_handler
    
keyboard.add_hotkey('ctrl+\\', PyVisualHelp.take_and_show_screenshot)

FFMPEG_handler.download_ffmpeg()

while True:
    time.sleep(1)