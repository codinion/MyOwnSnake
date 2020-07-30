"""
This file contains the SoundManager class which is responsible for handling the sound effects.
Author : Abir Mukherjee (codinion/mabir)
Email : abir.mukherjee0595@gmail.com
"""
import config as cfg 
from pygame.mixer import music,Sound,init,quit,pre_init

#Class definition of SoundManager object.
class SoundManager:
    #Constructor for SoundManager. Loads the music assets.
    def __init__(self):
        pre_init(22050, -16, 2, 1024)
        init()
        quit()
        init(22050, -16, 2, 1024)
        music.load(cfg.MUSIC_FILE)
        self.eatSfx=Sound(cfg.EAT_SFX_FILE)
        self.collideSfx=Sound(cfg.COLLIDE_SFX_FILE)
        self.winSfx=Sound(cfg.WIN_SFX_FILE)
    
    #Plays the background music.
    def playBackground(self):
        music.play()
    
    #Stops the background music.
    def stopBackground(self):
        music.stop()

    #Generates the eating SFX.
    def playEat(self):
        self.eatSfx.play()
    
    #Generates the collision SFX.
    def playCollide(self):
        self.collideSfx.play()

    #Generates the winning cheer SFX.
    def playWinning(self):
        self.winSfx.play()
