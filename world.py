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
<<<<<<< HEAD
        print(len(self.tilemap.data))
        ball_sprite = pygame.image.load("assets/ufo.png")
        ball = Player(rect=pygame.Rect(400,300,64,64), image=ball_sprite)
        self.entities.append(ball)
=======

        player_sprite = pygame.image.load("assets/ufo.png")
        self.player = Player(rect=pygame.Rect(400,300,128,128), image=player_sprite)

        self.camera = pygame.Rect(0,0, screen.get_width(), screen.get_height())
>>>>>>> a45fc62ffe4de6ea9dd37c736a03ca225d87b992
    
    def render(self, screen):
        screen.fill((0,0,0))

        self.tilemap.render(screen,self.camera)
        for ent in self.entities:
            ent.render(screen, self.camera)
        self.player.render(screen, self.camera)
        pygame.display.flip()

    def update(self):
        self.player.update()
        for ent in self.entities:
            ent.update()
        self.camera.center = self.player.rect.center
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
        if event.type == pygame.QUIT: return False
        return True

