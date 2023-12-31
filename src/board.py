class Board:
    def __init__(self):
        # Create a 3x3 grid initialized with empty spaces
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, position, player):
        # update the board with the players move
        if self.grid[position[0]][position[1]] == " ":
            self.grid[position[0]][position[1]] == player.symbol
            return True
        else:
            return False
    def is_win(self,symbol):
        #check rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        
        #check columns
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
        
        #check diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True
        if all(self.grid[i][2-i] == symbol for i in range(3)):
            return True
        
        return False
        
    def is_valid_move(self, row, col):
        #check to see if the spot able to be moved upon
        if self.grid[row][col] == " ":
            return True
        return False
    
    def is_tie(self):
        #check if the game is a tie
        for row in self.grid:
            if any(cell == " " for cell in row):
                return False # if cell is empty it is nto a tie
        return True #if no cell is empty it is a tie

    def display(self):
        for row in self.grid:
           print(" | ".join(row))
           if row != self.grid[-1]:
               print("-" * 9)