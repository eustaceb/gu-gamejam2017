import csv

from pygame.rect import Rect
from pygame.sprite import Group

from Tile import *


class TileMap(Group):
    def __init__(self, res, tile_h = 64, tile_w = 64, filename=None):
        super(TileMap, self).__init__()
        self.tile_h = tile_h
        self.tile_w = tile_w
        self.cols = 0
        self.rows = 0
        self.current = -1
        self.resources = res
        self.filename = filename
        self.collides = True

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
                        tile = Tile(Rect(x * self.tile_w, y * self.tile_h, self.tile_w, self.tile_h), self.resources[col].image)
                        self.add(tile)
                    x += 1
            
                y += 1
        if y != 0:
            self.rows = y
            self.cols = count / self.rows
    

    def get_dimensions(self):
        return self.rows, self.cols

    def render(self, screen, camera=None):
        for sprite in self:
            if camera:
                screen.blit(sprite.image, (sprite.rect.x-camera.x, sprite.rect.y-camera.y))
            else:
                screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))

    def __str__(self):
        return "%s, collides: %s"%(str(super(TileMap, self)), self.collides)
