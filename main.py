import pygame
import sys
import random


pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

score = 0
font = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

import random

stars = []

for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    stars.append([x, y])

# Load spaceship image
ship = pygame.image.load("image/ship.png")
ship = pygame.transform.scale(ship, (100, 100))

bullet_img = pygame.image.load("image/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (20, 30))

enemy_ship = pygame.image.load("image/enemy.png")
enemy_ship = pygame.transform.scale(enemy_ship, (80, 80))

# Player
player_width = 100
player_height = 100

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height

player_speed = 5

# Bullets
bullets = []
bullet_width = 20
bullet_height = 30
bullet_speed = 8

# Enemy
enemy_width = 80
enemy_height = 80

enemies = []

for i in range(3):
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(-600, -80)

    enemies.append([enemy_x, enemy_y])
enemy_speed = 4


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
score = 0

running = True

while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y

                bullets.append([bullet_x, bullet_y])


    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player inside screen
    player_x = max(0, min(player_x, WIDTH - player_width))
    player_y = max(0, min(player_y, HEIGHT - player_height))

    # Enemy movement
    
    enemy_speed = 2.5

    for enemy in enemies:

        enemy[1] += enemy_speed

        if enemy[1] > HEIGHT:
            enemy[0] = random.randint(0, WIDTH - enemy_width)
            enemy[1] = random.randint(-300, -80)


    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed

        if bullet[1] < 0:
            bullets.remove(bullet)
            continue

        bullet_rect = pygame.Rect(
            bullet[0],
            bullet[1],
            bullet_width,
            bullet_height
        )

        for enemy in enemies:

            enemy_rect = pygame.Rect(
                enemy[0],
                enemy[1],
                enemy_width,
                enemy_height
            )

            if bullet_rect.colliderect(enemy_rect):

                if bullet in bullets:
                    bullets.remove(bullet)

                enemy[0] = random.randint(0, WIDTH - enemy_width)
                enemy[1] = random.randint(-300, -80)

                score += 10

                break


    # Draw everything

    for star in stars:
        star[1] += 1

        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0

    screen.fill(BLACK)
    for star in stars:
        pygame.draw.circle(screen, WHITE, (star[0], star[1]), 2)

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), 2)

    # Draw spaceship image
    screen.blit(ship, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

    
    # Draw score
    
    for enemy in enemies:
        screen.blit(enemy_ship, (enemy[0], enemy[1]))

    score_text = font.render(
    f"Score: {score}",
    True,
    (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()

