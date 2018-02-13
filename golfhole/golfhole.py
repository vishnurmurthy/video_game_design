# this is a decent template for a minigame, if you want to use it (and we probably should use something that's the same)

import pygame, os
from pygame.locals import *

class Game:
    def __init__(self):
        self._running = True
        self._display_sfc = None
        self.size = self.weight, self.height = 640, 480
 
    def init(self):
        pygame.init()
        self._display_sfc = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        os.chdir('..')
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()
        pygame.mixer.music.load("assets\\time.wav")
        pygame.mixer.music.play()
        
        pygame.display.set_caption("TSA Video Game Design")
        self._display_sfc.fill([255, 255, 255])
 
    def events(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def loop(self):
        if not pygame.mixer.music.get_busy():
            self._running = False
        
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