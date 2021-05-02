import pyautogui as pygui
import time
import keyboard
import cv2 as cv
from param.garenaparam import Res_19201080 as p
from LoLPreparing import GarenaWin
from LoLPreparing import LoLMenuWin
from LoLGaming import LoLGameWin

"""
time.sleep(3)
print(pygui.position())
pygui.moveTo(pygui.locateOnScreen('lol.png',confidence=0.7))
#ygui.alert(text='', title='', button='OK')
lolMenuWin = LoLMenuWin()
while True:
	print(lolMenuWin.stillWaiting())
	time.sleep(1.5)
"""
print(pygui.locateOnScreen('cv_pattern/in_game/praise_text.png', confidence = 0.7))


time.sleep(2)
print(pygui.position())
print(pygui.size())
"""
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('e')
time.sleep(0.1)
keyboard.press_and_release('0')
time.sleep(0.1)
keyboard.press_and_release('4')
time.sleep(0.1)
keyboard.press_and_release('enter')
"""