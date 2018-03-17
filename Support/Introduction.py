import pygame
import time
import random

class Transition:
    def load(self, starting, lives):

        pygame.init()
        self.display_width = 1280
        self.display_height = 720
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.background_image = pygame.image.load("Support/g.jpg")
        self.heart_image = pygame.image.load("Support/heart.png")
        self.dude = pygame.image.load("Support/Sprites/stad.png")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))
        self.screen.blit(self.background_image, [0, 0])
        self.dude_x=0
        self.dude_y = 300
        if starting == "Exit":
            self.dude_x = 150
        elif starting == "Racing":
            self.dude_x = 450
        elif starting == "Archery":
            self.dude_x = 750
        elif starting == "Soccer":
            self.dude_x = 1050
        else:
            print ("ERRORZ")
        self.lives = lives
        self.screen.blit(self.dude, [self.dude_x, self.dude_y])
        if lives >=1:
            self.screen.blit(self.heart_image, [1100, 0])
            if lives >=2:
                self.screen.blit(self.heart_image, [1000, 0])
                if lives >= 3:
                    self.screen.blit(self.heart_image, [900, 0])


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
        pygame.display.set_caption("Transition")
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
    def main(self, endpos):
        lives = self.lives
        x =pygame.time.get_ticks()
        self.end_x = 0
        if endpos == "Exit":
            print ("Yuh")
            self.end_x = 150
        elif endpos == "Racing":
            self.end_x = 450
        elif endpos == "Archery":
            self.end_x = 750
        elif endpos == "Soccer":
            self.end_x = 1050
        self.change_x = self.end_x - self.dude_x
        self.change_x = self.change_x/250
        self.selfrunning = True
        while pygame.time.get_ticks() < x+8000 and self.selfrunning == True:
            self.screen.blit(self.background_image, [0, 0])
            self.dude_x = self.dude_x + self.change_x
            self.screen.blit(self.dude, [self.dude_x, self.dude_y])
            for event in pygame.event.get():
                self.events(event)
            if lives >= 1:
                self.screen.blit(self.heart_image, [1100, 0])
                if lives >= 2:
                    self.screen.blit(self.heart_image, [1000, 0])
                    if lives >= 3:
                        self.screen.blit(self.heart_image, [900, 0])
            pygame.display.flip()

        return x
    def events(self, event):
        if event.type == pygame.QUIT:
            self.selfrunning = False