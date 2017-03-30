from collections import OrderedDict

from TileMap import *
from Tile import *

from game_objects.Entity import *
from game_objects.Player import *
from game_objects.Turret import *


class Map:
    def __init__(self):
        self.tilemaps = {}
        self.entities = []
        self.player = None

    def entity_spawn(self, resource, x_pos=0, y_pos=0, **kwargs):
        if not "rect" in kwargs:
            kwargs["rect"] = pygame.Rect(x_pos, y_pos, resource.image.get_width(), resource.image.get_height())
        if resource.id == "p":
            self.player = Player(image=resource.image, **kwargs)
        elif resource.type == "turret":
            kwargs["rect"] = pygame.Rect(x_pos, y_pos, 64, 64)
            return Turret(image=resource.image, player=self.player, **kwargs)  # check if referenced correctly
        else:
            return Entity(image=resource.image, **kwargs)

    def load_map(self, filename, resources):
        with open(str(filename), 'r') as f:
            tile_map_populated = False
            tiles = []
            rows, cols = 0, 0
            tile_w, tile_h = 64, 64
            this_cols = 0
            y=0
            collides=True
            layer = 0 
            offset_x, offset_y = 0,0
            tile_repeat = 1
            row_repeat = 1
            for line in f.readlines():
                line_strip = line.strip()
                if len(line_strip) == 0:
                    if tile_map_populated:
                        tile_map = TileMap(res=resources, tile_h=tile_h, tile_w=tile_w)
                        tile_map.add(tiles)
                        tile_map.rows = rows
                        tile_map.cols = cols
                        tile_map.collides = collides
                        self.tilemaps[layer] = tile_map
                        if type(layer) is int:
                            layer += 1
                        else:
                            layer += "1"
                        tile_map_populated = False
                        tiles = []
                        rows, cols = 0, 0
                        tile_w, tile_h = 64, 64
                        offset_x, offset_y = 0, 0
                        collides = True
                        tile_repeat = 1
                        row_repeat = 1
                    else:
                        continue
                elif (line_strip[0] == "/"):
                    continue
                elif line_strip[0] == "@":
                    tokens = line_strip.split()
                    if tokens[0] == "@offset":
                        if len(tokens) >= 3:
                            if tokens[1].isalnum() and tokens[2].isalnum():
                                offset_x, offset_y = int(tokens[1]), int(tokens[2])
                            y = 0
                    elif tokens[0] == "@pad":
                        if len(tokens) >= 3:
                            if tokens[1].isalnum() and tokens[2].isalnum():
                                offset_x += int(tokens[1])
                                y += int(tokens[2])
                    elif tokens[0] == "@tile_size":
                        if len(tokens) >= 3:
                            tile_w, tile_h = int(tokens[1]), int(tokens[2])
                    elif tokens[0] == "@collide":
                        if len(tokens) >= 2:
                            if tokens[1] == "off":
                                collides = False
                            else:
                                collides = True
                    elif tokens[0] == "@layer":
                        if len(tokens) >= 2:
                            if tokens[1].isalnum():
                                layer = int(tokens[1])
                            else:
                                layer = tokens[1]
                    elif tokens[0] == "@repeat_h":
                        if len(tokens) >= 2:
                            if tokens[1].isalnum():
                                tile_repeat = int(tokens[1])
                    elif tokens[0] == "@repeat_v":
                        if len(tokens) >= 2:
                            if tokens[1].isalnum():
                                row_repeat = int(tokens[1])
                    elif tokens[0] == "@tile_grid":
                        if len(tokens) >= 3:
                            if tokens[1].isalnum() and tokens[2].isalnum():
                                tile_repeat = int(tokens[1])
                                row_repeat = int(tokens[2])



                else:
                
                
                    tile_ids = [x.strip() for x in line_strip.split(",")] * tile_repeat 
                    row_len = len(tile_ids)
                    print("row ",row_len)
                    tile_ids *= row_repeat
                        
                    x = 0
                    this_cols = 0
                    for id in tile_ids:
                        if id.isalnum():
                            tile_res = resources[id]
                            if tile_res.type == "tile":
                                tile = Tile(
                                    rect=pygame.Rect(offset_x + x, offset_y + y, tile_res.image.get_width(),
                                                     tile_res.image.get_height()),
                                    image=resources[id].get_image()
                                )
                                tiles.append(tile)
                                tile_map_populated = True
                            else:
                                self.entities.append(self.entity_spawn(
                                    resource=tile_res,
                                    x_pos=offset_x + x,
                                    y_pos=offset_y + y
                                ))
                        x += tile_w
                        this_cols += 1
                        if this_cols >= row_len:
                            y +=  tile_w
                            this_cols = 0
                            rows += 1
                            x = 0
                if this_cols > cols: cols = this_cols
                y += tile_h
                rows += 1

                if tile_map_populated:
                    tile_map = TileMap(res=resources, tile_h=tile_h, tile_w=tile_w)
                    tile_map.add(tiles)
                    tile_map.rows = rows
                    tile_map.cols = cols
                    tile_map.collides = collides
                    self.tilemaps[layer] = tile_map
        # Set player for turrets
        for i in range(len(self.entities)):
            if isinstance(self.entities[i], Turret):
                self.entities[i].set_player(self.player)

        self.tilemaps = OrderedDict(sorted(self.tilemaps.items(), key=lambda x:x[0], reverse=True))

        return self.player, self.tilemaps, self.entities
