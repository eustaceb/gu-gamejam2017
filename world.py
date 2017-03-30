import pygame
from game_objects.Entity import *
from game_objects.Player import *
import pygame, csv
from Resource import *
from TileMap import *


class World:
    def __init__(self, screen, resources):
        self.entities = []
        self.resources = resources
        self.tilemap = TileMap("map1.csv", self.resources)
        print(len(self.tilemap.data))
        ball_sprite = pygame.image.load("test.gif")
        ball = Player(rect=pygame.Rect(400,300,64,64), image=ball_sprite)
        self.entities.append(ball)
    
    def render(self, screen):
        screen.fill((0,0,0))

        self.tilemap.render(screen)
        for ent in self.entities:
            ent.render(screen)
        #screen.blit(self.tilemap.data[0][0].get_image(), (300,400))
        pygame.display.flip()

    def update(self):
        for ent in self.entities:
            ent.update()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
        if event.type == pygame.QUIT: return False
        return True

