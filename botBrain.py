import pyautogui
import pytesseract
from dataProcessing import removeUselessCharacters
from constants import *
import time

def move(keys, keyUpAll=False):
    if keyUpAll:
        allKeys = ['W', 'A', 'S', 'D']
        for key2 in allKeys:
            pyautogui.keyUp(key2)
        pyautogui.mouseUp()
    for key in keys:
        print('keydown', key)
        pyautogui.keyDown(key)

def extractCoords(regionCoords):
    pic = pyautogui.screenshot(region=regionCoords)
    coords = pytesseract.image_to_string(pic)
    
    if '.' in coords:
         coords = coords.split('. ')
    else:
        coords = coords.split(', ')
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