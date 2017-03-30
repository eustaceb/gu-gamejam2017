from .Entity import Entity
import pygame
import math

# Wow its a playar
class Player(Entity):

    key_up = pygame.K_W
    key_down = pygame.K_S
    key_left = pygame.K_A
    key_right = pygame.K_D

    def __init__(self):
        super(Player, self).__init__()

    def update(self):

        key = pygame.key.get_pressed()

        if key[self.key_up] and key[self.key_down] and key[self.key_left] and key[self.key_right]:
            self.slow()
        else:
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
