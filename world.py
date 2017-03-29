import pygame
from game_objects.Entity import *
import pygame, csv
from Resource import *
from TileMap import *


class World:
    def __init__(self, screen, resources):
        self.entities = []
        self.resources = resources
        self.tilemap = TileMap("map1.csv", self.resources)
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


