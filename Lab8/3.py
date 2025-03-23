import pygame
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
    form = "circle"
    
            
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                

            
                # determine if a number key was pressed
                if event.key == pygame.K_1:
                    mode = 'Red'
                elif event.key == pygame.K_2:
                    mode = 'Green'
                elif event.key == pygame.K_3:
                    mode = 'Blue'
                elif event.key == pygame.K_4:
                    mode = 'Brown'
                elif event.key == pygame.K_5:
                    mode = 'Grey'
                elif event.key == pygame.K_6:
                    mode = 'White'
                elif event.key == pygame.K_7:
                    mode = 'Purple'
                elif event.key == pygame.K_8:
                    mode = 'Orange'
                elif event.key == pygame.K_9:
                    mode = 'Yellow'
                elif event.key == pygame.K_0:
                    mode = 'Black'



                if event.key == pygame.K_UP: # UP grows radius
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN: # DOWN shrinks radius
                    radius = max(1, radius - 1)



                #CHANGE form
                if event.key == pygame.K_LEFT:
                    form = "circle"
                elif event.key == pygame.K_RIGHT:
                    form = "rectangle"


            #finds position and find is mouse moved with click or not
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing:  
                    position = event.pos
                    points = points + [position]
                    
        


        
        
        # draw all points
        i = last_point
        while i < len(points) -1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode,form)
            i += 1
            last_point+=1
            
        pygame.display.flip()
        
        clock.tick(120)

def drawLineBetween(screen, index, start, end, width, color_mode,form):
    #calculate coordinates
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    progress = 1.0  / iterations
    aprogress = 1 - progress
    x = int(aprogress * start[0] + progress * end[0])
    y = int(aprogress * start[1] + progress * end[1])
    #find which form is it and draw it
    if form == "circle":
        pygame.draw.circle(screen, color_mode, (x, y), width)
    else:
        pygame.draw.rect(screen, color_mode, (x,y,width*1.5,width*1.5))

main()
