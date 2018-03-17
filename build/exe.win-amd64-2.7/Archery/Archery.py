import pygame
import math
import random

class ArcheryGame:

    def setup1(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.xScreen = 1280
        self.yScreen = 720
        if pygame.display.get_surface():
            self.gameDisplay = pygame.display.get_surface()
        else:
            self.gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Archery')
        self.bg = pygame.image.load("Archery/Forest_background.jpg")#https://pixabay.com/en/wood-tree-forest-pine-forest-3107139/
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 35)

    def archeryGame(self, difficulty):    #difficulties: 1, 1.5, 2
        self.begintime1 = pygame.time.get_ticks()
        self.gameActive = True
        pygame.mouse.set_visible(True)
        self.score = 0
        self.textsurface3 = self.myfont.render('Score:  ' + str(self.score), True, (0, 0, 0))
        self.myfont.set_bold(True)
        self.gameDisplay.blit(self.textsurface3, (0, 600))
        self.gameDisplay.blit(self.bg, (0, 0))
        #if difficulty==1:
        #    self.introArchery()
        self.myfont.set_underline(True)
        self.gameDisplay.blit(self.bg, (0, 0))
        self.hasTarget = False
        self.targetX = 0 #top left corner of target
        self.targetY = 0
        self.centerX = 0 #center of target
        self.centerY = 0
        self.hit = False
        self.score = 0
        pygame.mixer.init()
        pygame.mixer.set_num_channels(10)
        pygame.mixer.music.load("Archery/Background_Music.mp3")
        pygame.mixer.music.play()                  #http://freemusicarchive.org/music/A_A_Aalto/Bright_Corners/Balloons_Rising
        while self.gameActive:#35000
            pygame.display.update()
            if self.hasTarget == False:
                self.ran = random.random() #must be below or equal to 0.0003
                if self.ran <= 0.003: #every 2 seconds                                      creates Target
                    self.targetImg = pygame.image.load("Archery/archery_target.png")#https://pixabay.com/en/archery-games-olympics-target-aim-152912/
                    self.targetImg = pygame.transform.scale(self.targetImg, (150, 150))
                    self.targetX = random.randint(0, self.xScreen-150)
                    self.targetY = random.randint(0, self.yScreen-100)
                    self.centerX = self.targetX + 75
                    self.centerY = self.targetY + 75
                    self.gameDisplay.blit(self.targetImg, (self.targetX, self.targetY))
                    self.hasTarget = True
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.gameActive=False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.pos = pygame.mouse.get_pos()
                    self.dist = int(math.hypot(self.centerX - self.pos[0], self.centerY - self.pos[1])) #distance between shot and center
                    if(self.dist < 75): #if it makes it
                        self.scoreDist = 76 - self.dist #points from shot
                        self.score = self.score + self.scoreDist
                        self.hasTarget = False
                        self.gameDisplay.blit(self.bg, (0, 0))
            self.textsurface3 = self.myfont.render('Score:  ' + str(self.score), True, (0, 0, 0))
            self.gameDisplay.blit(self.textsurface3, (1050, 0))
            if pygame.time.get_ticks() > self.begintime1 +35000:
                self.gameActive = False
        pygame.mixer.music.stop()
        if difficulty==1:#easy
            if self.score > 750:
                return True #passed
            else:
                return False #failed
        if difficulty == 1.5:#medium
            if self.score > 900:
                return True
            else:
                return False
        if difficulty == 2:#hard
            if self.score > 1000:
                return True
            else:
                return False
        return False


    def introArchery(self):
        self.time = pygame.time.get_ticks()
        self.textsurface1 = self.myfont.render('You are in an archery Competition!', True, (0, 0, 0))
        self.textsurface2 = self.myfont.render('Hit the center of the target to get the most points!', True, (0, 0, 0))
        self.gameDisplay.blit(self.textsurface1, (250, 300))
        pygame.display.update()
        self.boo = False
        while pygame.time.get_ticks() < self.time+5000:
            self.time = pygame.time.get_ticks()
            if self.boo == False and pygame.time.get_ticks() >self.time+2500:
                self.gameDisplay.blit(self.textsurface2, (0, 400))
                pygame.display.update()
                self.boo = True
