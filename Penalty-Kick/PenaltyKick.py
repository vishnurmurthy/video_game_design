import pygame
import random
import time

class Game:
    def setup(self):
        #Initialize Pygame
        pygame.init()

        #Define Game colors
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.light_green = (128,240,0)
        self.dark_green = (0,100,0)
        self.red = (255, 0, 0)

        #All constants
        self.displayWidth = 1280
        self.displayHeight = 720
        self.centreX = self.displayWidth/2
        self.centreY = self.displayHeight/2
        #Frames Per Second
        self.FPS = 15
        self.Shots = 5

        #Set Game Display and Top Bar
        if pygame.display.get_surface():
            self.gameDisplay = pygame.display.get_surface()
        else:
            self.gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Penalty Kick')

        #For using the frames per second
        self.clock=pygame.time.Clock()

        #start time
        self.start_ticks = pygame.time.get_ticks()

        #Load all images
        self.skyImg = pygame.image.load('images/sky.png')
        self.audImg = pygame.image.load('images/audi.png')
        self.bannerImg = pygame.image.load('images/BANNER.png')
        self.line1Img = pygame.image.load('images/line.png')
        self.goalpostImg = pygame.image.load('images/goalpost.png')
        self.boundryImg = pygame.image.load('images/boundry.png')
        self.pointImg = pygame.image.load('images/point.png')
        self.keeperImg = pygame.image.load('images/keeper.png')
        self.sbImg = pygame.image.load('images/soccerball.png')
        self.keyImg = pygame.image.load('images/keys.png')
        #Fonts
        self.smallfont=pygame.font.SysFont("Courier",20)
        self.smallfont.set_bold(True)
        self.medfont=pygame.font.SysFont("System",50)
        self.largefont=pygame.font.SysFont("Courier", 80)
        self.largefont.set_bold(True)

        #start tick
        self.start = pygame.time.get_ticks()

    #Font Formating Function
    def text_objects(self, text, color, size):
        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        if size == "medium":
            textSurface = self.medfont.render(text, True, color)
        if size == "large":
            textSurface = self.largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    #To display message to screen
    def message_to_screen(self,msg,color,y_displace=0,size="small"):
        self.textSurf,self.textRect = self.text_objects(msg, color, size)
        self.textRect.center = (self.centreX, y_displace)
        self.gameDisplay.blit(self.textSurf,self.textRect)

    #To display the score of the teams
    def score_card(self, msg, x_place, y_place, color=(0,0,0)):
        self.screen_text = self.smallfont.render(msg, True, color)
        self.gameDisplay.blit(self.screen_text, (x_place, y_place))
       
    def keeper(self, x):
        self.imgRect = self.keeperImg.get_rect()
        self.imgRect.center = (x, 300)
        self.gameDisplay.blit(self.keeperImg, self.imgRect)

    def ball(self,x,y):
        self.gameDisplay.blit(self.sbImg, (x, y))

    def screenSetup(self):
        #set game backgroud
        self.gameDisplay.fill(self.light_green)
        #set game sky
        self.gameDisplay.blit(self.skyImg, (0, 0))
        #set Audientces
        self.gameDisplay.blit(self.audImg,(0,80))
        self.gameDisplay.blit(self.audImg, (238, 80))
        self.gameDisplay.blit(self.audImg, (476, 80))
        self.gameDisplay.blit(self.audImg, (238*3, 80))
        self.gameDisplay.blit(self.audImg, (238*4, 80))
        self.gameDisplay.blit(self.audImg, (238*5, 80))
        self.gameDisplay.blit(self.audImg, (238*6, 80))
        #set Banner
        self.gameDisplay.blit(self.bannerImg,(0,280))
        self.gameDisplay.blit(self.line1Img,(0,360))
        #set GoalPost (633X347)
        self.imgRect = self.goalpostImg.get_rect()
        self.imgRect.center = (self.centreX,193)
        self.gameDisplay.blit(self.goalpostImg, self.imgRect)
        #set the box area (800X212)
        self.imgRect = self.boundryImg.get_rect()
        self.imgRect.center = (self.centreX, 456)
        self.gameDisplay.blit(self.boundryImg, self.imgRect)
        #set penalty point
        self.gameDisplay.blit(self.pointImg, (585, 660))
        #set soccer ball
        #ball(585, 640)
        #set Keeper
        #keeper(centreX)
        #start tick
        self.start = pygame.time.get_ticks()

    def directions(self):
        self.gameDisplay.fill(self.dark_green)
        self.message_to_screen("Penalty Kicks",self.black,75,"large")
        self.gameDisplay.blit(self.keyImg, (200, 150))
        pygame.display.update()
        time.sleep(5)

    def startGame(self):

        pygame.mixer.music.load('music/time.wav')
        pygame.mixer.music.play(-1)
        self.gameExit=False
        self.gameOver=False
        self.ballSaved = False
        self.difficulty = 1

        self.goalBlocked = 0
        self.goalMissed = 0

        self.keeper_x = self.centreX
        self.keeper_x_change = 0
        self.ball_x = 585
        self.ball_y = 640
        self.ball_x_change = 0
        self.ball_y_change = 0
        self.ball_slope = random.randrange(300, 850)

        while not self.gameExit:
            #Game over, display result
            #while gameOver == True:
                #gameDisplay.fill(light_green)
                #Display Score
                #blocked = 'You Blocked ' + str(goalBlocked) + ' goals'
                #missed = 'You Missed ' + str(goalMissed) + ' goals'
                #score_card(blocked, 520, 300, black)
                #score_card(missed, 520, 350, black)
                #gameDisplay.blit(sbImg, (centreX, 200))

                #for event in pygame.event.get():
                    #if event.type == pygame.QUIT:
                        #pygame.quit()
                        #quit()
                    #if event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_ESCAPE:
                            #pygame.quit()
                            #quit()
                #pygame.display.update()
            #timer
            self.seconds = (pygame.time.get_ticks()-self.start_ticks)/1000
            if self.seconds > 25 or self.goalBlocked == 5 :
                self.gameExit = True
                return False
            self.screenSetup()
            #set
            self.blocked = 'Goals Saved: ' + str(self.goalBlocked)
            self.missed = 'Time Left: ' + str(25 - self.seconds)
            self.score_card(self.blocked, 20, 10, self.black)
            self.score_card(self.missed, 960, 10, self.black)
            pygame.display.update()

            # Game Logic
            
            # Move the keeper around
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #keeper_x -= 5
                        self.keeper_x_change = -10
                    if event.key == pygame.K_RIGHT:
                        #keeper_x += 5
                        self.keeper_x_change = 10
                    if event.key == pygame.K_ESCAPE:
                        self.gameExit = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.keeper_x_change = 0
            #set boundry for keeper
            self.keeper_x += self.keeper_x_change
            self.keeper(self.keeper_x)
            
            if self.keeper_x < 250 or self.keeper_x > 950:
                self.keeper_x_change = 0

            # End of Keeper move
            #Soccer Ball Movement
            if self.ball_y >= 325 and not self.ballSaved:
                self.ball_y_change = -10 * self.difficulty
                self.ball_x_change = ((self.ball_slope - self.ball_x)/500*self.ball_y_change)
            if self.ball_y <= 325:
                self.ball_y = 640
                self.ball_x = 585
                self.ball_y_change = 0
                self.ball_x_change = 0
                self.ball_slope = random.randrange(300, 850)
                self.goalMissed += 1
                self.ballSaved = False
            if self.ball_y <= 350:
                if (self.ball_x >= self.keeper_x and self.ball_x <= (self.keeper_x + 75)) or (self.ball_x + 50 >= self.keeper_x and self.ball_x + 50 <= (self.keeper_x + 75)):
                    self.ballSaved = True
                    self.ball_y_change = 10 * self.difficulty
                    self.ball_x_change = -((self.ball_slope - self.ball_x)/500*self.ball_y_change)
                    self.goalBlocked +=1
            if (self.ball_x + 50) <= 0 or self.ball_x >= 1200 or self.ball_y >= 700:
                self.ball_y = 640
                self.ball_x = 585
                self.ball_y_change = 0
                self.ball_x_change = 0
                self.ball_slope = random.randrange(300, 850)
                self.ballSaved = False
            self.ball_x += self.ball_x_change
            self.ball_y += self.ball_y_change
            self.ball(self.ball_x, self.ball_y)
            pygame.display.update()
            self.clock.tick(60)
            
    def main(self):
        self.directions()
        self.startGame()