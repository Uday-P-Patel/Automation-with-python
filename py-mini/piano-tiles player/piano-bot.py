from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  373 Y:  500 RGB: (153, 159, 231)
#X:  439 Y:  500 RGB: (156, 162, 231)
#X:  502 Y:  500 RGB: (155, 161, 230)
#X:  579 Y:  500 RGB: (158, 163, 231)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(373,400)[0]== 0:
        click(373,400)
    if pyautogui.pixel(439,400)[0]== 0:
        click(439,400)
    if pyautogui.pixel(502,400)[0]== 0:
        click(502,400)
    if pyautogui.pixel(579,400)[0]== 0:
        click(579,400)
    
