##Libraries
import pygame
import pygame_gui

##Classes
from pygame_gui.elements.ui_label import UILabel
from player import Player
from collectible import Collectible
from UIControl import UIControl

##############
# Initialize #
##############

#Constants
screen_width = 800
screen_height = 800

#Pygame
pygame.init()
screen = pygame.display.set_mode((screen_width , screen_height)) 
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Top Down Shooter")


#Joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No joystick detected!")

#Player
player = Player(screen_width, screen_height, 'assets\player\player.png', 0.1)  

#Collectibles
collectibles = [Collectible(100, 450, 'assets\collectibles\jewel.png'), 
                Collectible(100, 250, 'assets\collectibles\jewel.png')]

#Pygame_GUI
manager = pygame_gui.UIManager((screen_width, screen_height))
# Initialize UI Controls
player_speed_ui = UIControl(50, 100, 120, 50, "PSpeed:", manager, player.speed)
rainbow_speed_ui = UIControl(250, 100, 120, 50, "RSpeed:", manager, player.rainbow.speed)


# #Player Speed
# player_speed_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((50, 50), (120, 50)), manager=manager)
# player_speed_entry.set_text(str(player.speed))
# player_speed_label = UILabel(relative_rect=pygame.Rect((10, 20), (200, 100)),
#                              text="PSpeed:",
#                              manager=manager)

# rainbow_speed_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((250, 50), (120, 50)), manager=manager)
# rainbow_speed_entry.set_text(str(player.rainbow.speed))
# rainbow_speed_label = UILabel(relative_rect=pygame.Rect((10, 20), (200, 100)),
#                              text="RSpeed:",
#                              manager=manager)

#############
# Game loop #
#############

running = True
while running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        # Handle quitting the game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Pass the event to the UIManager and UIControl objects
        manager.process_events(event)
        player_speed_ui.update(event)
        rainbow_speed_ui.update(event)

    # Apply new values from the UI Controls to the player and rainbow
    player.speed = player_speed_ui.value
    player.rainbow.speed = rainbow_speed_ui.value

    # Update the UIManager
    manager.update(time_delta)

    # Handle player movement
    if joystick_count > 0:
        player.handle_movement(joystick)
        player.handle_rainbow(joystick, time_delta)

    # Collision detection for collectibles
    for collectible in collectibles:
        if player.rect.colliderect(collectible.rect):
            collectible.collected = True
            # Add score increment or other effects here

    # Drawing
    screen.fill((200, 200, 250))  # Clear the screen
    player.draw(screen)           # Draw Player
    for collectible in collectibles:
        if not collectible.collected:
            collectible.draw(screen)  # Draw Collectibles

    manager.draw_ui(screen)        # Draw UI
    pygame.display.update()        # Update the display

# Quit Pygame
pygame.quit()