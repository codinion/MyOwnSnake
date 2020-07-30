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
        self.score_x=cfg.SCORE_X
        self.score_y=cfg.SCORE_Y
        self.stage_x=cfg.STAGE_X
        self.stage_y=cfg.STAGE_Y
        self.land_image=image.load(cfg.LAND_FILE)
        self.landSprite=transform.scale(self.land_image,(cfg.SPRITE_H,cfg.SPRITE_W))
        self.textFont=font.Font(cfg.FONT_FILE,cfg.FONT_SIZE)
        self.scoreText="Score : " + str(self.score)

    #Method to update/increment the score.
    def updateScore(self,delScore):
        self.score=self.score+delScore
        self.scoreText="Score : " + str(self.score)
    
    #Returns of the player has won the game or not!
    def isGameWon(self):
        if self.score == cfg.WINNING_SCORE:
            return True
        return False

    #Returns the current score of the player
    def getScore(self):
        return self.score
    
    #Responsible for rendering the GameOver screen when the player loses!
    def gameOver(self):
        self.screen.fill((0,0,0))
        gameOverFont=font.Font(cfg.FONT_FILE,cfg.GAMEOVER_FONT_SIZE)
        gameOverText="Game Over!"
        lastScoreFont=font.Font(cfg.FONT_FILE,cfg.LAST_SCORE_FONT_SIZE)
        lastScoreText="Final Score : "+str(self.score)
        gameOverSurf=gameOverFont.render(gameOverText,True,(255,255,255))
        gameOverRect=gameOverSurf.get_rect()
        gameOverRect.x=cfg.GAMEOVER_X
        gameOverRect.y=cfg.GAMEOVER_Y
        lastScoreSurf=lastScoreFont.render(lastScoreText,True,(255,255,255))
        lastScoreRect=lastScoreSurf.get_rect()
        lastScoreRect.x=cfg.LAST_SCORE_X
        lastScoreRect.y=cfg.LAST_SCORE_Y
        self.screen.blit(gameOverSurf,gameOverRect)
        self.screen.blit(lastScoreSurf,lastScoreRect)
        self.displayInstructions()

    #Responsible for rendering the GameWon screen when the player wins!
    def gameWon(self):
        self.screen.fill((0,0,0))
        gameWonFont=font.Font(cfg.FONT_FILE,cfg.GAMEWON_FONT_SIZE)
        gameWonText="You Have Won!"
        highScoreFont=font.Font(cfg.FONT_FILE,cfg.HIGH_SCORE_FONT_SIZE)
        highScoreText="High Score : "+str(self.score)
        gameWonSurf=gameWonFont.render(gameWonText,True,(255,255,255))
        gameWonRect=gameWonSurf.get_rect()
        gameWonRect.x=cfg.GAMEWON_X
        gameWonRect.y=cfg.GAMEWON_Y
        highScoreSurf=highScoreFont.render(highScoreText,True,(255,255,255))
        highScoreRect=highScoreSurf.get_rect()
        highScoreRect.x=cfg.HIGH_SCORE_X
        highScoreRect.y=cfg.HIGH_SCORE_Y
        self.screen.blit(gameWonSurf,gameWonRect)
        self.screen.blit(highScoreSurf,highScoreRect)
        self.displayInstructions()
    
    def displayInstructions(self):
        restartFont=font.Font(cfg.FONT_FILE,cfg.FONT_SIZE)
        restartText="Press R to Reset"
        quitFont=font.Font(cfg.FONT_FILE,cfg.FONT_SIZE)
        quitText="Press Q to Quit"
        restartSurf=restartFont.render(restartText,True,(255,255,255))
        quitSurf=quitFont.render(quitText,True,(255,255,255))
        restartRect=restartSurf.get_rect()
        quitRect=quitSurf.get_rect()
        restartRect.x=cfg.INST_RST_X
        restartRect.y=cfg.INST_RST_Y
        quitRect.x=cfg.INST_QT_X
        quitRect.y=cfg.INST_QT_Y
        self.screen.blit(restartSurf,restartRect)
        self.screen.blit(quitSurf,quitRect)

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
        




