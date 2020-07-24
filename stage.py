"""
This file is responsible for creating the stage and initializing the score.
Author : Abir Mukherjee (codinion/mabir)
Email : abir.mukherjee0595@gmail.com
"""
import config as cfg 
from pygame import image,transform,font

#Class for the Stage component. 
class Stage:
    #Constructor for initializing the stage.
    def __init__(self,scr):
        self.score=0
        self.screen=scr
        self.numCols=cfg.STAGE_W//cfg.SPRITE_W
        self.numRows=cfg.STAGE_H//cfg.SPRITE_H
        self.score_x=1
        self.score_y=1
        self.stage_x=5
        self.stage_y=cfg.SCORE_H
        self.land_image=image.load(cfg.LAND_FILE)
        self.landSprite=transform.scale(self.land_image,(cfg.SPRITE_H,cfg.SPRITE_W))
        self.textFont=font.Font(cfg.FONT_FILE,cfg.FONT_SIZE)
        self.scoreText="Score : " + str(self.score)

    #Method to update/increment the score.
    def updateScore(self,delScore):
        self.score=self.score+delScore
        self.scoreText="Score : " + str(self.score)
        
    #Method to blit the updated stage
    def refreshStage(self):
        text=self.textFont.render(self.scoreText,True,(255,255,255))
        textRect=text.get_rect()
        textRect.x=self.score_x
        textRect.y=self.score_y
        self.screen.blit(text,textRect)
        for rowIdx in range(self.numRows):
            for colIdx in range(self.numCols):
                # landUnit=self.landSprite.copy()
                landRect=self.landSprite.get_rect()
                landRect.x=self.stage_x+(colIdx*cfg.SPRITE_W)+cfg.STAGE_MARGIN_X
                landRect.y=self.stage_y+(rowIdx*cfg.SPRITE_H)+cfg.STAGE_MARGIN_Y
                landRect.w=cfg.SPRITE_W
                landRect.h=cfg.SPRITE_H
                self.screen.blit(self.landSprite,landRect)
        




