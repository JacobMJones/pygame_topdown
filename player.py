import pygame
import math

class Player:
    def __init__(self, screen_width, screen_height, image_path, scale_factor):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = .3
        self.angle = 0 # Rotation angle

        # Load and scale player image
        self.original_image = pygame.image.load(image_path)
        self.width, self.height = self.original_image.get_size()
        scaled_size = (int(self.width * scale_factor), int(self.height * scale_factor))
        self.original_image = pygame.transform.scale(self.original_image, scaled_size)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def handle_movement(self, joystick):
        axes = joystick.get_numaxes()
        if axes >= 2:
            # Movement with left stick
            self.x += joystick.get_axis(0) * self.speed
            self.y += joystick.get_axis(1) * self.speed
            self.check_boundaries()

        if axes >= 4:
            # Rotation with right stick
            right_stick_x = joystick.get_axis(2) * -1  # Invert the x-axis value
            right_stick_y = joystick.get_axis(3)
            threshold = 0.1
            if abs(right_stick_x) > threshold or abs(right_stick_y) > threshold:
                # Calculate the angle, adjusting it by 270 degrees to align with the image orientation
                self.angle = (math.degrees(math.atan2(-right_stick_y, right_stick_x)) + 270) % 360
            else:
                # If within the dead zone, don't change the angle
                return

    def draw(self, screen):
        # Rotate the player image around its center
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect.topleft)

    def draw(self, screen):
        # Rotate the player image around its center
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect.topleft)

    def draw(self, screen):
        # Rotate the player image around its center
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect.topleft)


    def check_boundaries(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.screen_width:
            self.x = self.screen_width
        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_height:
            self.y = self.screen_height

    def draw(self, screen):
        # Rotate the player
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect.topleft)
