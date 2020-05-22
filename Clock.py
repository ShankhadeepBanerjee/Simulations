import pygame, sys, math
from pygame.locals import *
from time import sleep, ctime

fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255, 0, 0)


FPS = 30

pygame.init()
Width = 500
Hieght = 500
display = (Width, Hieght)
Surf = pygame.display.set_mode(display)


class Clock():
	def __init__(self, time = [0, 0, 0]):


		self.center = (Width//2, Hieght//2)

		self.sec = int(time[2]) +15
		self.min = (((int(time[1]) + 15)  * 60) + self.sec)# % 60
		self.hr = ((((int(time[0]) + 3) % 12) * 3600) + self.min) #% 3600

		self.sec_hand_len = 120 
		self.sec_hand_end = (self.center[0] - self.sec_hand_len * math.cos(math.radians(self.sec * 6)), self.center[1] - self.sec_hand_len * math.sin(math.radians(self.sec * 6)))

		self.min_hand_len = 100
		self.min_hand_end = (self.center[0] - self.min_hand_len * math.cos(math.radians(self.min * 0.1)), self.center[1] - self.min_hand_len * math.sin(math.radians(self.min * 0.1)))

		self.hr_hand_len = 80
		self.hr_hand_end = (self.center[0] - self.hr_hand_len * math.cos(math.radians(self.hr * 0.0083)), self.center[1] - self.hr_hand_len * math.sin(math.radians(self.hr * 0.0083)))

		self.num_dict = {}
		for i in range(1, 13):
			x = self.sec_hand_len * math.cos(math.radians(i * 30))
			y = self.sec_hand_len * math.sin(math.radians(i * 30))
			self.num_dict[i] = (self.center[0] - x, self.center[1] - y)

	def update(self):
		self.sec = (self.sec + 1) 
		x = self.sec_hand_len * math.cos(math.radians(self.sec * 6))
		y = self.sec_hand_len * math.sin(math.radians(self.sec * 6))
		self.sec_hand_end = (self.center[0] - x, self.center[1] - y)

		

		self.min = (self.min + 1) 
		x = self.min_hand_len * math.cos(math.radians(self.min * 0.1))
		y = self.min_hand_len * math.sin(math.radians(self.min * 0.1))
		self.min_hand_end = (self.center[0] - x, self.center[1] - y)

		
		self.hr = (self.hr + 1) 
		x = self.hr_hand_len * math.cos(math.radians(self.hr * 0.0083))
		y = self.hr_hand_len * math.sin(math.radians(self.hr * 0.0083))
		self.hr_hand_end = (self.center[0] - x, self.center[1] - y)


	def show(self):

		pygame.draw.circle(Surf, BLUE, self.center, self.sec_hand_len+5, 2)
		pygame.draw.line(Surf, BLUE, self.center, self.sec_hand_end, 2)
		pygame.draw.line(Surf, RED, self.center, self.min_hand_end, 6)
		pygame.draw.line(Surf, GREEN, self.center, self.hr_hand_end, 10)
		# for i in self.num_dict:
		# 	pygame.draw.line(Surf, Black, self.center, self.num_dict[i], 2)
		pygame.draw.circle(Surf, Black, self.center, 5, False)






def game():
	time = ctime()
	splited_time = time.split(" ")[3].split(":")


	clk = Clock(splited_time)

	while True:

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		clk.show()
		pygame.time.delay(1000)
		clk.update()
		
				

		pygame.display.update()
		#fpsclock.tick(FPS)

if __name__ == "__main__":
	game()