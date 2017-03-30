import csv

from pygame.rect import Rect
from pygame.sprite import Group

from Tile import *


class TileMap(Group):
    def __init__(self, filename, res, tile_h = 64, tile_w = 64):
        super(TileMap, self).__init__()
        self.tile_h = tile_h
        self.tile_w = tile_w
        self.cols = 0
        self.rows = 0
        self.current = -1
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
                    if not col == "#": 
                        tile = Tile(Rect(x, y, self.tile_w, self.tile_h), self.resources[col].image)
                        self.add(tile)
                    x += 1
                    count += 1
                y += 1
        if y != 0:
            self.rows = y
            self.cols = count / self.rows
    
    @static_method
    def parse_map(filename):
        with open(filename, "r") as f:
            for line in f.readlines():
                line_strip = line.strip()
                if len(line_strip) == 0:
                     
                elif line_strip[0] == "/"
                    
                if line_strip[0] == "@":
                    tokens = line_strip.split()
                    if tokens[0] == "@offset":
                        if len(tokens) >= 3:
                            offset = int(tokens[1]), int(tokens[2])

    def get_dimensions(self):
        return self.rows, self.cols

    def render(self, screen, camera):
        for sprite in self:
            screen.blit(sprite.image, (sprite.rect.x-camera.x, sprite.rect.y-camera.y))
