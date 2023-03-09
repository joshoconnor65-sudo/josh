import pyautogui
from textExtract import extractText
import numpy as np
import cv2
import time
import pytesseract
from PIL import Image
import pydirectinput
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

farmCoords = [51, 71, 47]

time.sleep(2)
while True:
    pic = pyautogui.screenshot(region=(320, 210, 290, 50))
    # pic.save('ok.png')
    coords = pytesseract.image_to_string(pic)
    # coords = coords.split(' ')
    print(coords.split(','), 'coords')
    coords = coords.split(',')
    i = 0
    for coord in coords:
        coord = coord.replace(')', ' ')
        coord = coord.replace('(', ' ') 
        coord = coord.replace('/', ' ') 
        coord = coord.replace('|', ' ') 
        try:
            coord = int(coord)
            coordType = coordOptions[i]
            currentCoords[f"{coordType}"] = coord
            print(f"{coordType}={coord}")
            i += 1
            print(list(currentCoords.values()) == farmCoords)
            if list(currentCoords.values()) == farmCoords:
                pyautogui.keyDown('W')
                pyautogui.keyDown('D')
                pyautogui.mouseDown()
                print("LETS GO")
        except:
            print('error')
        
    time.sleep(0.1)