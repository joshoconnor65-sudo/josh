import pyautogui

pic = pyautogui.screenshot(region=(530, 272, 100, 160))
pic.save('ok.png')
print('done')