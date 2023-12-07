import pygame
from player import Player
from collectible import Collectible
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

collectibles = [Collectible(100, 450, 'assets\collectibles\jewel.png'), 
                Collectible(100, 250, 'assets\collectibles\jewel.png')
               ]
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    if joystick:
        player.handle_movement(joystick)

    # Collision detection for collectibles
    for collectible in collectibles:
        if player.rect.colliderect(collectible.rect):
            collectible.collected = True
            # Add score increment or other effects here

    # Drawing
    screen.fill((0, 128, 255))  # Clear the screen
    player.draw(screen)
    for collectible in collectibles:
        collectible.draw(screen)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()