import keyboard
import time
import PyVisualHelp
import GUI

keyboard.add_hotkey('ctrl+\\', PyVisualHelp.take_and_show_screenshot)

GUI.display_gui()

while True:
    time.sleep(1)