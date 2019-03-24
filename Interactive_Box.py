import pygame,sys
from pygame.locals import *


def draw_box(posx,posy):
    pygame.draw.circle(Surf, Blue, (posx,posy),50,5)
    
def main():
    global Surf,White,Blue

    White = (255,255,255)
    Blue = (0,0,255)

    pygame.init()
    display = (500,500)
    Surf = pygame.display.set_mode(display)

    box_pos_chng = False
    posx,posy = -200,-200
    
    while True:
        Surf.fill(White)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                if not box_pos_chng:
                    box_pos_chng = True
                target_posx, target_posy = pygame.mouse.get_pos()
##                target_posx -= 25
##                target_posy -= 25

            
        if box_pos_chng:
            
            if target_posx > posx:
                posx += 1
            else:
                posx -= 1

            if target_posy > posy:
                posy += 1
            else:
                posy -= 1

            if (target_posx-2 <posx < target_posx+2 and target_posy-2 < posy <target_posy+2):
                box_pos_chng = False
                
        draw_box(posx,posy)
        pygame.display.update()
        


main()
