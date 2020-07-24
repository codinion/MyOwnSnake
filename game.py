"""
This is the main file of the game which performs all the initializations and contains the game loop.
Author : Abir Mukherjee (codinion/mabir)
Email : abir.mukherjee0595@gmail.com
"""

import pygame
from pygame import display, image,event
from time import sleep
import config as cfg
from stage import Stage

#Some basic initializations..
pygame.init()
display.set_caption("My Own Snake")
screen=display.set_mode((cfg.SCREEN_W,cfg.SCREEN_H))
myStage=Stage(screen)

#The main event loop...
isRunning=True
screen.fill((0,0,0))
while isRunning:
    evt_q=event.get()
    for e in evt_q:
        if e.type==pygame.QUIT:
            isRunning=False
            break
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                isRunning=False
                break

    myStage.refreshStage()
    display.flip()
    screen.fill((0,0,0))
