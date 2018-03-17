import pygame
import time
import random

class LoseLife:
    def main(self):
        pygame.init()
        self.display_width = 1280
        self.display_height = 720
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.background_image = pygame.image.load("Support/skull.png")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))
        self.screen.blit(self.background_image, [0, 0])

        pygame.display.flip()
        pygame.mixer.music.load("Support/lifelost.wav")
        pygame.mixer.music.play()
        if pygame.display.get_surface():
            self.gameDisplay = pygame.display.get_surface()
        else:
            self.gameDisplay = pygame.display.set_mode((display_width, display_height),
                                                       pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Life Lost")
        x = pygame.time.get_ticks()
        while x+5000 > pygame.time.get_ticks():
            y = 5
        return True
