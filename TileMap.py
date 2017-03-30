import csv
from Tile import *


class TileMap:
    def __init__(self, filename, res, tile_h = 64, tile_w = 64):
        self.tile_h = tile_h
        self.tile_w = tile_w
        self.cols = 0
        self.rows = 0
        self.current = -1
        self.data = {}
        self.resources = res
        self.filename = filename
        if filename: 
            self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            count = 0
            y = 0
            for line in reader:
                current_row = []
                x = 0
                for col in line:
                    tile = Tile(x, y, self.tile_w, self.tile_h, self.resources[col])
                    self.data[(x,y)] = tile
                    x += 1
                    count += 1
                y += 1
        if y != 0:
            self.rows = y
            self.cols = count / self.rows

    def get_dimensions(self):
        return self.rows, self.cols

    def get_data(self):
        return self.data

    def get_tile(self, x, y):
        return self.data((x,y))

    def __iter__(self):
        self.current = 0
        return self

    def next(self):
        if self.current >= (self.rows * self.cols) - 1:
            raise StopIteration
        else:
            self.current += 1
            return self.data[( self.current % self.rows, self.cols / self.rows) ]

    def render(self, screen):
        for t in self:
            t.render(screen)
