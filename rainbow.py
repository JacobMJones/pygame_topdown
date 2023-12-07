import pygame
import random
import math

class Rainbow:
    def __init__(self, start_x, start_y, num_bands=200, speed=0.3):
        self.start_x = start_x
        self.start_y = start_y
        self.max_band_height = 15  # Maximum height of each color band
        self.num_bands = num_bands
        self.colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]  # Start with one random color
        self.current_band_height = 0
        self.growth_phase = 0  # Track the phase of the growth/shrinkage
        self.speed = speed  # Speed of the growth and shrinkage

    def generate_random_color(self):
        # Generates a color variation based on the last color or a new random color if no colors are present
        if self.colors:
            last_color = self.colors[-1]
            color_variation = 40  # The maximum change in each RGB component
            new_color = tuple(max(0, min(255, c + random.randint(-color_variation, color_variation))) for c in last_color)
        else:
            # If there are no colors, generate a completely new random color
            new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        return new_color

    def update(self, grow):
        self.growth_phase += self.speed
        self.current_band_height = self.max_band_height * (math.sin(self.growth_phase) * 0.5 + 0.5)

        if grow:
            if self.growth_phase >= math.pi:
                self.growth_phase = 0
                if len(self.colors) < self.num_bands:
                    self.colors.append(self.generate_random_color())
        else:
            if self.growth_phase >= math.pi:
                if len(self.colors) > 0:
                    self.colors.pop()
                self.growth_phase = 0

    def draw(self, screen, angle):
        angle_radians = math.radians(angle)
        
        for i, color in enumerate(self.colors):
            band_height = i * self.max_band_height
            if i == len(self.colors) - 1:
                band_height += self.current_band_height

            start_x = self.start_x + math.sin(angle_radians) * band_height
            start_y = self.start_y - math.cos(angle_radians) * band_height
            
            end_x = self.start_x + math.sin(angle_radians) * (band_height + self.max_band_height)
            end_y = self.start_y - math.cos(angle_radians) * (band_height + self.max_band_height)
            
            pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), self.max_band_height)
