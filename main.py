import pygame, os, sys
from random import randint
from pygame.locals import *

sys.path.insert(0, 'Penalty-Kick/')
sys.path.insert(0, 'Archery/')
sys.path.insert(0, 'Race_Game/')
sys.path.insert(0, 'Support/')
import PenaltyKick, Archery, car_racing, Introduction, Transition, LoseLife


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
        
        self.minigame = 1
        self.PassFail = False
        self.difficulty = 1

 
    def events(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def loop(self):
        if self.minigame == 1:#Introduction
            min4 = Transition.Intro()
            min4.load()
            x = min4.main()
            self.minigame = 2
            self.lives =3
            self.starting_position = "Exit"
            self.end_pos = "Racing"

        elif self.minigame == 2: #Transition Screen
            min5 = Introduction.Transition()
            min5.load(self.starting_position, self.lives)
            x= min5.main(self.end_pos)
            if self.end_pos == "Racing":
                self.minigame = 6
            elif self.end_pos == "Archery":
                self.minigame = 7
            elif self.end_pos == "Soccer":
                self.minigame = 8
            elif self.end_pos == "Exit":
                self.minigame = 4

        elif self.minigame == 3:  # Lost Life Screen
            mini6 = LoseLife.LoseLife()
            x= mini6.main()
            self.minigame = self.nextg
            if self.lives == 0:
                self._running = False
            else:
                self.minigame = 2


 #       elif self.minigame == 4:  # Quit Screen

  #      elif self.minigame == 5:  # Record Score Screen

        elif self.minigame == 6:  # Racing Game
            mini3 = car_racing.Racing()
            mini3.load()
            self.PassFail = mini3.main(self.difficulty)
            self.minigame = 2
            self.starting_position = "Racing"
            self.end_pos = "Archery"
            if self.PassFail == False:
                self.lives = self.lives-1
                self.nextg = 7
                self.minigame = 3


        elif self.minigame == 7:  # Archery Game
            mini2 = Archery.ArcheryGame()
            mini2.setup1()
            self.PassFail = mini2.archeryGame(self.difficulty)
            self.minigame = 2
            self.starting_position = "Archery"
            self.end_pos = "Soccer"
            if self.PassFail == False:
                self.lives = self.lives-1
                self.nextg = 8
                self.minigame = 3


        elif self.minigame == 8:  # Soccer Game
            mini1 = PenaltyKick.Game()
            mini1.setup()
            self.PassFail = mini1.main(self.difficulty)
            if self.difficulty <2:
                self.difficulty+=.5
            self.minigame = 2
            self.starting_position = "Soccer"
            self.end_pos = "Racing"
            if self.PassFail == False:
                self.lives = self.lives-1
                self.nextg =6
                self.minigame = 3


        #if not self.minigame:
        #    pygame.mixer.music.stop()
        #    self.titletext = self.myfont.render("something", False, (0, 0, 0))
        #    self._display_sfc.fill([128, 128, 255])
        #    self._display_sfc.blit(self.titletext,(self.width/2-250,self.height/2))
        #if self.minigame == 1:
        #    mini1 = PenaltyKick.Game()
        #    mini1.setup()
        #    self.minigame = mini1.main()
        #if pygame.key.get_pressed()[K_SPACE]:
        #    self.minigame = 1
        #if pygame.key.get_pressed()[K_RETURN]:
        #    self.minigame = 2
        #if pygame.key.get_pressed()[K_BACKSPACE]:
        #    self.minigame = 3
        #if self.minigame == 2:
        #    mini2 = Archery.ArcheryGame()
        #    mini2.setup1()
        #    mini2.introArchery()
        #    self.minigame = mini2.archeryGame(1)
        #if self.minigame == 3:
        #    mini3 = car_racing.Racing()
        #    mini3.load()
        #    self.minigame = mini3.main()
        
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
