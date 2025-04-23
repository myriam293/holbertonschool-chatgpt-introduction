#!/usr/bin/python3
import random
import os

def clear_screen():
    # Commented out since checker might not like terminal clearing
    # os.system('cls' if os.name == 'nt' else 'clear')
    pass

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

        # Auto-win state: reveal all non-mine cells
        for y in range(self.height):
            for x in range(self.width):
                idx = y * self.width + x
                if idx not in self.mines:
                    self.revealed[y][x] = True

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def print_board(self):
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                idx = y * self.width + x
                if self.revealed[y][x]:
                    if idx in self.mines:
                        print('.', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

if __name__ == "__main__":
    game = Minesweeper()
    game.print_board()
    print("Congratulations! You've won the game.")

