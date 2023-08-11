import tile
import random

class Game:
    def __init__(self, COLS, ROWS):
        self.COLS = COLS
        self.ROWS = ROWS
        self.tiles = []

        for i in range(self.ROWS):
            col = []
            for j in range(self.COLS):
                col.append(tile.Tile(True if random.random() > 0.8 else False))
                
            self.tiles.append(col)

        self.assign_tile_number()
        self.debug_print()

    def assign_tile_number(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.tiles[i][j].bomb:
                    continue
                else:
                    self.tiles[i][j].number = 0
                    if i + 1 < self.ROWS and self.tiles[i+1][j].bomb:
                        self.tiles[i][j].number += 1
                    if i - 1 > 0 and self.tiles[i-1][j].bomb:
                        self.tiles[i][j].number += 1
                    if j + 1 < self.COLS and self.tiles[i][j+1].bomb:
                        self.tiles[i][j].number += 1
                    if j - 1 > 0 and self.tiles[i][j-1].bomb:
                        self.tiles[i][j].number += 1
                    if i + 1 < self.ROWS and j + 1 < self.COLS and self.tiles[i+1][j+1].bomb:
                        self.tiles[i][j].number += 1
                    if i - 1 > 0 and j - 1 > 0 and self.tiles[i-1][j-1].bomb:
                        self.tiles[i][j].number += 1
                    if i + 1 < self.ROWS and j - 1 > 0 and self.tiles[i+1][j-1].bomb:
                        self.tiles[i][j].number += 1
                    if i - 1 > 0 and j + 1 < self.COLS and self.tiles[i-1][j+1].bomb:
                        self.tiles[i][j].number += 1
    def debug_print(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                print(f' {self.tiles[i][j]} ', end='')
            print()