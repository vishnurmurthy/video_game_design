import pygame
import random
import time

#Initialize Pygame
pygame.init()

#Define Game colors
white = (255,255,255)
black = (0,0,0)
light_green = (128,240,0)
dark_green=(0,100,0)
red = (255, 0, 0)

#All constants
displayWidth = 1200
displayHeight = 700
centreX = displayWidth/2
centreY = displayHeight/2
#Frames Per Second
FPS = 15
Shots = 5

#Set Game Display and Top Bar
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Penalty Kick')

#For using the frames per second
clock=pygame.time.Clock()

#start time
start_ticks = pygame.time.get_ticks()

#Load all images
skyImg = pygame.image.load('images/sky.png')
audImg = pygame.image.load('images/audi.png')
bannerImg = pygame.image.load('images/BANNER.png')
line1Img = pygame.image.load('images/line.png')
goalpostImg = pygame.image.load('images/goalpost.png')
boundryImg = pygame.image.load('images/boundry.png')
pointImg = pygame.image.load('images/point.png')
keeperImg = pygame.image.load('images/keeper.png')
sbImg = pygame.image.load('images/soccerball.png')
keyImg = pygame.image.load('images/keys.png')
#Fonts
smallfont=pygame.font.SysFont("Courier",20)
smallfont.set_bold(True)
medfont=pygame.font.SysFont("System",50)
largefont=pygame.font.SysFont("Courier", 80)
largefont.set_bold(True)

#start tick
start = pygame.time.get_ticks()

#Font Formating Function
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

#To display message to screen
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = (centreX, y_displace)
    gameDisplay.blit(textSurf,textRect)


#To display the score of the teams
def score_card(msg, x_place, y_place, color=black):
    screen_text = smallfont.render(msg, True, color)
    gameDisplay.blit(screen_text, (x_place, y_place))
   
def keeper(x):
    imgRect = keeperImg.get_rect()
    imgRect.center = (x, 300)
    gameDisplay.blit(keeperImg, imgRect)

def ball(x,y):
    gameDisplay.blit(sbImg, (x, y))

def screenSetup():
    #set game backgroud
    gameDisplay.fill(light_green)
    #set game sky
    gameDisplay.blit(skyImg, (0, 0))
    #set Audientces
    gameDisplay.blit(audImg,(0,80))
    gameDisplay.blit(audImg, (238, 80))
    gameDisplay.blit(audImg, (476, 80))
    gameDisplay.blit(audImg, (238*3, 80))
    gameDisplay.blit(audImg, (238*4, 80))
    gameDisplay.blit(audImg, (238*5, 80))
    gameDisplay.blit(audImg, (238*6, 80))
    #set Banner
    gameDisplay.blit(bannerImg,(0,280))
    gameDisplay.blit(line1Img,(0,360))
    #set GoalPost (633X347)
    imgRect = goalpostImg.get_rect()
    imgRect.center = (centreX,193)
    gameDisplay.blit(goalpostImg, imgRect)
    #set the box area (800X212)
    imgRect = boundryImg.get_rect()
    imgRect.center = (centreX, 456)
    gameDisplay.blit(boundryImg, imgRect)
    #set penalty point
    gameDisplay.blit(pointImg, (585, 660))
    #set soccer ball
    #ball(585, 640)
    #set Keeper
    #keeper(centreX)
    #start tick
    start = pygame.time.get_ticks()

def directions():
    gameDisplay.fill(dark_green)
    message_to_screen("Penalty Kicks",black,75,"large")
    gameDisplay.blit(keyImg, (200, 150))
    pygame.display.update()
    time.sleep(5)

def startGame():

    pygame.mixer.music.load('music/time.wav')
    pygame.mixer.music.play(-1)
    gameExit=False
    gameOver=False
    ballSaved = False
    difficulty = 1

    goalBlocked = 0
    goalMissed = 0

    keeper_x = centreX
    keeper_x_change = 0
    ball_x = 585
    ball_y = 640
    ball_x_change = 0
    ball_y_change = 0
    ball_slope = random.randrange(300, 850)

    while not gameExit:
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
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds > 25:
            gameExit = True
        if goalBlocked == 5:
            gameExit = True
        screenSetup()
        #set
        blocked = 'Goals Saved: ' + str(goalBlocked)
        missed = 'Time Left: ' + str(25 - seconds)
        score_card(blocked, 20, 10, black)
        score_card(missed, 960, 10, black)
        pygame.display.update()

        # Game Logic
        
        # Move the keeper around
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #keeper_x -= 5
                    keeper_x_change = -10
                if event.key == pygame.K_RIGHT:
                    #keeper_x += 5
                    keeper_x_change = 10
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    keeper_x_change = 0
        #set boundry for keeper
        keeper_x += keeper_x_change
        keeper(keeper_x)
        
        if keeper_x < 250 or keeper_x > 950:
            keeper_x_change = 0

        # End of Keeper move
        #Soccer Ball Movement
        if ball_y >= 325 and not ballSaved:
            ball_y_change = -10 * difficulty
            ball_x_change = ((ball_slope - ball_x)/500*ball_y_change)
        if ball_y <= 325:
            ball_y = 640
            ball_x = 585
            ball_y_change = 0
            ball_x_change = 0
            ball_slope = random.randrange(300, 850)
            goalMissed += 1
            ballSaved = False
        if ball_y <= 350:
            if (ball_x >= keeper_x and ball_x <= (keeper_x + 75)) or (ball_x + 50 >= keeper_x and ball_x + 50 <= (keeper_x + 75)):
                ballSaved = True
                ball_y_change = 10 * difficulty
                ball_x_change = -((ball_slope - ball_x)/500*ball_y_change)
                goalBlocked +=1
        if (ball_x + 50) <= 0 or ball_x >= 1200 or ball_y >= 700:
            ball_y = 640
            ball_x = 585
            ball_y_change = 0
            ball_x_change = 0
            ball_slope = random.randrange(300, 850)
            ballSaved = False
        ball_x += ball_x_change
        ball_y += ball_y_change
        ball(ball_x, ball_y)
        pygame.display.update()
        clock.tick(60)
        
#Main Game
directions()
startGame()
pygame.quit()
quit()







