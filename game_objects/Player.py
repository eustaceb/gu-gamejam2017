from .Entity import Entity

import pygame
import math

# Wow its a playar
class Player(Entity):

    key_up = pygame.K_w
    key_down = pygame.K_s
    key_left = pygame.K_a
    key_right = pygame.K_d
    
    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)

    def update(self, tilemap, entities):

        key = pygame.key.get_pressed()

        if key[self.key_up]:
            if not key[self.key_down]:
                self.move_up()
        elif key[self.key_down]:
            self.move_down()

        if key[self.key_left]:
            if not key[self.key_right]:
                self.move_left()
        elif key[self.key_right]:
            self.move_right()

        super(Player, self).update(tilemap, entities)
