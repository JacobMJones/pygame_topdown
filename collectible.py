import pygame

class Collectible:
    def __init__(self, x, y, image_path):
        print("Loading image from:", image_path)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.collected = False

        # Print the size of the image
        print("Image size:", self.image.get_size())

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)