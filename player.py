import pygame
import math
from rainbow import Rainbow

class Player:
    def __init__(self, screen_width, screen_height, image_path, scale_factor):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5
        self.angle = 0 # Rotation angle
        self.rainbow = Rainbow(self.x, self.y)
        self.scale_factor = scale_factor
        # Load and scale player image
        self.original_image = pygame.image.load(image_path)
        self.width, self.height = self.original_image.get_size()
        scaled_size = (int(self.width * scale_factor), int(self.height * scale_factor))
        self.original_image = pygame.transform.scale(self.original_image, scaled_size)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.x, self.y))


    def handle_rainbow(self, joystick, time_delta):

        # Get the value of the right trigger
        trigger_value = joystick.get_axis(5)  # Adjust the axis number as needed

        # Normalize the trigger value
        normalized_trigger_value = max(0, trigger_value)

        # Calculate the top center point of the player at its current scale
        # We use the scaled height to determine the position
        top_center_x = 0  # The top center x relative to the player's center is 0 because it's in the middle
        top_center_y = -self.height * self.scale_factor / 2  # Negative because we're going up from the center

        # Rotate this point around the player's center by the player's current rotation angle
        angle_radians = math.radians(self.angle)
        rotated_top_center_x = top_center_x * math.cos(angle_radians) - top_center_y * math.sin(angle_radians)
        rotated_top_center_y = top_center_x * math.sin(angle_radians) + top_center_y * math.cos(angle_radians)

        # Update the starting position of the rainbow
        self.rainbow.start_x = self.x + rotated_top_center_x
        self.rainbow.start_y = self.y + rotated_top_center_y

        # Update rainbow based on trigger value
        if normalized_trigger_value > 0.1:  # Adjust threshold as needed
            self.rainbow.update(True, time_delta)
        else:
            self.rainbow.update(False, time_delta)



            
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
            
    #checks for screen edge
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
        
        # Draw the rainbow with the player's angle
        self.rainbow.draw(screen, self.angle)