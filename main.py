import time

import keyboard
import pyautogui
import win32api
import win32con


# Tile 1 Position: X:  "pixel" Y:  "pixel" RGB: ( 0, 0, 0)
# Tile 2 Position: X:  "pixel" Y:  "pixel" RGB: ( r, g, b)
# Tile 3 Position: X:  "pixel" Y:  "pixel" RGB: ( r, g, b)
# Tile 4 Position: X:  "pixel" Y:  "pixel" RGB: ( r, g, b)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # Pausing for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)
