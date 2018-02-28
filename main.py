import pygame, os
from random import randint
from pygame.locals import *

class RealGame:
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
        
        pygame.display.set_caption("TSA Video Game Design")
        self._display_sfc.fill([128, 128, 255])
        
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 30)
        self.titletext = self.myfont.render("something", False, (0, 0, 0))
 
    def events(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def loop(self):
        self.titletext = self.myfont.render("something", False, (0, 0, 0))
        self._display_sfc.fill([128, 128, 255])
        self._display_sfc.blit(self.titletext,(self.width/2-250,self.height/2))
        
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
    mainGame = RealGame()
    mainGame.on_execute()