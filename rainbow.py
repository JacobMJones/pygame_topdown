import pygame
import math
class Rainbow:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.length = 0
        self.max_length = 1000
        self.width = 25
        self.color = (155, 120, 0)  # Starting color, can be changed to a rainbow gradient
        print('po')

    def update(self, grow):
        if grow and self.length < self.max_length:
            self.length += 1.5  # Increase the length of the rainbow
        else:
            self.length = max(0, self.length - 1)  # Decrease the length

    def draw(self, screen, angle):
            # Calculate the end point of the rainbow
            angle_radians = math.radians(angle)
            end_x = self.start_x + math.sin(angle_radians) * self.length
            end_y = self.start_y - math.cos(angle_radians) * self.length  # Pygame's y-coordinates increase downwards

            # Draw the rainbow
            pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (end_x, end_y), self.width)
