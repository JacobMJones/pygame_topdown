import pygame
import pygame_gui

class UIControl:
    def __init__(self, x, y, width, height, text, manager, initial_value):
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x, y - 30), (width, height)),
            text=text,
            manager=manager
        )

        self.text_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x, y), (width, height)),
            manager=manager
        )
        self.text_entry.set_text(str(initial_value))

        self.value = initial_value

    def update(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == self.text_entry:
                    try:
                        self.value = float(self.text_entry.get_text())
                    except ValueError:
                        pass  # Handle invalid input

    def draw(self, screen):
        # Drawing is handled by the pygame_gui manager
        pass
