import pyautogui
import pytesseract
from dataProcessing import removeUselessCharacters
from constants import *
import time

def move(keys, keyUpAll=False):
    allKeys = ['W', 'A', 'S', 'D']
    if keyUpAll:
        for key2 in allKeys:
            pyautogui.keyUp(key2)
        pyautogui.mouseUp()
    for key in keys:
        print('keydown', key)
        pyautogui.keyDown(key)

def extractCoords():
    pic = pyautogui.screenshot(region=(320, 210, 290, 50))
    coords = pytesseract.image_to_string(pic)
    coords.split(',')
    coords = removeUselessCharacters(coords)
    return coords

def moveByState(state):
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