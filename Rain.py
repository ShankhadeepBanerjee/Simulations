import pygame, sys
from pygame.locals import *
from random import randrange, randint

fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)

Width = 500
Hieght = 500
FPS = 60

pygame.init()
display = (Width, Hieght)
Surf = pygame.display.set_mode(display)

class Cell(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.width = 5
		self.hieght = 15
		self.z_val = 0.1 * randint(0,9)
		self.width *= self.z_val
		self.hieght *= self.z_val


		self.image = pygame.Surface([self.width, self.hieght])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		

		self.rect.left = randint(0, Width - int(self.width))
		self.rect.bottom = randint(-500, -10)

		self.speedy = 10
		self.speedy *= self.z_val

		

	def update(self):
		if self.rect.top > Width:
			self.rect.bottom = -10
		else:
			self.rect.y += self.speedy
		

			
			


all_sprites = pygame.sprite.Group()


for i in range(500):
	cell = Cell()
	all_sprites.add(cell)


def Rain():
	n = 0
	cells_len_High = False
	while not cells_len_High:

		Surf.fill(Black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		all_sprites.update()
		all_sprites.draw(Surf)
		

			

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	Rain()