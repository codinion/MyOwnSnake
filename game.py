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
from snake import Snake
from food import Food
from soundManager import SoundManager


#Some basic initializations..
pygame.init()
display.set_caption("My Own Snake")
screen=display.set_mode((cfg.SCREEN_W,cfg.SCREEN_H))
myStage=Stage(screen)
mySnake=Snake(screen)
myFood=Food(screen,mySnake.getBodylist())
mySoundMgr=SoundManager()

#The main event loop...
isRunning=True
screen.fill((0,0,0))
onOverScreen=False
onWonScreen=False
mySoundMgr.playBackground()
while isRunning:
    evt_q=event.get()
    newD=mySnake.getCurrentDirection()

    #Process the event queue
    for e in evt_q:
        if e.type==pygame.QUIT:
            isRunning=False
            break
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                isRunning=False
                mySoundMgr.stopBackground()
                break
            if e.key==pygame.K_q:
                isRunning=False
                mySoundMgr.stopBackground()
                break
            if e.key==pygame.K_r:
                onOverScreen=False
                onWonScreen=False
                myStage=Stage(screen)
                mySnake=Snake(screen)
                myFood=Food(screen,mySnake.getBodylist())
                mySoundMgr.stopBackground()
                mySoundMgr=SoundManager()
                mySoundMgr.playBackground()
                break
            if e.key==pygame.K_b:
                cfg.BOUNDS=not cfg.BOUNDS
            if e.key==pygame.K_UP:
                newD='U'
            if e.key==pygame.K_DOWN:
                newD='D'
            if e.key==pygame.K_LEFT:
                newD='L'
            if e.key==pygame.K_RIGHT:
                newD='R'

    #If game currently active,i.e., not on GameOver or GameWon screen       
    if onOverScreen==False and onWonScreen==False:
        currentSnakeBody=mySnake.getBodylist()
        currentSnakeHead=currentSnakeBody[0]
        currentFood=myFood.getFoodXY()

        #If the snake eats the food
        if currentFood==currentSnakeHead:
            mySoundMgr.playEat()
            mySnake.moveSnake(newD,True)
            myFood.moveFood(mySnake.getBodylist())
            myStage.updateScore(1)
        else:
            mySnake.moveSnake(newD,False)
            
        #If the snake eats itself or hits the bounds(if BOUNDS on)
        if mySnake.isGameOver():
            onOverScreen=True
            mySoundMgr.stopBackground()
            mySoundMgr.playCollide()
        elif myStage.isGameWon():               #If the player has scored winning points
            onWonScreen=True
            mySoundMgr.stopBackground()
            mySoundMgr.playWinning()
        else:
            myStage.refreshStage()
            myFood.renderFood()
            mySnake.renderSnake()
        
    if onOverScreen==True:
        myStage.gameOver()
    if onWonScreen==True:
        myStage.gameWon()
    display.flip()
    sleepDuration=max(cfg.MIN_SLEEP,cfg.INIT_SLEEP-(myStage.getScore()//cfg.LEVEL_UP)*cfg.LEVEL_DT)
    sleep(sleepDuration)
    screen.fill((0,0,0))
