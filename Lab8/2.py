import pygame
from color_palette import *
import random

pygame.init()

#arguments
WIDTH = 600
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
HEIGHT = 600
font_small = pygame.font.SysFont("Verdana", 20)
CELL = 30

# draw gird or in russian(сетка)
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

#classes or "objects"
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    #draws snake in cell form or transforme it to cell format
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    #help to create 
    def check_collision(self, food):
        global food_count,level,FPS
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            global food_count, level, FPS
            head = self.body[0]
            if head.x == food.pos.x and head.y == food.pos.y:
                print("Got food!")
                food_count += 1
                self.body.append(Point(head.x, head.y))
                food.generate_random_pos(self.body)
            #level
            if food_count%5 == 0 and food_count != 0 and level == food_count/5:
                level +=1
                FPS +=0.5


class Food:
    def __init__(self):
        self.pos = Point(9, 9)
    
    #draws food in cell form or transforme it to cell format
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            # check if the generated position overlaps with the snake's body
            if all(segment.x != self.pos.x or segment.y != self.pos.y for segment in snake_body):
                break

FPS = 5
clock = pygame.time.Clock()

food_count = 0
level = 1
food = Food()
snake = Snake()

running = True
while running:
    dead = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #find where are you want to go
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)
    # uses previous functions
    draw_grid()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    
    #give us level and score in screen
    level_appear = font_small.render("Level:"+str(level), True, colorGREEN)
    score_appear = font_small.render("Score:"+str(food_count), True, colorGREEN)
    
    
    screen.blit(level_appear, (10,610))
    screen.blit(score_appear, (300,610))
    
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.quit()