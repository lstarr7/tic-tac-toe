import pygame

class TextRenderer:
    def __init__(self, font_path=None, font_size=36, font_color=(255, 255, 255)):
        self.font = pygame.font.Font(font_path, font_size)
        self.font_color = font_color

    def render_text(self, text, antialias=True):
        return self.font.render(text, antialias, self.font_color)

    def draw_text(self, screen, text, position):
        text_surface = self.render_text(text)
        screen.blit(text_surface, position)
