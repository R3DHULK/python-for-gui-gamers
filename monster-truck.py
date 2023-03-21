import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions and title
window_width = 800
window_height = 600
window_title = 'Bike Racing Game'

# Set colors
background_color = (120, 120, 120)
bike_color = (255, 255, 255)
obstacle_color = (255, 0, 0)

# Set game variables
bike_width = 50
bike_height = 80
bike_speed = 5
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 7
score = 0

# Set up the window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

# Load the font
font = pygame.font.SysFont(None, 40)

# Define the bike class


class Bike:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, bike_color,
                         (self.x, self.y, bike_width, bike_height))

    def move_left(self):
        if self.x > 0:
            self.x -= bike_speed

    def move_right(self):
        if self.x < window_width - bike_width:
            self.x += bike_speed

# Define the obstacle class


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, obstacle_color,
                         (self.x, self.y, obstacle_width, obstacle_height))

    def move(self):
        self.y += obstacle_speed


# Create the bike object
bike = Bike(window_width // 2 - bike_width //
            2, window_height - bike_height - 20)

# Create a list of obstacles
obstacles = []

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bike.move_left()
            elif event.key == pygame.K_RIGHT:
                bike.move_right()

    # Draw the background
    screen.fill(background_color)

    # Draw the bike
    bike.draw()

    # Add a new obstacle every 40 frames
    if random.randrange(0, 40) == 0:
        new_obstacle = Obstacle(random.randrange(
            0, window_width - obstacle_width), 0)
        obstacles.append(new_obstacle)

    # Move the obstacles and remove them if they go off the screen
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()
        if obstacle.y > window_height:
            obstacles.remove(obstacle)

    # Check for collisions with the obstacles
    for obstacle in obstacles:
        if bike.x < obstacle.x + obstacle_width and bike.x + bike_width > obstacle.x and bike.y < obstacle.y + obstacle_height and bike.y + bike_height > obstacle.y:
            game_over = True

    # Display the score
    score_text = font.render('Score: {}'.format(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(60)

    # Increment the score
    score += 1

# Game over, display the final score
final_score_text = font.render(
    'Final Score: {}'.format(score), True, (255, 255, 255))
screen.blit(final_score_text, (window_width //
            2 - 100, window_height // 2 - 15))
pygame.display.update()

# Wait for a key press to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            quit()
