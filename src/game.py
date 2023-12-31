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
        move = input(f"{self.current_player.name} ({self.current_player.symbol}), enter your move (row, col)")
        row , col = map(int, move.split())
        if self.board.is
    def play(self):
        self.board.display()

    
    def switch_player(self):
        #handel a players turn
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1