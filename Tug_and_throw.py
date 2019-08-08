import pygame
import sys
import math
from pygame.locals import *
from random import randint, choice
from random import randint


global DISPLAYSURF, BLUE, Hieght, Width
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

reducing_factor = 0.08


FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()
Hieght, Width = 600, 600
DISPLAYSURF = pygame.display.set_mode((Hieght, Width))
pygame.display.set_caption("Tug and Throw")




class Ball:
    def __init__(self, r, x=-100, y=-100):
        self.r = r
        self.x = x
        self.y = y
        self.speedx = 0  
        self.speedy = 0  

    def draw_ball(self):
        self.x += self.speedx
        self.y += self.speedy
        pygame.draw.circle(DISPLAYSURF, BLUE, (self.x, self.y), self.r)

    def change_direction(self, changex=False, changey=False):
        if changex:
            self.speedx = -self.speedx
        elif changey:
            self.speedy = -self.speedy

    def check_collision(self):
        changex = (0 in range(self.x-self.r, self.x+self.r)) or(Width in range(self.x-self.r,
        self.x+self.r) or self.x-self.speedx <= 0 or self.x + self.speedx >= Width)
        #

        changey = (0 in range(self.y-self.r, self.y+self.r)) or(Hieght in range(self.y-self.r,
        self.y+self.r) or self.y-self.speedy <= 0 or self.y + self.speedy >= Hieght)
        #

        if changex:
            if self.x-self.r <= 0 or self.x-self.speedx <= 0:
                self.x = self.r
            else:
                self.x = Width-self.r
        if changey:
            if self.y - self.r <= 0 or self.y-self.speedy <= 0:
                self.y = self.r
            else:
                self.y = Hieght - self.r

        self.change_direction(changex, changey)


class Screen:
    def __init__(self, Objlist=[]):
        self.objlist = Objlist

    def _add_ball(self, ball):
        self.objlist.append(ball)

    def show(self):
        for i in self.objlist:
            i.check_collision()
            i.draw_ball()


def main():
    screen = Screen()

    creat = False
    started = False
    running = False

    while True:
        DISPLAYSURF.fill(WHITE)

        screen.show()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                started = True
                startx, starty = event.pos

            elif started and event.type == pygame.MOUSEMOTION:
                running = True
                midx, midy = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                endx, endy = event.pos
                started = False
                if running:
                    creat = True

        if started and running:
            pygame.draw.line(DISPLAYSURF, BLUE, (startx, starty), (midx, midy))

        if creat and running:
            ball = Ball(10, abs(endx), abs(endy))
            temp_speedx = math.ceil(abs((startx - endx) * reducing_factor))
            temp_speedy = math.ceil(abs((starty - endy) * reducing_factor))

            if startx < endx:
                ball.speedx = -temp_speedx
            else:
                ball.speedx = temp_speedx

            if starty < endy:
                ball.speedy = -temp_speedy
            else:
                ball.speedy = temp_speedy

            screen._add_ball(ball)
            creat = False
            running = False

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
