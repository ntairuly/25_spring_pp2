import sys, pygame
pygame.init()
screen = pygame.display.set_mode((800,600))#set display mode


#load images
clock = pygame.image.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/images/clock.png")
min_hand = pygame.image.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/images/min_hand.png")#big one
sec_hand = pygame.image.load("C:/Users/User/Desktop/python_pp2/25_spring_pp2/Lab7/images/sec_hand.png")#small one


#main variables 
running = True
angle_sec=60
angle_min=-50
sec = 0


while running:
    screen.blit(clock,(0,0))#hides used texture under it and it is wordk like background
    

    #rotate second hand
    rotated_image1 = pygame.transform.rotate(sec_hand, angle_sec)
    rotated_image_rect1 = rotated_image1.get_rect(center = (400,300))
    #rotate minute hand
    rotated_image2 = pygame.transform.rotate(min_hand, angle_min)
    rotated_image_rect2 = rotated_image2.get_rect(center = (400,300))
    

    #collebrating angle
    if sec == 60:
        angle_min-=360/60
    sec+=1
    angle_sec-=360/60

    #give image in correct position
    screen.blit(rotated_image1, rotated_image_rect1)
    screen.blit(rotated_image2, rotated_image_rect2)
    pygame.display.flip()#update screen


    #allow to exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #waits a second        
    pygame.time.delay(1000)