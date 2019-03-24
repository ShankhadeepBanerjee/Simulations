import pygame, sys, math
from pygame.locals import *
from Vectors import Vector2D, Point, dist, angle_in_points
from random import randint

fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)


FPS = 30

pygame.init()
Width, Hieght = 500, 500
display = (Width, Hieght)



#display = (1000,1000)
Surf = pygame.display.set_mode(display)

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
		# pygame.draw.circle(Surf, Black, self.start.points, 2)
		# pygame.draw.circle(Surf, White, self.end.points, 2)



# class Arm:
# 	def __init__(self, Base):


# 	def follow(self, target):

# 	def update(self):

# 	def draw(self):


def game():
	lis = []
	n = 10
	for i in range(n):
		if 0 < i < 9:
			Seg1 = Segment(lis[i-1].end.points, 50, 0, False)
			lis.append(Seg1)
		elif i == n-1:
			Seg1 = Segment((Width//2, Hieght//2), 50, 0, True)
			lis.append(Seg1)
		else:
			Seg1 = Segment((Width//2, Hieght//2), 50, 0, False)
			lis.append(Seg1)
			
		

	#lis.reverse()	
	mouse = (pygame.mouse.get_pos())
	while True:

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#====================================================================

		mouse = pygame.mouse.get_pos()
		for i, elem in enumerate(lis):
			if i == 0:
				
				elem.draw()
				elem.follow(mouse)              # maintain this order
				elem.update()

			else:	
				elem.draw()
				elem.follow(lis[i-1].start.points)
				elem.update()
		

		#====================================================================

			

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()