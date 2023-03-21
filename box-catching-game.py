import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Box Catching Game')

# Set the font
font = pygame.font.Font(None, 30)

# Set the colors
player_color = (255, 0, 0)
enemy_color = (0, 0, 255)

# Set the game variables
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 20
player_speed = 5
enemies = []
for i in range(5):
    enemy_size = random.randint(30, 50)
    enemy_x = random.randint(0, screen_width - enemy_size)
    enemy_y = random.randint(0, screen_height - enemy_size - player_size - 20)
    enemy_speed = random.randint(1, 5)
    enemy = {'x': enemy_x, 'y': enemy_y,
             'size': enemy_size, 'speed': enemy_speed}
    enemies.append(enemy)
score = 0

# Set the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_speed

    # Move the enemies
    for enemy in enemies:
        enemy['y'] += enemy['speed']
        if enemy['y'] > screen_height:
            enemy_size = random.randint(30, 50)
            enemy_x = random.randint(0, screen_width - enemy_size)
            enemy_y = random.randint(-screen_height, -
                                     enemy_size - player_size - 20)
            enemy_speed = random.randint(1, 5)
            enemy['x'] = enemy_x
            enemy['y'] = enemy_y
            enemy['size'] = enemy_size
            enemy['speed'] = enemy_speed

        # Check for collisions with the player
        if (player_x + player_size > enemy['x'] and player_x < enemy['x'] + enemy['size'] and
                player_y + player_size > enemy['y'] and player_y < enemy['y'] + enemy['size']):
            score += 1
            enemy_size = random.randint(30, 50)
            enemy_x = random.randint(0, screen_width - enemy_size)
            enemy_y = random.randint(-screen_height, -
                                     enemy_size - player_size - 20)
            enemy_speed = random.randint(1, 5)
            enemy['x'] = enemy_x
            enemy['y'] = enemy_y
            enemy['size'] = enemy_size
            enemy['speed'] = enemy_speed

    # Draw the player and enemies
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player_color, (player_x,
                     player_y, player_size, player_size))
    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color,
                         (enemy['x'], enemy['y'], enemy['size'], enemy['size']))

    # Draw the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Set the game clock
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit pygame
pygame.quit()
