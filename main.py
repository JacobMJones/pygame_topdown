##Libraries
import pygame
import pygame_gui

##Classes
from pygame_gui.elements.ui_label import UILabel
from player import Player
from collectible import Collectible


##############
# Initialize #
##############

#Constants
screen_width = 1000
screen_height = 1000

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


#Player Speed
player_speed_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((50, 50), (200, 50)), manager=manager)
player_speed_entry.set_text(str(player.speed))
player_speed_label = UILabel(relative_rect=pygame.Rect((50, 20), (200, 30)),
                             text="Player Speed:",
                             manager=manager)

#############
# Game loop #
#############

running = True
while running:
   
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():

    ##Quit program
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Pass the event to the UIManager
        manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == player_speed_entry:
                    try:
                        player.speed = float(player_speed_entry.get_text())
                    except ValueError:
                        pass  # Handle invalid input   


    # Update the UIManager
    manager.update(time_delta)

    # Handle player movement
    if joystick:
        player.handle_movement(joystick)
        player.handle_rainbow(joystick, time_delta)

    # Collision detection for collectibles
    for collectible in collectibles:
        if player.rect.colliderect(collectible.rect):
            collectible.collected = True
            # Add score increment or other effects here

    # Drawing
    screen.fill((200, 200, 250))  # Clear the screen
    player.draw(screen) # Draw Player
    for collectible in collectibles:
        collectible.draw(screen) #Draw Collectibles

    manager.draw_ui(screen)
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()