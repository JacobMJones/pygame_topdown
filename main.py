import pygame
from player import Player

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Top Down Shooter")

# Initialize joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No joystick detected!")

# Create a player instance
player = Player(screen_width, screen_height, 'assets\player\player.png', 0.1)  


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    player.handle_movement(joystick)

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    player.draw(screen)

    # Update the game window
    pygame.display.update()

# Quit Pygame
pygame.quit()
