import pyautogui as pygui
import time
from LoLPreparing import GarenaWin
from LoLPreparing import LoLMenuWin
from LoLGaming import LoLGameWin

garenaWin = GarenaWin()

garenaWin.returnToDesktop()
garenaWin.openGarena()
garenaWin.loginGarena()