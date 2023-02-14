from enum import Enum
import numpy as np

class Player(Enum):
    tic = 1
    toc = -1

class BadStep:
    pass


class Field:
    def __init__(self, sizes=3):
        self.sizes = sizes
        self.field = np.zeros((sizes, sizes))
        self.player = Player.tic
    
    def check_win(self, player):
        for i in range(self.sizes):
            if sum(self.field[i, :]) * self.player == 3:
                return True
            if sum(self.field[:, i]) * self.player == 3:
                return True
        sum_left = 0
        sum_right = 0
        for i in range(self.sizes):
            sum_left += self.field[i, i]
            sum_right += self.field[self.sizes - i - 1, self.sizes - i - 1]
        if sum_left * player == 3:
            return True
        if sum_right * player == 3:
            return True
        return False
    
    def draw(self):
        pass
    
    def make_step(self, step):
        y, x = step
        if self.field[y][x] != 0:
            raise BadStep()
        self.field[y][x] = self.step
        
        is_win, where = self.check_win(self.player)

        if is_win:
            self.draw()
        
        self.player *= -1

        
