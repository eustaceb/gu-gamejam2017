import pygame
from game_objects.Entity import *
from game_objects.Player import *
import pygame, csv
from Resource import *
from TileMap import *
from Map import *
from collections import deque


class World:
    def __init__(self, screen, resources):
        self.tilemaps = {}
        self.entities = []
        self.bullets = deque()
        self.resources = resources
        #self.tilemap = TileMap("map1.csv", self.resources)
        self.map = Map()
        self.player, self.tilemaps, self.entities = self.map.load_map(filename="map2.txt", resources=self.resources)

        # Set player and world for turrets
        for i in range(len(self.entities)):
            if isinstance(self.entities[i], Turret):
                self.entities[i].set_player(self.player)
                self.entities[i].set_world(self)

        player_sprite = pygame.image.load("assets/ufo.png")

        self.camera = pygame.Rect(0,0, screen.get_width(), screen.get_height())
        self.bg_surface = pygame.Surface(screen.get_size())
    
    def render(self, screen):
        screen.fill((0,0,0))
        #print(self.tilemaps.keys())
        if "bg" in self.tilemaps:
            self.tilemaps["bg"].draw(self.bg_surface)
        screen.blit(self.bg_surface, screen.get_rect())
        # Moved from self.map.render
        for k,tilemap in self.tilemaps.iteritems():
            if k=="bg":continue
            tilemap.render(screen, self.camera)

        for ent in self.entities:
            ent.render(screen, self.camera)
        for bul in self.bullets:
            bul.render(screen, self.camera)
        self.player.render(screen, self.camera)

    def update(self):
        self.player.update(self.map.tilemaps.itervalues(), self.entities)
        for ent in self.entities:
            ent.update()
        for bul in self.bullets:
            bul.update()
        self.camera.center = self.player.rect.center

        if len(self.bullets) > 0:  # Pop one by one, no need to iterate over the whole list due to freq updates
            if self.bullets[0].gone():
                self.bullets.popleft()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
        if event.type == pygame.QUIT: return False
        return True

