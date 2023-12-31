from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1
    
    def get_player_move(self):
        #get player move
        while True:
            try:
                move = input(f"{self.current_player.name} ({self.current_player.symbol}), enter your move (row, col)")
                row , col = map(int, move.split())
                if self.board.is_valid_move(row,col):
                    return [row, col] #return the move as a list
                else:
                    print("This cell is already occupied please try again")
            except ValueError:
                print("invalud input. Please enter a row and column as a number seperated by a space")
    def play(self):
        while True:
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


    def switch_player(self):
        #handel a players turn
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1