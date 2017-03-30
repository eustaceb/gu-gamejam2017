from collections import OrderedDict

from TileMap import *
from Tile import *

from game_objects.Entity import *
from game_objects.Player import *

class Map:
    def __init__(self):
        self.tilemaps = {}
        self.entities = []
        self.player=None
    

    def entity_spawn(self, id, x_pos=0, y_pos=0, **kwargs):
        if not "rect" in kwargs:
            kwargs["rect"] = pygame.Rect(x_pos, y_pos, 128, 128)
        if id == "p":
            self.player = Player(**kwargs)
        else:
            self.entities.append(Entity(**kwargs))

    def load_map(self, filename, resources):
        with open(str(filename) , 'r') as f:
            tile_map_populated = False
            tiles = []
            rows,cols = 0,0
            tile_w, tile_h = 64,64
            this_cols = 0
            y=0
            layer = 0 
            offset_x, offset_y = 0,0
            for line in f.readlines():
                line_strip = line.strip()
                if len(line_strip) == 0:
                    if tile_map_populated:
                        tile_map = TileMap(res=resources, tile_h=tile_h, tile_w=tile_w)
                        tile_map.add(tiles)
                        tile_map.rows = rows
                        tile_map.cols = cols
                        tile_map.collides = True
                        self.tilemaps[layer] = tile_map
                        layer += 1
                        tile_map_populated = False
                        tiles = []
                        rows,cols = 0,0
                        tile_w, tile_h = 64,64
                        offset_x, offset_y = 0,0
                    else:
                        continue
                elif (line_strip[0] == "/") :
                    continue
                elif line_strip[0] == "@":
                    tokens = line_strip.split()
                    if tokens[0] == "@offset":
                        if len(tokens) >= 3:
                            offset_x, offset_y = int(tokens[1]), int(tokens[2])
                    elif tokens[0] == "@tile_size":
                        if len(tokens) >= 3:
                            tile_w, tile_h = int(tokens[1]), int(tokens[2])
                else:
                    tile_ids = [x.strip() for x in line_strip.split(",")]
                    x = 0
                    this_cols = 0
                    for id in tile_ids:
                        if id.isalnum():
                            tile_res = resources[id]
                            if tile_res.type == "tile":
                                tile = Tile(
                                    rect = pygame.Rect(offset_x+x, offset_y+y, tile_w, tile_h), 
                                    image = resources[id].get_image()
                                )
                                tiles.append(tile)
                                tile_map_populated = True
                            else:
                                self.entities.append(self.entity_spawn(
                                    id = tile_res.id,
                                    image = tile_res.image,
                                    x_pos = offset_x+x,
                                    y_pos = offset_y+y
                                ))
                        x += tile_w
                        this_cols += 1
                if this_cols > cols: cols = this_cols
                y += tile_h        
                rows += 1
                self.tilemaps = OrderedDict(sorted(self.tilemaps.items(), key=lambda x:x[0]))

                if tile_map_populated:
                    tile_map = TileMap(res=resources, tile_h=tile_h, tile_w=tile_w)
                    print(tiles)
                    tile_map.add(tiles)
                    print(tile_map)
                    tile_map.rows = rows
                    tile_map.cols = cols
                    tile_map.collides = True
                    self.tilemaps[layer] = tile_map

    def render(self, screen, camera):
        for tilemap in self.tilemaps.itervalues():
            tilemap.render(screen, camera)

