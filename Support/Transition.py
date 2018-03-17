import pygame
import time
import random

class Intro:
    def load(self):

        pygame.init()
        self.display_width = 1280
        self.display_height = 720
        screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.background_image = pygame.image.load("Support/g.jpg")
        self.heart_image = pygame.image.load("Support/heart.png")
        self.dude = pygame.image.load("Support/Sprites/stad.png")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))
        screen.blit(self.background_image, [0, 0])
        screen.blit(self.dude, [100, 300])
        screen.blit(self.heart_image, [1100, 0])
        screen.blit(self.heart_image, [1000, 0])
        screen.blit(self.heart_image, [900, 0])

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('In this triathlon game you play one of three sports until you lose all your lives!', False, (0, 0, 0))
        screen.blit(textsurface, (100, 600))

        pygame.display.flip()

        # Defines the colors that can be used
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        # Indicates the starting music
        pygame.mixer.music.load("Support/ambiance.mp3")
        pygame.mixer.music.play()
        if pygame.display.get_surface():
            self.gameDisplay = pygame.display.get_surface()
        else:
            self.gameDisplay = pygame.display.set_mode((display_width, display_height),
                                                       pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Beggining")
        self.clock = pygame.time.Clock()

#    def intro(self):
 #       # Intro music can start
#        self.intro = True
        # timer is set to true
#        while self.intro:
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    pygame.quit()
#                    quit()
#            pygame.display.update()
#            self.clock.tick(50)
#            self.start_ticks = pygame.time.get_ticks()
    def main(self):
        x =pygame.time.get_ticks()
        self.selfrunning = True
        while x < 15000 and self.selfrunning == True:
            x= pygame.time.get_ticks()
            for event in pygame.event.get():
                self.events(event)
        return x
    def events(self, event):
        if event.type == pygame.QUIT:
            self.selfrunning = False
