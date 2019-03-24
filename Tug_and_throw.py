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


def measure_dist(a, b):
    print(a, b, ((a[0] - b[0])**2), ((a[1] - b[1])**2))
    reducing_factor = 0.08
    return(int(reducing_factor * math.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))))


class Ball:
    def __init__(self, r, x=-100, y=-100):
        self.r = r
        self.x = x
        self.y = y
        # self.directions = 0#[randint(5,20),randint(5,20),randint(-20,-5),randint(-20,-5)]
        self.speedx = 0  # choice(self.directions)
        self.speedy = 0  # choice(self.directions)

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

    ##    ball1 = Ball(70,200,150)
    ##    ball2 = Ball(30,100,150)
    ##    ball3 = Ball(20,250,300)
    ##    ball4 = Ball(8,25,30)
    ##    ball5 = Ball(8,215,340)
    ##    ball6 = Ball(8,10,40)
    ##    screen = Screen([ball1,ball2,ball3,ball4,ball5,ball6])
    ##    balllist = []
    # for i in range(30):
    ##        ball = Ball(10,randint(10,Width-10),randint(10,Width-10))
    # balllist.append(ball)
    ##
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

                # print(event.pos,"----------------1")

            elif started and event.type == pygame.MOUSEMOTION:
                running = True
                midx, midy = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                endx, endy = event.pos
                # print(event.pos,"----------------2")
                started = False
                if running:
                    creat = True

        if started and running:
            pygame.draw.line(DISPLAYSURF, BLUE, (startx, starty), (midx, midy))

        if creat and running:
            ball = Ball(10, abs(endx), abs(endy))  # randint(10,Width-10),randint(10,Width-10))
            temp_speedx = math.ceil(abs((startx - endx) * reducing_factor))
            temp_speedy = math.ceil(abs((starty - endy) * reducing_factor))
            #print(temp_speedx, temp_speedy)

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
