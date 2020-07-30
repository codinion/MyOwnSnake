"""
This file is the class file for the Food object.
Author : Abir Mukherjee (codinion/mabir)
Email : abir.mukherjee0595@gmail.com
"""

import config as cfg 
from pygame import image,transform
from random import  randrange

#Class definition representing the Food in the game.
class Food:
    #Constructor for the Food object.
    def __init__(self,scr,blist):
        self.screen=scr
        self.food_x=randrange(0,(cfg.STAGE_W//cfg.SPRITE_W))
        self.food_y=randrange(0,(cfg.STAGE_H//cfg.SPRITE_H))
        while (self.food_x,self.food_y) in blist:
            self.food_x=randrange(0,(cfg.STAGE_W//cfg.SPRITE_W))
            self.food_y=randrange(0,(cfg.STAGE_H//cfg.SPRITE_H))
        self.food_image=image.load(cfg.FOOD_FILE)
        self.foodSprite=transform.scale(self.food_image,(cfg.SPRITE_H,cfg.SPRITE_W))
    
    #Returns the (x,y) index of the Food.
    def getFoodXY(self):
        return (self.food_x,self.food_y)
    
    #Responsible for moving the food to a new location on the stage.
    def moveFood(self,blist):
        newx=randrange(0,(cfg.STAGE_W//cfg.SPRITE_W))
        newy=randrange(0,(cfg.STAGE_H//cfg.SPRITE_H))
        while newx==self.food_x or newy==self.food_y or (newx,newy) in blist:
            newx=randrange(0,(cfg.STAGE_W//cfg.SPRITE_W))
            newy=randrange(0,(cfg.STAGE_H//cfg.SPRITE_H))   
        self.food_x=newx
        self.food_y=newy
    
    #Responsible for rendering the food object.
    def renderFood(self):
        foodRect=self.foodSprite.get_rect()
        foodRect.x=cfg.STAGE_X+(self.food_x*cfg.SPRITE_W)+cfg.STAGE_MARGIN_X
        foodRect.y=cfg.STAGE_Y+(self.food_y*cfg.SPRITE_H)+cfg.STAGE_MARGIN_Y
        self.screen.blit(self.foodSprite,foodRect)

