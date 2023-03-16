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
from constants import *

state = 'forward'
farmPoints[state]


def move(keys, keyUpAll=False):
    allKeys = ['W', 'A', 'S', 'D']
    if keyUpAll:
        for key2 in allKeys:
            pyautogui.keyUp(key2)
        pyautogui.mouseUp()
    for key in keys:
        print('keydown', key)
        pyautogui.keyDown(key)


lastCoords = []
while True:
    pic = pyautogui.screenshot(region=(320, 210, 290, 50))
    coords = pytesseract.image_to_string(pic)
    coords.split(',')
    coords = removeUselessCharacters(coords)
    if not coords:
        continue
    x,y,z = coords

    coordType = coordOptions[i]
    currentCoords[f"{coordType}"] = x

    if (x == 142 and z < -130):
        time.sleep(10000)
 
    if (z and x == farmPoints[state]):
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