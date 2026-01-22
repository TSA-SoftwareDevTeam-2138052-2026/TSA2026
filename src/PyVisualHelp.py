import cv2
import pyautogui
import pygetwindow as gw
import os

class screenshot():
    def __init__(self):
        pass
    
    @classmethod
    def take_and_show_screenshot(cls):
        # Take the screenshot to display
        image = pyautogui.screenshot("screenshot.png")
        
        # Create the window
        cv2.namedWindow("tsa_project_screenshot", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('tsa_project_screenshot',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        # Render the window    
        image = cv2.imread("screenshot.png", 0)
        cv2.imshow("tsa_project_screenshot", image)
        windows = gw.getWindowsWithTitle("tsa_project_screenshot")
        
        # Switch to the window
        if windows != []:
            window = windows[0]
            try:
                window.activate()
            except Exception as e:
                window.minimize()
                window.maximize()
        
        # Now we wait for the user to press a key to close the window.
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        if os.path.exists("screenshot.png"):
            os.remove("screenshot.png") # delete for privacy