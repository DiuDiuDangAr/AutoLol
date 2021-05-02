import pyautogui as pygui
import time
import mouse
import cv2 as cv

class GarenaWin:

	def __init__(self, oog_pat_path = 'cv_pattern/out_of_game/'):
		self.oog_pat_path = oog_pat_path

	def easyClick(self, target_1, target_2):
		pygui.moveTo(pygui.locateOnScreen(self.oog_pat_path+target_1))
		pygui.moveTo(pygui.locateOnScreen(self.oog_pat_path+target_2))
		time.sleep(0.5)
		pygui.click(clicks=1)
		pygui.moveTo(1020,20,0.5)

	def returnToDesktop(self):
		pygui.keyDown('win')
		pygui.press('d')
		pygui.keyUp('win')

	def openGarena(self):
		self.easyClick('garena_icon.png', 'garena_icon_dark.png')
		# todo ... check whether the garena win is opened?

	def loginGarena(self):
		#pygui.moveTo(1154,653, 3)
		self.easyClick('login_btn.png', 'login_btn_dark.png')

	def openLolApp(self):
		#3. open LoL
		#3-1. find the check mark, and click the 英雄聯盟 big icon
		time.sleep(8)
		check_mark_loc = pygui.locateOnScreen(self.oog_pat_path + 'check_mark.png')
		if check_mark_loc is None:
			pygui.moveTo(1074,387, 5)
		else:
			try:
				pygui.moveTo(check_mark_loc[0]+50,check_mark_loc[1]+50,1.5)
			except Exception as e:
				print(e)
		pygui.click(clicks=1)
		time.sleep(3)

		#3-2. find the 啟動 btn, and click it
		home_btn_loc = pygui.locateOnScreen(self.oog_pat_path + 'home_btn.png')
		if home_btn_loc is not None:
			pygui.moveTo(home_btn_loc)
			pygui.click(clicks=1)
		time.sleep(2)

		start_btn_loc = pygui.locateOnScreen(self.oog_pat_path + 'start_btn.png')
		start_btn_dark_loc = pygui.locateOnScreen('cv_pattern/out_of_game/start_btn_dark.png')
		if start_btn_loc != None:
			pygui.moveTo(start_btn_loc)
		elif start_btn_dark_loc != None:
			pygui.moveTo(start_btn_dark_loc)
		else:
			pygui.moveTo(955,834, 3)
			print('force to move the cursor')
		pygui.click(clicks=3)

class LoLMenuWin:

	def __init__(self, ig_pat_path = 'cv_pattern/in_game/'):
		self.ig_pat_path = ig_pat_path

	def detectAndPress(self, btn_1, btn_2, force_x, force_y):
		btn_loc = pygui.locateOnScreen(self.ig_pat_path+btn_1)
		btn_light_loc = pygui.locateOnScreen(self.ig_pat_path+btn_2)
		if btn_loc != None:
			pygui.moveTo(btn_loc)
		elif btn_light_loc != None:
			pygui.moveTo(btn_light_loc)
		else:
			pygui.moveTo(force_x,force_y, 3)
			print('force to move the cursor to destination: btn_1')
		time.sleep(2)
		print('start clicking')
		pygui.mouseDown()
		time.sleep(0.5) #or whatever you need, if even needed
		pygui.mouseUp()
		time.sleep(2)

	def openGameAI(self, difficulty):
		if difficulty == 'easy':
			pass
			#0. click award
			self.closeAwardBox()
			#1. click 開始
			self.detectAndPress('start_btn.png','start_btn_light.png',445,197)

			#2. click 玩家vs電腦
			self.detectAndPress('player_vs_com.png','player_vs_com_light.png',526,257)

			#3. click 確認
			self.detectAndPress('confirm_btn.png','confirm_btn_light.png',859,840)

			#4. click 尋找對戰
			self.detectAndPress('search_btn.png','search_btn_light.png',859,840)

			#5. click 接受
			# todo... checking whether are we in the selection pane
			while self.isStillWaiting():
				self.detectAndPress('accept_btn.png','accept_btn_light.png',967,702)
				time.sleep(1.5)

			#6. select champion
			self.selectAndLockChamp()

			#7. check loading

			#

	def isStillWaiting(self, target_1, target_2):
		ahri = pygui.locateOnScreen(self.ig_pat_path+'champion_head/ahri_selection.png', confidence=0.7)
		ahri_l = pygui.locateOnScreen(self.ig_pat_path+'champion_head/ahri_selection_light.png', confidence=0.7)
		if (ahri is not None) or (ahri_l is not None):
			return False
		else:
			return True

	def closeAwardBox(self):
		pygui.moveTo(1069,726,0.5)
		pygui.mouseDown()
		time.sleep(0.5) #or whatever you need, if even needed
		pygui.mouseUp()

	def clickOneMoreGame(self):
		self.detectAndPress('one_more_btn.png','one_more_btn_light.png',859,840)

	def selectAndLockChamp(self):
		self.detectAndPress('champion_head/ahri_selection.png', 'champion_head/ahri_selection_light.png',880,366)
		self.detectAndPress('champion_head/sivir_selection.png', 'champion_head/sivir_selection_light.png',780,366)
		self.detectAndPress('champion_head/cait_selection.png', 'champion_head/cait_selection_light.png',680,366)
		self.detectAndPress('champion_head/ashe_selection.png', 'champion_head/ashe_selection_light.png',880,333)		
		self.detectAndPress('lock_btn.png', 'lock_btn.png',859,840)

if __name__ == '__main__':
	garenaWin = GarenaWin()
	lolMenuWin = LoLMenuWin()
	
	garenaWin.returnToDesktop()
	garenaWin.openGarena()
	garenaWin.loginGarena()
	garenaWin.openLolApp()
	
	time.sleep(25)
	
	lolMenuWin.openGameAI('easy')