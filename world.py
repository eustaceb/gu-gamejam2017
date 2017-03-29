import pygame
from game_objects.Entity import *
import pygame, csv
from Resource import *
from TileMap import *


class World:
    def __init__(self, screen):
        self.entities = []
        self.resources = self.load_resources("resources.csv")
        self.tilemap = TileMap("map1.csv", self.resources)
        print(self.tilemap.data)
        ball_sprite = pygame.image.load("test.gif")
        ball = Entity(rect=pygame.Rect(400,300,64,64), image=ball_sprite)
        self.entities.append(ball)
    
    def render(self, screen):
        screen.fill((0,0,0))
        for tile in self.tilemap:
            pos = tile.get_x() * tile.get_width(), tile.get_y() * tile.get_height()
            screen.blit(tile.get_image(), pos)
        for ent in self.entities:
            ent.render(screen)
        pygame.display.flip()

    def update(self):
        for ent in self.entities:
            ent.update()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
            elif event.key == pygame.K_d:
                self.entities[0].x_velocity = 400/60.0
            elif event.key == pygame.K_a:
                self.entities[0].x_velocity = -400/60.0 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.entities[0].x_velocity = 0
            elif event.key == pygame.K_a:
                self.entities[0].x_velocity = 0
        return True

    def load_resources(self, filename):
        resources = {}
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader, None)
            # id,name,filename,type
            for line in reader:
                res_id, name, filename, type = line
                resources[res_id] = Resource(res_id, name, filename, type)
        return resources

