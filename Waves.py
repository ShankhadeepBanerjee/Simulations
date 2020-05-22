import pygame, sys
from pygame.locals import *
	
	
class Screen:
    def __init__(self):
        
        self.drop_list = []
        self.drop_def_rad = 20
            
    def add_drop(self,drop_coords):
        self.drop_list.append([drop_coords,self.drop_def_rad])

                
    def draw_drops(self):

        drops_to_pop = []
        
        for ind, drop in enumerate(self.drop_list):
            pygame.draw.circle(Surf, Blue, drop[0], self.drop_list[ind][1], 1)
            pygame.draw.circle(Surf, Blue_1, drop[0], self.drop_list[ind][1]-5, 2)
            pygame.draw.circle(Surf, Blue_2, drop[0], self.drop_list[ind][1]-10, 3)
            pygame.draw.circle(Surf, Blue_3, drop[0], self.drop_list[ind][1]-15, 4)

            if self.drop_list[ind][1] < 500:
                self.drop_list[ind][1] += 1
            else:
                drops_to_pop.append(ind)
                
        for this_drop in drops_to_pop:
            self.drop_list.pop(this_drop)
def main():
    global Surf,Blue,Blue_1,Blue_2,Blue_3
    
    fpsclock = pygame.time.Clock()
    Black = (0,0,0)
    White = (255,255,255)
    Blue = (0,10,255)
    Blue_1 = (0,20,225)
    Blue_2 = (0,30,200)
    Blue_3 = (0,40,175)

    FPS = 50
    
    pygame.init()
    display = (500,500)
    Surf = pygame.display.set_mode(display)
    rad = 16
    drop_state = False

    
    theScreen = Screen()
	
    while True:
        Surf.fill(White)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    mousex,mousey = pygame.mouse.get_pos()
                    theScreen.add_drop((mousex,mousey))

        if theScreen.drop_list:
            theScreen.draw_drops()
        
        pygame.display.update()
        fpsclock.tick(FPS)


main()
