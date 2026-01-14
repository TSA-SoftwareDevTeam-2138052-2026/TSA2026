import cv2
import pyautogui
import keyboard
import time
import numpy as np

def take_and_show_screenshot():
    
    # Take the screenshot to display
    image = pyautogui.screenshot("image.png")
    
    # Create the window
    cv2.namedWindow("tsa_project_screenshot", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('tsa_project_screenshot',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    # Render the window    
    image = cv2.imread("image.png", 0)
    cv2.imshow("tsa_project_screenshot", image)
    keyboard.press_and_release("alt+shift+tab")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
keyboard.add_hotkey('ctrl+\\', take_and_show_screenshot)

while True:
    time.sleep(1)