
import pygame
import time
import random 

class Racing:
    def load(self):
        pygame.init()
        self.display_width = 1000
        self.display_height = 600

        #Defines the colors that can be used
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.red = (255,0,0)
        self.blue = (0,0,255)

        #Give fields for the dimensions of cars
        self.car_width = 50
        self.car_height = 100
        self.chicken_width = 50
        self.chicken_height = 75

        #Indicates the starting music
        pygame.mixer.music.load("Race_Game/Hurry_Up.mp3")
        if pygame.display.get_surface():
            self.gameDisplay = pygame.display.get_surface()
        else:
            self.gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("RACE CAR")
        self.clock = pygame.time.Clock()

        #Loads images of objects
        self.carImg = pygame.image.load("Race_Game/car1.png") 
        self.car2Img = pygame.image.load("Race_Game/car2.png")
        self.bgImg = pygame.image.load("Race_Game/back2.jpg")
        self.crash_img = pygame.image.load("Race_Game/crash.png")
        
        self.gg = 0


    def intro(self):
       #Intro music can start
       self.intro = True
       #timer is set to true
       self.menu1_x = 200
       self.menu1_y = 400
       self.menu2_x = 500
       self.menu2_y = 400
       self.menu_width = 200
       self.menu_height = 100
       while self.intro:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
          pygame.display.set_icon(self.carImg)
          
          pygame.draw.rect(self.gameDisplay,self.black,(200,400,100,50))
          pygame.draw.rect(self.gameDisplay,self.black,(500,400,100,50))
             
          self.gameDisplay.fill(self.white)
          self.message_display("RACE CAR",100,self.display_width/2,self.display_height/2)
           
          pygame.draw.rect(self.gameDisplay,self.green,(200,400,100,50))
          pygame.draw.rect(self.gameDisplay,self.red,(500,400,100,50))
          
          self.mouse = pygame.mouse.get_pos()
          self.click = pygame.mouse.get_pressed()
          
          
          if self.menu1_x < self.mouse[0] < self.menu1_x+self.menu_width and self.menu1_y < self.mouse[1] < self.menu1_y+self.menu_height:
             pygame.draw.rect(self.gameDisplay,self.green,(200,400,100,50))
             if self.click[0] == 1:
                self.intro = False
          if self.menu2_x < self.mouse[0] < self.menu2_x+self.menu_width and self.menu2_y < self.mouse[1] < self.menu2_y+self.menu_height:
             pygame.draw.rect(self.gameDisplay,self.green,(500,400,100,50))
             if self.click[0] == 1:
                pygame.quit()
                quit()
       
          self.message_display("Go",40,self.menu1_x+self.menu_width/2,self.menu1_y+self.menu_height/2)
          self.message_display("Exit",40,self.menu2_x+self.menu_width/2,self.menu2_y+self.menu_height/2)
          
          pygame.display.update()
          self.clock.tick(50)
          
          self.start_ticks=pygame.time.get_ticks() 
    '''
    while timer == True: # mainloop
       seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
       if seconds>30: # if more than 10 seconds close the game
          break
        #print (seconds) 
        '''
    def highscore(self,count):
       self.font = pygame.font.SysFont(None,20)
       self.text = self.font.render("Score : "+str(count),True,self.black)
       self.gameDisplay.blit(self.text,(0,0))
       
    def draw_things(self,thingx,thingy,thing):
       self.gameDisplay.blit(thing,(thingx,thingy))
       
       
    def car(self,x,y):
       self.gameDisplay.blit(self.carImg,(x,y))

    def text_objects(self,text,font):
       textSurface = self.font.render(text,True,self.black)
       return textSurface,textSurface.get_rect()
       
       
    def message_display(self,text,size,x,y):
       self.font = pygame.font.Font("freesansbold.ttf",size)
       self.text_surface , self.text_rectangle = self.text_objects(text,self.font)
       self.text_rectangle.center =(x,y)
       self.gameDisplay.blit(self.text_surface,self.text_rectangle)
       
       
    def crash(self,x,y):
       self.gameDisplay.blit(self.crash_img,(x,y))
       self.message_display("Boom Boom ****Crash****",70,600,self.display_height/2)
       pygame.display.update()
       time.sleep(2)
       self.gameExit = True
       self.gg = 1
       
    def gameloop(self, difficulty):
       pygame.mixer.music.play(-1)
       self.bg_x1 = (self.display_width/2)-(360/2)
       self.bg_x2 = (self.display_width/2)-(360/2)
       self.bg_y1 = 0
       self.bg_y2 = -600
       self.bg_speed = 6
       self.bg_speed_change = 0
       self.car_x = ((self.display_width / 2) - (self.car_width / 2))
       self.car_y = (self.display_height - self.car_height)
       self.car_x_change = 0
         
       self.road_start_x =  (self.display_width/2)-112
       self.road_end_x = (self.display_width/2)+112
       
       self.thing_startx = random.randrange(self.road_start_x,self.road_end_x-self.car_width)
       self.thing_starty = -600
       self.thingw = 50
       self.thingh = 100
       self.thing_speed = 3
       self.count=0
       self.gameExit = False
       
       while not self.gameExit:

          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                self.gameExit = True
                pygame.quit()
                quit()
             
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   self.car_x_change = -5
                elif event.key == pygame.K_RIGHT:
                   self.car_x_change = 5
                
                   
             if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   self.car_x_change = 0
             
             
          self.car_x+=self.car_x_change

          if self.car_x > self.road_end_x-self.car_width:
             self.crash(self.car_x,self.car_y)
          if self.car_x < self.road_start_x:
             self.crash(self.car_x-self.car_width,self.car_y)
          
          
          if self.car_y < self.thing_starty + self.thingh:
             if self.car_x >= self.thing_startx and self.car_x <= self.thing_startx+self.thingw:
                self.crash(self.car_x-25,self.car_y-self.car_height/2)
             if self.car_x+self.car_width >= self.thing_startx and self.car_x+self.car_width <= self.thing_startx+self.thingw:
                self.crash(self.car_x,self.car_y-self.car_height/2)

          self.gameDisplay.fill(self.green)       
          self.gameDisplay.blit(self.bgImg,(self.bg_x1,self.bg_y1))
          self.gameDisplay.blit(self.bgImg,(self.bg_x2,self.bg_y2))
          
          self.car(self.car_x,self.car_y) 
          self.draw_things(self.thing_startx,self.thing_starty,self.car2Img)
          self.highscore(self.count)
          self.count+=1
          self.thing_starty += self.thing_speed
          
          if self.thing_starty > self.display_height:
             self.thing_startx = random.randrange(self.road_start_x,self.road_end_x-self.car_width)
             self.thing_starty = -200

             
          if (self.count>2000):
             self.message_display("Time's Up! You win!",75,self.display_width/2,self.display_height/2)
             pygame.display.update()
             time.sleep(3)
             self.gameExit = True
             

             
          self.bg_y1 += self.bg_speed
          self.bg_y2 += self.bg_speed
          
          if self.bg_y1 >= self.display_height:
             self.bg_y1 = -600
             
          if self.bg_y2 >= self.display_height:
             self.bg_y2 = -600
          
          
          pygame.display.update() # helps to update the screen if the scenario arises.
          self.clock.tick(60) 
          
    def main(self, difficulty):
        self.gameloop(difficulty)
        if self.gg==1:
            return False
        return True
