import pyautogui as gui
import time 
while True:
    time.sleep(20)
    gui.moveTo(gui.position().x+1,gui.position().y+1)