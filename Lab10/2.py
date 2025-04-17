import pygame
import random
import json
import psycopg2
import psycopg2.extras
from color_palette import *

pygame.init()

# Global game parameters
CELL = 30
WIDTH = 300
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_small = pygame.font.SysFont("Verdana", 20)
font_large = pygame.font.SysFont("Verdana", 30)
clock = pygame.time.Clock()
FPS = 5

food_count = 0
level = 1 

def init_db(conn):

    #Create the users and user_score tables if they do not exist.
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            current_level INTEGER DEFAULT 1
        );
    """)
    

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER,
            game_state TEXT,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()

def get_or_create_user(conn, username):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user is None:
        cur.execute(
            "INSERT INTO users (username, current_level) VALUES (%s, %s) RETURNING *;",
            (username, 1)
        )
        conn.commit()
        user = cur.fetchone()
    cur.close()
    return user

def update_user_level(conn, user_id, new_level):
    cur = conn.cursor()
    cur.execute("UPDATE users SET current_level = %s WHERE id = %s;", (new_level, user_id))
    conn.commit()
    cur.close()

def save_game_state(conn, user_id, level, score, snake, food, red_zones):
    state = {
        "snake": {
            "body": [(segment.x, segment.y) for segment in snake.body],
            "dx": snake.dx,
            "dy": snake.dy
        },
        "food": {
            "pos": (food.pos.x, food.pos.y)
        },
        "red_zones": [(zone.x, zone.y) for zone in red_zones] if red_zones else []
    }
    state_json = json.dumps(state)
    
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_score (user_id, score, game_state) VALUES (%s, %s, %s);", 
        (user_id, score, state_json)
    )
    conn.commit()
    cur.close()
    print("Game state saved to database.")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

def draw_grid():
    # Draw grid lines based on current WIDTH and HEIGHT
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (j * CELL, i * CELL, CELL, CELL), 1)

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self, level):
        # Shift the snake's segments from tail to head.
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Update head position based on the current direction.
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if level == 1:
            # Level 1: wrapping board behavior.
            if self.body[0].x >= WIDTH // CELL:
                self.body[0].x = 0
            if self.body[0].x < 0:
                self.body[0].x = WIDTH // CELL - 1
            if self.body[0].y >= HEIGHT // CELL:
                self.body[0].y = 0
            if self.body[0].y < 0:
                self.body[0].y = HEIGHT // CELL - 1
            return False  # snake remains alive.
        else:
            # Levels 2 and 3: snake dies on wall collision.
            if (self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or
                self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL):
                return True  # collision with wall.
            # Check self-collision.
            for segment in self.body[1:]:
                if self.body[0].x == segment.x and self.body[0].y == segment.y:
                    return True  # snake collides with its body.
            return False  # snake remains alive.

    def draw(self):
        # Draw the head.
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # Draw the rest of the body.
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global food_count
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            food_count += 1
            # Append a new segment at the tail’s position.
            tail = self.body[-1]
            self.body.append(Point(tail.x, tail.y))
            food.generate_random_pos(self.body)
            return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            # Ensure food will not spawn on the snake.
            if all(segment.x != self.pos.x or segment.y != self.pos.y for segment in snake_body):
                break
try:
    # Updated connection parameters.
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        host="localhost",
        password="Baton2018",
        port=5432
    )
except Exception as e:
    print("Failed to connect to the database:", e)
    exit(1)

init_db(conn)

username = input("Enter your username: ").strip()
user = get_or_create_user(conn, username)
user_id = user["id"]
level = user["current_level"]
print(f"Welcome {username}! Current level: {level}")
red_zones = []
if level >= 2:
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    if level == 2:
        FPS = 7
    elif level == 3:
        FPS = 10
        # Prepare red zones for level 3.
        for i in range(8, 12):
            for j in range(8, 12):
                red_zones.append(Point(i, j))
food = Food()
snake = Snake()

# Set an event to teleport the food randomly every 10 seconds.
CHANGE_POS = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_POS, 10000)

# Set immortality until time (3 seconds from start)
immortal_until = pygame.time.get_ticks() + 3000

running = True
while running:
    dead = False
    for event in pygame.event.get():
        if event.type == CHANGE_POS:
            food.generate_random_pos(snake.body)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Pause and save state if 'P' is pressed.
            if event.key == pygame.K_p:
                save_game_state(conn, user_id, level, food_count, snake, food, red_zones)
                # Enter pause loop.
                paused = True
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_p:
                            paused = False
                    pause_text = font_small.render("Paused. Press P to resume", True, colorWHITE)
                    screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, 
                                              HEIGHT // 2 - pause_text.get_height() // 2))
                    pygame.display.flip()
                    clock.tick(5)
                # When resuming, reapply immortality (3 seconds).
                immortal_until = pygame.time.get_ticks() + 3000
            # Prevent moves in the opposite direction.
            elif event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBLACK)
    draw_grid()

    # Move the snake for the current level.
    dead = snake.move(level)

    # For level 3, check for collision with red zones.
    if level == 3:
        for zone in red_zones:
            if snake.body[0].x == zone.x and snake.body[0].y == zone.y:
                dead = True
                break

    # Check if immortality is still active.
    current_time = pygame.time.get_ticks()
    immortality_active = current_time < immortal_until
    if immortality_active:
        # Ignore death during the immortality period.
        dead = False
        immortal_text = font_small.render("IMMORTAL", True, colorWHITE)
        screen.blit(immortal_text, (10, 10))

    if dead:
        print("Game Over!")
        running = False

    # Check collision with food.
    snake.check_collision(food)

    # Level transitions.
    if level == 1 and food_count >= 3:
        level = 2
        WIDTH, HEIGHT = 600, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        FPS = 7
        print("Transition to Level 2!")
        update_user_level(conn, user_id, level)
    
    if level == 2 and food_count >= 10:
        level = 3
        FPS = 10
        print("Transition to Level 3!")
        update_user_level(conn, user_id, level)
        red_zones = []
        for i in range(8, 12):
            for j in range(8, 12):
                red_zones.append(Point(i, j))

    snake.draw()
    food.draw()

    # Draw red zones if in level 3.
    if level == 3:
        for zone in red_zones:
            pygame.draw.rect(screen, colorRED, (zone.x * CELL, zone.y * CELL, CELL, CELL))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
conn.close()