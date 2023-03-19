import pyautogui
import time
from botBrain import extractCoords
from constants import *
from botBrain import move

state = 'forward'

lastCoords = []
while True:
    coords = extractCoords()

    if not coords:
        continue

    x,y,z = coords

 
    if (z == farmPoints[state] or x == farmPoints[state]):
        pyautogui.mouseUp()
        if state == 'forward':
            state = 'backward'
        else:
            state = 'forward'

        if state == 'backward':
            print('before')
            move(['S', 'D'], keyUpAll=True)
            time.sleep(3)
            move(stateKeys['backward'], keyUpAll=True)   
            pyautogui.mouseDown()    

        else:
            move(stateKeys['forward'], keyUpAll=True)
            time.sleep(3.5)
            pyautogui.mouseDown()    

        
        
    time.sleep(0.1)