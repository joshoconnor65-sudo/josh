import pyautogui
from textExtract import extractText
import numpy as np
import cv2
import time
import pytesseract
from PIL import Image
import pydirectinput
import subprocess
from dataValidators import isInt
from dataProcessing import removeUselessCharacters
coordOptions = {
    0: 'x',
    1: 'y',
    2: 'z',
}

currentCoords = {
    'x': 0,
    'y': 0,
    'z': 0,
}

state = 'forward'
stateKeys = {
    'forward': ['W', 'D'],
    'backwards': ['S']
}
farmPoints = {
    'forwards': -47,
    'backwards': 47
}

farmCoords = [51, 71, 47]

def move(keys, keyUpAll=False):
    allKeys = ['W', 'A', 'S', 'D']
    if keyUpAll:
        for key in allKeys:
            pyautogui.keyUp(key)
        pyautogui.mouseUp()

    for key in keys:
        pyautogui.keyDown(key)


time.sleep(3)
subprocess.run(["moveMouse.exe"])
while True:
    pic = pyautogui.screenshot(region=(320, 210, 290, 50))
    coords = pytesseract.image_to_string(pic)
    coords = coords.split(',')
    i = 0
    for coord in coords:
        
        coord = removeUselessCharacters(coord)
        coord = isInt(coord)
        if not coord:
            break

        coordType = coordOptions[i]
        currentCoords[f"{coordType}"] = coord

        print(f"{coordType}={coord}")
        if list(currentCoords.values()) == farmCoords:
            move(['W', 'D'])
            pyautogui.mouseDown()

        i += 1

  
        
    time.sleep(0.1)