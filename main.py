import pyautogui
from textExtract import extractText
import numpy as np
import cv2
import time
time.sleep(5)
pic = pyautogui.screenshot(region=(530, 272, 100, 160))
pic.save('ok.png')
pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2RGBA)
cv2.imwrite('ok.jpg', pic)
coords = extractText(pic)
print(coords)