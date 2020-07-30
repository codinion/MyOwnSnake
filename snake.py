"""
This file is the class file for the Snake object.
Author : Abir Mukherjee (codinion/mabir)
Email : abir.mukherjee0595@gmail.com
"""

import config as cfg 
from pygame import image,transform


#Class definition for the Snake object. It is responsible for handling the movement and rendering of the snake.
class Snake:
    #Constructor for Snake object
    def __init__(self,scr):
        self.screen=scr
        self.currentW=cfg.INIT_SNAKE_W
        self.currentD=cfg.INIT_SNAKE_D
        self.bodylist=[]
        self.bodylist.append((cfg.INIT_HEAD_X,cfg.INIT_HEAD_Y))
        if self.currentD=='L':
            dx=1
            dy=0
        elif self.currentD=='R':
            dx=-1
            dy=0
        elif self.currentD=='U':
            dx=0
            dy=1
        else:
            dx=0
            dy=-1
        boundsX=cfg.STAGE_W//cfg.SPRITE_W
        boundsY=cfg.STAGE_H//cfg.SPRITE_H
        for i in range(self.currentW-1):
            self.bodylist.append(((self.bodylist[-1][0]+dx)%boundsX,(self.bodylist[-1][1]+dy)%boundsY))
        self.head_image=image.load(cfg.HEAD_FILE)
        self.headSprite=transform.scale(self.head_image,(cfg.SPRITE_H,cfg.SPRITE_W))
        self.body_image=image.load(cfg.BODY_FILE)
        self.bodySprite=transform.scale(self.body_image,(cfg.SPRITE_H,cfg.SPRITE_W))

    #Function to check if the snake has eaten itself or is out of bounds(if BOUNDS are turned on)    
    def isGameOver(self):
        if cfg.BOUNDS==True:
            boundsX=(cfg.STAGE_W//cfg.SPRITE_W)
            boundsY=(cfg.STAGE_H//cfg.SPRITE_H)
            if self.bodylist[0][0]<0 or self.bodylist[0][0]>=boundsX or self.bodylist[0][1]<0 or self.bodylist[0][1]>=boundsY:
                return True
        if self.bodylist[0] in self.bodylist[1:]:
            return True
        return False
    
    #Returns the current direction of movement of snake
    def getCurrentDirection(self):
        return self.currentD
    
    #Returns the list of body indices of the snake
    def getBodylist(self):
        return self.bodylist

    #Responsible for moving the snake around
    def moveSnake(self,direction,onFood):
        if self.currentD==direction or (self.currentD=='R' and direction=='L') or (self.currentD=='D' and direction=='U') or (self.currentD=='L' and direction=='R') or (self.currentD=='U' and direction=='D'):
            self.currentD=self.currentD
        else:
            self.currentD=direction
        if self.currentD=='L':
            dx=-1
            dy=0
        elif self.currentD=='R':
            dx=1
            dy=0
        elif self.currentD=='U':
            dx=0
            dy=-1
        else:
            dx=0
            dy=1
        if(onFood==False):
            self.bodylist=self.bodylist[:-1]
        if cfg.BOUNDS==False:
            boundsX=cfg.STAGE_W//cfg.SPRITE_W
            boundsY=cfg.STAGE_H//cfg.SPRITE_H
            self.bodylist.insert(0,((self.bodylist[0][0]+dx)%boundsX,(self.bodylist[0][1]+dy)%boundsY))
        else:
            self.bodylist.insert(0,(self.bodylist[0][0]+dx,self.bodylist[0][1]+dy))
            
    #Responsible for rendering the snake        
    def renderSnake(self):
        if self.currentD=='R':
            self.headSprite=transform.rotate(self.head_image,-180)
        elif  self.currentD=='U':
            self.headSprite=transform.rotate(self.head_image,-90)
        elif  self.currentD=='D':
            self.headSprite=transform.rotate(self.head_image,90)
        else:
            self.headSprite=transform.rotate(self.head_image,0)
        self.headSprite=transform.scale(self.headSprite,(cfg.SPRITE_H,cfg.SPRITE_W))
        headRect=self.headSprite.get_rect()
        headRect.x=cfg.STAGE_X+(self.bodylist[0][0]*cfg.SPRITE_W)+cfg.STAGE_MARGIN_X
        headRect.y=cfg.STAGE_Y+(self.bodylist[0][1]*cfg.SPRITE_H)+cfg.STAGE_MARGIN_Y
        self.screen.blit(self.headSprite,headRect)
        for b in self.bodylist[1:]:
            bodyRect=self.bodySprite.get_rect()
            bodyRect.x=cfg.STAGE_X+(b[0]*cfg.SPRITE_W)+cfg.STAGE_MARGIN_X
            bodyRect.y=cfg.STAGE_Y+(b[1]*cfg.SPRITE_H)+cfg.STAGE_MARGIN_Y
            self.screen.blit(self.bodySprite,bodyRect)


