pip install pygame


import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubbles Game")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Player properties
player_radius = 30
player_x = screen_width // 2
player_y = screen_height - 50

# Bubble properties
bubble_radius = 20
bubble_speed = 2
bubbles = []

def spawn_bubble():
    x = random.randint(bubble_radius, screen_width - bubble_radius)
    y = -bubble_radius
    bubbles.append((x, y))

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_radius:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_radius:
        player_x += 5

    screen.fill(white)

    # Update and draw bubbles
    for i in range(len(bubbles)-1, -1, -1):
        x, y = bubbles[i]
        y += bubble_speed
        bubbles[i] = (x, y)

        if y > screen_height + bubble_radius:
            bubbles.pop(i)
        else:
            pygame.draw.circle(screen, blue, (x, int(y)), bubble_radius)

            # Check for collision with player
            if distance(x, y, player_x, player_y) < bubble_radius + player_radius:
                bubbles.pop(i)

    # Draw player
    pygame.draw.circle(screen, blue, (player_x, player_y), player_radius)

    # Spawn new bubbles
    if random.randint(1, 100) < 2:
        spawn_bubble()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
