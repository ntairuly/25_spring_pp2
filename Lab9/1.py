#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

background_music = pygame.mixer.music.load(r'C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\Sound\background.wav')
pygame.mixer.music.play(-1) 

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\image\AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\image\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#new object named "coin"
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image_origin = pygame.transform.scale(pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\image\coin.png"),(50,50))
        self.image1 = pygame.transform.scale(pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab9\image\1.png"),(50,50))
        self.image2 = pygame.transform.scale(pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab9\image\2.png"),(50,50))
        self.image3 = pygame.transform.scale(pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab9\image\3.png"),(50,50))
        self.image = self.image_origin.copy()
        
        a = (random.randint(40,SCREEN_WIDTH-40), SCREEN_HEIGHT-80)
        self.number_choice = 1

 
        self.image.blit(self.image1,(0,0))
        self.number_choice = random.randint(1,3)
        self.rect = self.image.get_rect()
        self.rect.center = a
        self.INC_SPEED = 10
        
        


      def move(self):
        global COIN_SCORE,P1,coins,SPEED
        #if player touches coin, it change coin position and give him point
        if pygame.sprite.spritecollideany(P1, coins):   
            self.image = self.image_origin.copy()
            a = (random.randint(40,SCREEN_WIDTH-40), SCREEN_HEIGHT-80) 
            print(self.number_choice)


            #find how many points, you will get
            if self.number_choice == 1:
                COIN_SCORE +=1  
            elif self.number_choice == 2:
                COIN_SCORE +=2
            else:
                COIN_SCORE +=3

            #INCREASE SPEED
            if COIN_SCORE>=self.INC_SPEED:
                self.INC_SPEED += 10
                SPEED+=0.5 


            self.number_choice = random.randint(1,3)

            #fusion the image
            if self.number_choice == 1:
                self.image.blit(self.image1,(0,0))
            elif self.number_choice == 2:
                self.image.blit(self.image2,(0,0))
            else:
                self.image.blit(self.image3,(0,0))
            
            
            self.rect = self.image.get_rect()
            self.rect.center = a



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\image\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)



#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    scores1 = font_small.render(str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores1, (SCREEN_WIDTH-30,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    

     

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'C:\Users\User\Desktop\python_pp2\25_spring_pp2\Lab8\Sound\crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
              entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)