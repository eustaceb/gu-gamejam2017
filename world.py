import pygame
from game_objects.Entity import *
from game_objects.Player import *
import pygame, csv
from Resource import *
from TileMap import *
from Map import *
from game_objects.House import *
from collections import deque

from game_objects.Villager import Villager


class World:
    def __init__(self, screen, resources):
        self.font = pygame.font.SysFont("Arial", 25)
        self.tilemaps = {}
        self.entities = []
        self.bullets = pygame.sprite.Group()
        self.resources = resources
        #self.tilemap = TileMap("map1.csv", self.resources)
        self.map = Map()
        self.player, self.tilemaps, self.entities = self.map.load_map(filename="map2.txt", resources=self.resources)
        self.entities.append(Villager(self.player.rect.x, self.player.rect.y, player=self.player))

        # Set player and world for turrets; house images for houses
        house_images = [resources["h1"].image, resources["h2"].image, resources["h3"].image,
                        resources["h4"].image, resources["h5"].image]
        for i in range(len(self.entities)):
            if isinstance(self.entities[i], Turret):
                self.entities[i].set_player(self.player)
                self.entities[i].set_world(self)
            elif isinstance(self.entities[i], House):
                self.entities[i].set_images(house_images)

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

        health_text = self.font.render("Health: " + str(self.player.health), 1, (255, 0, 0))
        score_text = self.font.render("Score: " + str(self.player.score), 1, (255, 0, 0))
        screen.blit(health_text, (0, 0))
        screen.blit(score_text, (0, 50))

    def update(self, time_now):
        self.player.update(tilemap=self.map.tilemaps.itervalues(), entities=self.entities, bullets=self.bullets)
        for ent in self.entities:
            ent.update(tilemap=self.map.tilemaps.itervalues(), tick=time_now)

        for bul in self.bullets:
            bul.update()
        self.camera.center = self.player.rect.center

        if len(self.bullets) > 0:  # Pop one by one, no need to iterate over the whole list due to freq updates
            frst = self.bullets.sprites()[0]
            if frst.gone(time_now):
                self.bullets.remove(frst)



    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
        if event.type == pygame.QUIT: return False
        return True

