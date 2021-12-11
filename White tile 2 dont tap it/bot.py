from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(600,300)[0] == 0:
        click(600,300)
    if pyautogui.pixel(700,300)[0] == 0:
        click(700,300)
    if pyautogui.pixel(800,300)[0] == 0:
        click(800,300)
    if pyautogui.pixel(900,300)[0] == 0:
        click(900,300)
    if pyautogui.pixel(600,400)[0] == 0:
        click(600,400)
    if pyautogui.pixel(700,400)[0] == 0:
        click(700,400)
    if pyautogui.pixel(800,400)[0] == 0:
        click(800,400)
    if pyautogui.pixel(900,400)[0] == 0:
        click(900,400)
    if pyautogui.pixel(600,500)[0] == 0:
        click(600,500)
    if pyautogui.pixel(700,500)[0] == 0:
        click(700,500)
    if pyautogui.pixel(800,500)[0] == 0:
        click(800,500)
    if pyautogui.pixel(900,500)[0] == 0:
        click(900,500)
    if pyautogui.pixel(600,600)[0] == 0:
        click(600,600)
    if pyautogui.pixel(700,600)[0] == 0:
        click(700,600)
    if pyautogui.pixel(800,600)[0] == 0:
        click(800,600)
    if pyautogui.pixel(900,600)[0] == 0:
        click(900,600)
        
        
