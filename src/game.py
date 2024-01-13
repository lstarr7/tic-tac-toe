import pygame
from .player import Player
from .board import Board
from .textbox import TextBox
from .textrendering import TextRenderer
class Game:
    def __init__(self):
        info = pygame.display.Info()

# You can now access the screen width and height
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width//2,self.screen_height//2))
        self.font = pygame.font.Font(None, 32)
        self.textbox = TextBox(50, 50, 140, 32, self.font)
        self.board = Board()
        self.text_renderer = TextRenderer(font_size=32, font_color=(255, 255, 255))
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1
    def get_player_move(self):
        while True:
            try:
                move = input(f"{self.current_player.name} ({self.current_player.symbol}), enter your move (row, col): ")
                row, col = map(int, move.split())
                
                if 0 <= row < 3 and 0 <= col < 3:  # Check if the move is within the grid
                    if self.board.is_valid_move(row, col):
                        return [row, col]  # Return the move as a list
                    else:
                        print("This cell is already occupied. Please try again.")
                else:
                    print("Move out of range. Please enter row and column numbers between 0 and 2.")

            except ValueError:
                print("Invalid input. Please enter row and column as numbers separated by a space.")

    def play(self):
        text_input = ""
        input_active = False
        run = True
        while run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and (self.player1.name == "" or self.player2.name == ""):
                        if self.player1.name == "":
                            self.player1.name = self.textbox.text
                            self.text_renderer.draw_text(self.screen,self.player1.name,(self.screen_width - 50, self.screen_height))
                        else:
                            self.player2.name = self.textbox.text
                            self.text_renderer.draw_text(self.screen,self.player2.name,(self.screen_width - 50, self.screen_height - 50))
                        #print(f"{self.player1.name} player1 name")
                        #print(f"{self.player2.name} player2 name")
                self.textbox.handle_event(event)
            self.screen.fill((20,100,0))
            if self.player1.name:
                print("player1")
                self.text_renderer.draw_text(self.screen,self.player1.name,(self.screen_width - 50, self.screen_height))
            if self.player2.name:
                print("player 2")
                self.text_renderer.draw_text(self.screen,self.player2.name,(100, 50))

            self.textbox.draw(self.screen)
            pygame.display.flip()
            '''
            print("hi")
            self.board.display()
            position = self.get_player_move()
            self.board.make_move(position, self.current_player)
            if self.board.is_win(self.current_player.symbol) or self.board.is_tie():
                # Announce the result
                if self.board.is_win(self.current_player.symbol):
                    print(f"{self.current_player.name} wins!")
                else:
                    print("It's a tie!")

                    # Ask if they want to play again
                play_again = input("Play again? (y/n): ").lower()
                if play_again == "y":
                    self.board.reset_board()
                    # Optionally reset other game states like current player
                else:
                    break
            self.screen.fill((255, 255, 255))
            #self.board.draw(self.screen)
            pygame.display.flip()
            self.switch_player()
            '''

    def switch_player(self):
        #handel a players turn
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1