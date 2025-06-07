import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 20, 40
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Shooter")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR_LIST = [(255, 0, 0), (0, 200, 0), (0, 0, 255), (255, 255, 0)]

rows = []
tank_x = WIDTH // 2
tank_speed = CELL_WIDTH
bullets = []
bullet_speed = 12
row_timer = pygame.time.get_ticks()
last_shot_time = 0
shoot_delay = 100
game_over = False
running = True

def draw_tank(x):
    base_y = HEIGHT - CELL_HEIGHT
    pygame.draw.rect(screen, WHITE, (x, base_y, CELL_WIDTH, CELL_HEIGHT))
    pygame.draw.rect(screen, WHITE, (x + CELL_WIDTH // 2 - 3, base_y - 12, 6, 12))

def create_row():
    new_row = [0] * COLS
    count = random.randint(3, 10)
    indices = random.sample(range(COLS), count)
    for i in indices:
        new_row[i] = random.choice(COLOR_LIST)
    rows.insert(0, new_row)

def draw_blocks():
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

def draw_bullets():
    for b in bullets:
        pygame.draw.rect(screen, WHITE, (b[0], b[1], 4, 10))

while running:
    screen.fill(BLACK)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tank_x -= tank_speed
            tank_x = max(0, tank_x)
        if keys[pygame.K_RIGHT]:
            tank_x += tank_speed
            tank_x = min(WIDTH - CELL_WIDTH, tank_x)

        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and now - last_shot_time > shoot_delay:
            bullets.append([tank_x + CELL_WIDTH // 2, HEIGHT - CELL_HEIGHT - 15])
            last_shot_time = now

        if pygame.time.get_ticks() - row_timer > 1000:
            create_row()
            row_timer = pygame.time.get_ticks()

        for b in bullets[:]:
            b[1] -= bullet_speed
            if b[1] < 0:
                bullets.remove(b)

        for b in bullets[:]:
            col = b[0] // CELL_WIDTH
            row = b[1] // CELL_HEIGHT
            if 0 <= row < len(rows) and rows[row][col]:
                rows[row][col] = 0
                if b in bullets:
                    bullets.remove(b)

        if len(rows) > ROWS:
            game_over = True

        draw_blocks()
        draw_tank(tank_x)
        draw_bullets()

    else:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()