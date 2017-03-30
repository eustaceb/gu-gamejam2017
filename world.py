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

        player_sprite = pygame.image.load("assets/ufo.png")

        self.camera = pygame.Rect(0,0, screen.get_width(), screen.get_height())
    
    def render(self, screen):
        screen.fill((0,0,0))

        # Moved from self.map.render
        for tilemap in self.tilemaps.itervalues():
            tilemap.render(screen, self.camera)

        for ent in self.entities:
            ent.render(screen, self.camera)
        self.player.render(screen, self.camera)

    def update(self):
        self.player.update(self.map.tilemaps.itervalues(), self.entities)
        for ent in self.entities:
            ent.update()
        self.camera.center = self.player.rect.center

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
        if event.type == pygame.QUIT: return False
        return True

