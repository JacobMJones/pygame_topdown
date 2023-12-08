import pygame
import random
import math

class Rainbow:
    def __init__(self, start_x, start_y, num_bands=300, band_width=20, band_height=2, speed=3000):
        self.start_x = start_x
        self.start_y = start_y
        self.band_width = band_width  # Width of each color band
        self.band_height = band_height  # Height of each color band
        self.band_heights = [] 
        self.num_bands = num_bands
        self.colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]  # Start with one random color
        self.current_band_height = 0
        self.growth_phase = 0  # Track the phase of the growth/shrinkage
        self.speed = speed  # Speed of the growth and shrinkage
        self.white_speed = 8

    def update(self, grow, time_delta):
        if grow:
            # Check if starting from zero bands, generate a completely new random color
            if len(self.band_heights) == 0:
                new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.colors = [new_color]

            # Add a new color band based on the last color if needed
            if len(self.band_heights) < self.num_bands:
                if len(self.band_heights) == 0 or self.band_heights[-1] >= self.band_height:
                    new_color = self.generate_random_color_based_on_last()
                    self.colors.append(new_color)
                    self.band_heights.append(0)

            # Grow the current band
            for i in range(len(self.band_heights)):
                if self.band_heights[i] < self.band_height:
                    self.band_heights[i] += self.speed * time_delta
                    break
        else:
            # Shrink the last band and remove it if its height is zero
            if len(self.band_heights) > 0:
                last_band_index = len(self.band_heights) - 1
                self.band_heights[last_band_index] -= self.speed * time_delta
                if self.band_heights[last_band_index] <= 0:
                    self.band_heights.pop()
                    self.colors.pop()

    def generate_random_color_based_on_last(self):
        color_variation = 15  # The maximum change in each RGB component for more variation
        if self.colors:
            # Generate a new color based on the last color with some variation
            last_color = self.colors[-1]
            new_color = tuple(

                max(0, min(255, c + random.randint(-color_variation, color_variation)+self.white_speed))
                for c in last_color
            )
        else:
            # If there are no colors, generate a completely new random color
            new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        return new_color

    def draw(self, screen, angle):
        angle_radians = math.radians(angle)
        for i in range(len(self.colors)):
            if i < len(self.band_heights):  # Check if the index is valid for both lists
                band_position = sum(self.band_heights[:i])
                start_x = self.start_x + math.sin(angle_radians) * band_position
                start_y = self.start_y - math.cos(angle_radians) * band_position

                end_x = self.start_x + math.sin(angle_radians) * (band_position + self.band_heights[i])
                end_y = self.start_y - math.cos(angle_radians) * (band_position + self.band_heights[i])

                pygame.draw.line(screen, self.colors[i], (start_x, start_y), (end_x, end_y), self.band_width)
