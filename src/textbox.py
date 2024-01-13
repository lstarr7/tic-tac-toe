import pygame

class TextBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('dodgerblue2')
        self.text = ''
        self.font = font
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Activate the box if the user clicked on it
            self.active = self.rect.collidepoint(event.pos)
            self.color = pygame.Color('lightskyblue3') if self.active else pygame.Color('dodgerblue2')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Or do something else with the text
                    self.text = ''  # Reset the text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        # Render the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        # Resize the box if the text is too long
        width = max(200, text_surface.get_width()+10)
        self.rect.w = width
        # Blit the text
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)
