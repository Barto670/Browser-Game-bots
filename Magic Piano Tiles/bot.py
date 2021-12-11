from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
win32api.SetCursorPos((760,461))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(0.01)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(619,500)[0] == 0:
        click(619,500)
    if pyautogui.pixel(734,500)[0] == 0:
        click(734,500)
    if pyautogui.pixel(800,500)[0] == 0:
        click(800,500)
    if pyautogui.pixel(900,500)[0] == 0:
        click(900,500)
