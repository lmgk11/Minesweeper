class Tile:
    def __init__(self, bomb):
        self.bomb = bomb # bool to set bombs
        self.number = None
        self.revealed = False
        self.flagged = False
    def set_number(self, number):
        self.number = number
    def __str__(self):
        return '*' if self.bomb else f'{self.number}'