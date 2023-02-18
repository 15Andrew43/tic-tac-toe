from enum import Enum
import numpy as np



class BadStep(Exception):
    pass
class WIN(Exception):
    pass


class Field:
    def __init__(self, sizes=3):
        self.sizes = sizes
        self.field = np.zeros((sizes, sizes), dtype=int)
        self.player = 1 #  Player.tic
    
    def check_win(self, player):
        for i in range(self.sizes):
            if sum(self.field[i, :]) * self.player == 3:
                return True, [(i, 0), (i, self.sizes)]
            if sum(self.field[:, i]) * self.player == 3:
                return True, [(0, i), (self.sizes, i)]
        sum_left = 0
        sum_right = 0
        for i in range(self.sizes):
            sum_left += self.field[i, i]
            sum_right += self.field[i, self.sizes - i - 1]
        if sum_left * player == 3:
            return True, [(0, 0), (self.sizes, self.sizes)]
        elif sum_right * player == 3:
            return True, [(0, self.sizes), (self.sizes, 0)]
        return False, []
    
    
    def make_step(self, step):
        y, x = step
        if self.field[y][x] != 0:
            raise BadStep()
        self.field[y][x] = self.player
        
        is_win, where = self.check_win(self.player)

        self.player *= 1 if is_win else -1
        
        return is_win, self.player
        
        
    
    def __getitem__(self, key):
        return self.field[key]

    def __repr__(self):
        return str(self.field)
