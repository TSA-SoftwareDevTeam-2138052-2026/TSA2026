import cv2
import os
import pyautogui
import pygetwindow as gw
from PIL import Image

class Screenshot:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    # Source - https://stackoverflow.com/a/42054155
    # Posted by Håken Lid, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-02-27, License - CC BY-SA 3.0
    @classmethod
    def contrast_photo(cls, image: Image.Image, level):
        factor = (259 * (level + 255)) / (255 * (259 - level))
        def contrast(c):
            value = 128 + factor * (c - 128)
            return max(0, min(255, value))
        return image.point(contrast)

    def contrast_screenshot(self):
        try:
            # Take the screenshot to display
            image = pyautogui.screenshot(self.data_dir + "screenshot.png") # type: ignore
            
            image = self.contrast_photo(image, 100)
            image.save(self.data_dir + "screenshot_processed.png", "png")
            
            # Create the window
            cv2.namedWindow("tsa_project_screenshot", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('tsa_project_screenshot',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

            # Render the window
            image = cv2.imread(self.data_dir + "screenshot_processed.png")
            cv2.imshow("tsa_project_screenshot", image) # type: ignore # this is completely valid
            windows = gw.getWindowsWithTitle("tsa_project_screenshot") # type: ignore # ignoring due to proper skip over if not initialiized properly
            
            # Switch to the window
            if windows != []:
                window = windows[0]
                try:
                    window.activate()
                except Exception as e:
                    try:
                        window.minimize()
                        window.maximize()
                    except Exception as e:
                        print("Error opening window:", e)
            
            # Now we wait for the user to press a key to close the window.
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            print("ERROR")
        
        if os.path.exists(self.data_dir + "screenshot.png"):
            os.remove(self.data_dir + "screenshot.png") # delete for privacy
        if os.path.exists(self.data_dir + "screenshot_processed.png"):
            os.remove(self.data_dir + "screenshot_processed.png") # delete for privacy

class Magnify:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def take_screenshot(self):
        pyautogui.screenshot(self.data_dir + "screenshot.png")
        
    def delete_screenshot(self):
        if os.path.exists(self.data_dir + "screenshot.png"):
            os.remove(self.data_dir + "screenshot.png")