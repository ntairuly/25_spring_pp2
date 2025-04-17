import pygame
import math
import pygame.time

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    # arguments
    radius = 15
    mode = 'blue'
    points = []
    drawing = False
    last_point=0
    form = "rectangle"
    
            
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                

            
             

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                    rect = pygame.Rect(0,0,100,100) 
                    rect1 = pygame.Rect(100,0,100,100)
                    rect2 = pygame.Rect(200, 0, 100, 100)
                    if rect.collidepoint(event.pos):  
                        mode = "Red"
                    if rect1.collidepoint(event.pos):  
                        mode = "Blue"
                    if rect2.collidepoint(event.pos):  
                        mode = "Green"

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing:  
                    position = event.pos
                    points = points + [position]
                    
        


        pygame.draw.rect(screen, "Red", (0,0,100,100))
        pygame.draw.rect(screen, "Blue", (100,0,100,100))
        pygame.draw.rect(screen, "Green", (200, 0, 100, 100))
        i = last_point
        while i < len(points) -1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode,form)
            i += 1
            last_point+=1
            
        pygame.display.flip()
        
        clock.tick(120)

def drawLineBetween(screen, index, start, end, width, color_mode,form):

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    progress = 1.0  / iterations
    aprogress = 1 - progress
    x = int(aprogress * start[0] + progress * end[0])
    y = int(aprogress * start[1] + progress * end[1])

    if form == "circle":
        pygame.draw.circle(screen, color_mode, (x, y), width)
    elif form == "rectangle":
        pygame.draw.rect(screen, color_mode, (x,y,width*1.5,width))
main()
