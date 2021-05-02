import pyautogui as pygui
import time
import mouse
import keyboard
import random


class LoLGameWin:
	def __init__(self, duration):
		self.lane_postition_dict = {
		"top_out" : (1703,816),
		"mid_out" : (1781,906),
		"bot_out" : (1869,992),
		"top_mid" : (1795,807),
		"mid_mid" : (1828,860),
		"bot_mid" : (1885,889),
		"top_inn" : (1833,800),
		"mid_inn" : (1873,821),
		"bot_inn" : (1888,853)}

		self.shit_words = ["e04", "okok", "back please", "nicee", "sp4", "push, thx", "coooooool", "XD", "sor", "my bad QQ"]

		self.skill = ['r','w','e','q']

		keyboard.press_and_release('y')

		time.sleep(duration)


	def simpleClick(self, click):
		pygui.mouseDown(button= click)
		time.sleep(0.5) #or whatever you need, if even needed
		pygui.mouseUp(button=click)

	def learnSkill(self):
		for s in self.skill:
			keyboard.press_and_release('ctrl+'+s)

	def buyItem(self):
		time.sleep(0.5)
		keyboard.press_and_release('p')
		pygui.moveTo(602,366, 0.5)
		self.simpleClick('right')
		keyboard.press_and_release('p')

	def walkHome(self, duration):
		pygui.moveTo(1674,1015, 0.5)
		self.simpleClick('right')
		time.sleep(duration)

	def talkSomeShits(self, text, duration):
		keyboard.press_and_release('enter')
		for c in self.shit_words[text]:
			time.sleep(0.4)
			keyboard.press_and_release(c)
		keyboard.press_and_release('enter')
		time.sleep(duration)

	def stepBack(self):
		pygui.moveTo(532,696,0.5)
		self.simpleClick('right')

	def placeWard(self, duration):
		keyboard.press_and_release('4')
		pygui.moveTo(random.randint(550,1333), random.randint(350,550),0.5)
		self.simpleClick('left')
		time.sleep(duration)

	def pingAlert(self, duration):
		keyboard.press_and_release('g')
		#pygui.moveTo(1683,796,1)
		#self.simpleClick('left')
		pygui.moveTo(random.randint(1703,1888), random.randint(800,992),0.5)
		pygui.mouseDown()
		pygui.move(random.randint(-5,5),random.randint(-5,5),1)
		pygui.mouseUp()
		time.sleep(duration)

	def useSkill(self):
		spell = self.skill[random.randint(0,2)]
		keyboard.press_and_release(spell)
		pygui.moveTo(random.randint(1060,1335), random.randint(188,368),0.5)
		self.simpleClick('left')

	def useSummonersSkill(self):
		summoner_skill = ['d','f']
		keyboard.press_and_release(summoner_skill[random.randint(0,1)])

	def backHome(self, duration):
		keyboard.press_and_release('b')
		time.sleep(duration)

	def simpleMove(self, lane):
		target_position = self.lane_postition_dict.get(lane)
		pygui.moveTo(target_position[0],target_position[1], 0.5)
		self.simpleClick('right')

	def simpleWalkA(self,lane):
		target_position = self.lane_postition_dict.get(lane)
		pygui.moveTo(target_position[0],target_position[1], 0.5)
		keyboard.press_and_release('a')
		time.sleep(0.3)
		self.simpleClick('left')
		
	def checkStartGame(self):
		pygui.locateOnScreen('cv_pattern/in_game/praise_text.png')

	def checkIfEndGame(self):
		if pygui.locateOnScreen('cv_pattern/in_game/praise_text.png',confidence=0.7) is None:
			return False
		else:
			return True

if __name__ == '__main__':
	lolGameWin = LoLGameWin(3)

	#lolGameWin.checkStartGame()

	lolGameWin.pingAlert(0.5)

	while True:
		lolGameWin.buyItem()
		lolGameWin.simpleWalkA('mid_out')
		for i in range(random.randint(13,26)):
			time.sleep(3)
			lolGameWin.simpleWalkA('mid_inn')
			lolGameWin.learnSkill()
			if i%3 == 0:
				lolGameWin.useSkill()
			if i%4 == 0:
				lolGameWin.buyItem()
			if i%7 == 0:
				lolGameWin.useSummonersSkill()
			if i%13 == 0:
				lolGameWin.pingAlert(0.5)
			if lolGameWin.checkIfEndGame():
				break;
		if lolGameWin.checkIfEndGame():
			break;
		lolGameWin.walkHome(5)
		lolGameWin.backHome(12)
		lolGameWin.placeWard(2)
		lolGameWin.talkSomeShits(random.randint(0,len(lolGameWin.shit_words)-1),3)

	time.sleep(60)