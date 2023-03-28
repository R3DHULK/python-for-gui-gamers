import pygame,sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Virtual Reality Game")

# Set up the player sprite
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill((255, 0, 0))
player_rect = player_image.get_rect()
player_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Set up the enemy sprite
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
enemy_image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
enemy_image.fill((0, 0, 255))
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Move the player sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, 5)
        
    # Check for collisions between the player and the enemy
    if player_rect.colliderect(enemy_rect):
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Update the screen
    window.fill((255, 255, 255))
    window.blit(player_image, player_rect)
    window.blit(enemy_image, enemy_rect)
    pygame.display.flip()
    
    # Update the game clock
    clock.tick(60)
