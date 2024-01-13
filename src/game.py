import pygame
from .player import Player
from .board import Board

class Game:
    def __init__(self):
        info = pygame.display.Info()

# You can now access the screen width and height
        screen_width = info.current_w
        screen_height = info.current_h
        self.screen = pygame.display.set_mode((screen_width//2,screen_height//2))
        self.board = Board()
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
        while True:
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

    def switch_player(self):
        #handel a players turn
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1