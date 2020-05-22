import pygame, sys, math
from pygame.locals import *
from Vectors import  Point, dist
from random import randint, choice
# import random

fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)


FPS = 15

pygame.init()
Width, Hieght = 250, 250
display = (Width, Hieght)

Surf = pygame.display.set_mode(display)





class Ball:
	def __init__(self, r = 5, color = BLUE, x = randint(0, 500), y = randint(0, 500)):
		self.r = r
		self.x = x
		self.y = y
		self.color = color
		self.directions = [-30, 30] 
		self.speedx = choice(self.directions)
		self.speedy = choice(self.directions)

	def update(self):
		self.speedx = choice(self.directions)
		self.speedy = choice(self.directions)

		self.x += self.speedx
		self.y += self.speedy
		
		if self.x - self.r <= 0:
			self.x = 0 + self.r
			self.speedx = -self.speedx

		elif self.x + self.r >= Width:
			self.x = Width - self.r
			self.speedx = -self.speedx

		elif self.y - self.r <= 0:
			self.y = 0 + self.r
			self.speedy = -self.speedy

		elif self.y + self.r >= Hieght:
			self.y = Hieght - self.r
			self.speedy = -self.speedy
			
		

	def draw(self):
		pygame.draw.circle(Surf, self.color, (self.x,self.y), self.r ,5)
		self.update()

    

class Segment:
	def __init__(self, start, mag, angle, base = True):
		self.base = base
		self.start = Point(start)
		self.angle = angle
		self.mag = mag
		self.endx = (self.start.x + self.mag * math.cos(math.radians(self.angle)))
		self.endy = (self.start.y - self.mag * math.sin(math.radians(self.angle)))
		self.end = Point((self.endx, self.endy))
		self.targetvect = Point((0,0))
		self.on_target = False


	def follow(self, target = False):
	
		if self.base:
			if target:
				self.targetvect = Point(target)
				new_angle = self.start.get_angle(self.targetvect)
				self.angle = new_angle
		else:
			if target and self.end.points != target:
				self.on_target = False
				self.targetvect = Point(target)
				self.end = self.targetvect
				
				new_angle = self.start.get_angle(self.targetvect)
				self.angle = new_angle


	def update(self):
		if self.base:
			if self.targetvect.x < self.start.x:
				self.endx = (self.start.x - self.mag * math.cos(math.radians(self.angle)))
				self.endy = (self.start.y + self.mag * math.sin(math.radians(self.angle)))
				
			else:
				self.endx = (self.start.x + self.mag * math.cos(math.radians(self.angle)))
				self.endy = (self.start.y - self.mag * math.sin(math.radians(self.angle)))
			self.end = Point((self.endx, self.endy))

		else:
			if not self.on_target:
				d = dist(self.start, self.targetvect)
				if d > self.mag:
					d -= self.mag
				else:
					d = 2
				if self.targetvect.x < self.start.x:
					x = (self.start.x - d * math.cos(math.radians(self.angle)))
					y = (self.start.y + d * math.sin(math.radians(self.angle)))
					
				else:
					x = (self.start.x + d * math.cos(math.radians(self.angle)))
					y = (self.start.y - d * math.sin(math.radians(self.angle)))

				self.start = Point((x, y))
				self.on_target = True


	def draw(self):
		pygame.draw.line(Surf, BLUE, self.start.points, self.end.points, 2)
		pygame.draw.circle(Surf, Black, self.start.points, 2)
		pygame.draw.circle(Surf, White, self.end.points, 2)



class Arm:
	def __init__(self, parts, size, Base = (Width//2, Hieght//2)):
		self.parts = parts
		self.size = size
		self.Base = Base
		self.segments = []
		for i in range(self.parts):
			if 0 < i:
				Seg = Segment(self.segments[i-1].end.points, self.size, 0, False)
				self.segments.append(Seg)
			else:
				Seg = Segment(Base, self.size, 0, False)
				self.segments.append(Seg)


	def follow(self, point):
		for i, elem in enumerate(self.segments):
			if i == 0:
				elem.follow(point)              # maintain this order
				elem.update()
			else:
				elem.follow(self.segments[i-1].start.points)
				elem.update()

	def show(self):
		for i, elem in enumerate(self.segments):
			elem.draw()


def game():
	B1 = Ball()

	arm = Arm(30, 20)
	while True:

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		arm.follow((B1.x, B1.y))
		arm.show()


		B1.draw()
			

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()