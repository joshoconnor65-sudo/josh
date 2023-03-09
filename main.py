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

time.sleep(2)
pydirectinput.click(240, 240)
# while True:
#     pic = pyautogui.screenshot(region=(320, 210, 290, 50))
#     # pic.save('ok.png')
#     coords = pytesseract.image_to_string(pic)
#     # coords = coords.split(' ')
#     print(coords.split(','), 'coords')
#     coords = coords.split(',')
#     i = 0
#     for coord in coords:
#         coord = coord.replace(')', ' ')
#         coord = coord.replace('(', ' ') 
#         coord = coord.replace('/', ' ') 
#         coord = coord.replace('|', ' ') 
#         try:
#             coord = int(coord)

#             print(f"{coordOptions[i]}={coord}")
#             i += 1
#         except:
#             print('error')
        
#     time.sleep(0.1)