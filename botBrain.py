import pyautogui

def move(keys, keyUpAll=False):
    allKeys = ['W', 'A', 'S', 'D']
    if keyUpAll:
        for key2 in allKeys:
            pyautogui.keyUp(key2)
        pyautogui.mouseUp()
    for key in keys:
        print('keydown', key)
        pyautogui.keyDown(key)