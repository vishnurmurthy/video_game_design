# this is a decent template for a minigame, if you want to use it (and we probably should use something that's the same)

import pygame, os
from random import randint
from pygame.locals import *

class Game:
    def __init__(self):
        self._running = True
        self._display_sfc = None
        self.size = self.width, self.height = 640, 480
 
    def init(self): 
        pygame.init()
        if pygame.display.get_surface():
            self._display_sfc = pygame.display.get_surface()
        else:
            self._display_sfc = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        os.chdir('..')
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()
        pygame.mixer.music.load("assets\\time.wav")
        pygame.mixer.music.play()
        
        pygame.display.set_caption("TSA Video Game Design")
        self._display_sfc.fill([128, 255, 128])
        
        pygame.font.init()
        self.on = 0
        self.gauge = 1
        self.direct = 0.1
        self.myfont = pygame.font.SysFont('Arial', 30)
        self.gtext = self.myfont.render(str(self.gauge), False, (0, 0, 0))
        
        self.random = randint(25,75)
 
    def events(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def loop(self):
        if not pygame.mixer.music.get_busy():
            self._running = False
        if self.gauge >= 100 or self.gauge <= 0:
            self.direct *= -1
        if pygame.key.get_pressed()[K_SPACE]:
            self.on = 1
        if not self.on:
            self.gauge += self.direct
        self.gtext = self.myfont.render(str(int(self.gauge)), False, (0, 0, 0))
        self._display_sfc.fill([128, 255, 128])
        pygame.draw.circle(self._display_sfc, (0, 0, 0), (self.width/2,self.height/2-self.random*2), 15)
        self._display_sfc.blit(self.gtext,(0,0))
        
    def render(self):
        pygame.display.flip()
        
    def cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.init() == False:
            self._running = False
        
        while( self._running ):
            for event in pygame.event.get():
                self.events(event)
            self.loop()
            self.render()
        self.cleanup()

if __name__ == "__main__" :
    mainGame = Game()
    mainGame.on_execute()