import keyboard
import time
import PyVisualHelp
    
keyboard.add_hotkey('ctrl+\\', PyVisualHelp.take_and_show_screenshot)

while True:
    time.sleep(1)