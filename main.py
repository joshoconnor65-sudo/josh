import pyautogui
import time
from botBrain import extractCoords
from constants import *
from botBrain import move, moveByState

state = 'forward'

lastCoords = []
while True:
    coords = extractCoords(regionCoords=(320, 210, 290, 50))

    if not coords:
        continue

    x,y,z = coords

    farmPoint = farmPoints[state]
    if (z == farmPoint or x == farmPoint):
        pyautogui.mouseUp()
        if state == 'forward':
            state = 'backward'
        else:
            state = 'forward'

        moveByState(state)

        
        
    time.sleep(0.1)