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
from botBrain import extractCoords
from constants import *

state = 'forward'

lastCoords = []
while True:
    coords = extractCoords()

    if not coords:
        continue

    x,y,z = coords

 
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