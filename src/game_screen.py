import pygame

pygame.init()

window_size = 300
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Tic-Tac-Toe")
WHITE = (255, 255, 255)
BLACK = (0,0,0)
line_thickness = 2
def draw_board():
    window.fill(WHITE)

    pygame.draw.line(window, BLACK, (window_size // 3, 0), (window_size // 3, window_size), line_thickness)
    pygame.draw.line(window, BLACK, (window_size // 3 * 2, 0), (window_size // 3 * 2, window_size), line_thickness)

    # Horizontal lines
    pygame.draw.line(window, BLACK, (0, window_size // 3), (window_size, window_size // 3), line_thickness)
    pygame.draw.line(window, BLACK, (0, window_size // 3 * 2), (window_size, window_size // 3 * 2), line_thickness)

# Main game loop