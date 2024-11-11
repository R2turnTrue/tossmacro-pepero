import time
import pyautogui

pyautogui.PAUSE = 0.0

while True:
    print("CLICK")
    pyautogui.click(253, 623, _pause=False)
    time.sleep(1)