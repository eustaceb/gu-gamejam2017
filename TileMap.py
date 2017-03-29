import csv
from Tile import *


class TileMap:
    def __init__(self, filename, res, tile_h = 64, tile_w = 64):
        self.tile_h = tile_h
        self.tile_w = tile_w
        self.current = -1
        self.data = []
        self.resources = res
        self.filename = filename
        if filename != "":
            self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            y = 0
            for line in reader:
                current_row = []
                x = 0
                for col in line:
                    tile = Tile(x, y, self.tile_w, self.tile_h, self.resources[col])
                    current_row += [tile]
                    x += 1
                self.data += [current_row]
                y += 1

    def get_data(self):
        return self.data

    def get_tile(self, x, y):
        return self.data[y][x]

    def __iter__(self):
        return self

    def next(self):
        if self.current >= (len(self.data) * len(self.data[0])) - 1:
            raise StopIteration
        else:
            self.current += 1
            return self.data[self.current / len(self.data[0])][self.current % len(self.data[0])]
