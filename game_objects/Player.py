from .Entity import *
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

    def update(self):

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

        velocity = math.sqrt(math.pow(self.x_velocity, 2) + math.pow(self.y_velocity, 2))

        if velocity > self.max_velocity:
            direction = math.atan2(self.y_velocity, self.x_velocity)
            self.y_velocity = math.sin(direction)*self.max_velocity
            self.x_velocity = math.cos(direction)*self.max_velocity

        super(Player, self).update()
