import pygame, os, sys
from random import randint
from pygame.locals import *

sys.path.insert(0, 'Penalty-Kick/')
sys.path.insert(0, 'Archery/')
import PenaltyKick, Archery

class RealGame:
    def __init__(self):
        self._running = True
        self._display_sfc = None
        self.size = self.width, self.height = 1280, 720
 
    def init(self): 
        pygame.init()
        if pygame.display.get_surface():
            self._display_sfc = pygame.display.get_surface()
        else:
            self._display_sfc = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()
        
        pygame.display.set_caption("TSA Video Game Design")
        self._display_sfc.fill([128, 128, 255])
        
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 30)
        self.titletext = self.myfont.render("something", False, (0, 0, 0))
        
        self.minigame = 0
 
    def events(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def loop(self):
        if not self.minigame:
            pygame.mixer.music.stop()
            self.titletext = self.myfont.render("something", False, (0, 0, 0))
            self._display_sfc.fill([128, 128, 255])
            self._display_sfc.blit(self.titletext,(self.width/2-250,self.height/2))
        if self.minigame == 1:
            mini1 = PenaltyKick.Game()
            mini1.setup()
            self.minigame = mini1.main()
        if pygame.key.get_pressed()[K_SPACE]:
            self.minigame = 1
        if pygame.key.get_pressed()[K_RETURN]:
            self.minigame = 2
        if self.minigame == 2:
            mini2 = Archery.ArcheryGame()
            mini2.setup1()
            mini2.introArchery()
            self.minigame = mini2.archeryGame(1)
        
    def render(self):
        pygame.display.flip()
        
    def cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.init() == False:
            self._running = False
        
        while self._running:
            for event in pygame.event.get():
                self.events(event)
            self.loop()
            self.render()
        self.cleanup()

if __name__ == "__main__" :
    mainGame = RealGame()
    mainGame.on_execute()
