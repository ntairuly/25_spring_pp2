import pygame
pygame.init()#allow us to use pygame module


def border(cor,len,radius):
    if cor + radius>len:
        return len - radius
    elif cor - radius < 0:
        return radius
    else:
        return cor


width, height = 1200,700
screen = pygame.display.set_mode((width,height))#set display


speed = 20
cor_x,cor_y = width/2,height/2#coordinate of center of ball
radius =25
running = True


#allow to use fps to make the ball move smoothly
clock = pygame.time.Clock()
Fps = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #allow to get pressed keys        
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        cor_y-=speed
        cor_y=border(cor_y,height,radius)
    if pressed_keys[pygame.K_DOWN]:
        cor_y+=speed
        cor_y=border(cor_y,height,radius)
    if pressed_keys[pygame.K_RIGHT]:
        cor_x+=speed
        cor_x=border(cor_x,width,radius)
    if pressed_keys[pygame.K_LEFT]:
        cor_x-=speed
        cor_x=border(cor_x,width,radius)


    screen.fill("White")    
    ball=pygame.draw.circle(screen,"Red",(cor_x,cor_y),radius)

    pygame.display.update()
    clock.tick(Fps) 