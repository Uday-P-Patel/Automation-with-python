from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(0.5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    img = pyautogui.screenshot(region=(80,435,780,540))
    width,height=img.size
    for x in range(0,width,10):
        for y in range (0,height,10):
            r,g,b=img.getpixel((x,y))
            if b==195:
                click(x+80,y+435)
                time.sleep(0.05)
                break;
