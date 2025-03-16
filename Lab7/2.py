import sys, pygame
pygame.init()


#allow to load needed music
def choice(order):
    if order == 0:
        return pygame.mixer.music.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/music/music1.mp3")
    elif order == 1:
        return pygame.mixer.music.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/music/music2.mp3")
    elif order == 2:
        return pygame.mixer.music.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/music/music3.mp3")
    elif order == 3:
        return pygame.mixer.music.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/music/music4.mp3")


screen = pygame.display.set_mode((800,600))
running = True
order = 0
changing = True#Check changes in music

#allow to use commands smoothly without repeating too many
clock = pygame.time.Clock()
Fps = 7

while running:
    if changing:
        choice(order)
        changing = False
        flag1 = True#used to check is it played firstly or not
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #allow to get pressed keys
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        if flag1:
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.unpause()#used to continue listening in paused place
            flag1 = True
    if pressed_keys[pygame.K_DOWN]:
        pygame.mixer.music.pause()
        flag1=False
    if pressed_keys[pygame.K_RIGHT]:
       if order == 3:
           order-=4
       order+=1
       changing = True
    if pressed_keys[pygame.K_LEFT]:
        if order == 0:
            order+=4 
        order-=1
        changing = True

        
    pygame.display.update()
    clock.tick(Fps) 
    print(order)