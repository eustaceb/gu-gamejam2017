import random

import pygame
from enum import Enum
from pygame.sprite import Group

from .PhysicsEntity import PhysicsEntity


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    STATIONARY = 2


# A villager that lives in the village
class NPC(PhysicsEntity):

    switch_timer = 0
    direction = Direction.LEFT
    player = None

    def __init__(self, rect, image, player=None, **kwargs):
        self.player = player
        self.tractor = Group(player.tractor_beam)
        super(NPC, self).__init__(rect, image, **kwargs)

    def update(self, tilemap=None, entities=None, **kwargs):
        super(NPC, self).update(tilemap, entities)

        if(self.switch_timer == 0):
            switch_direction = random.randint(0,50)

            if switch_direction == 0:
                if self.direction == Direction.LEFT:
                    self.direction = Direction.RIGHT
                else:
                    self.direction = Direction.LEFT
            elif switch_direction == 50:
                self.direction = Direction.STATIONARY
        else:
            self.switch_timer -= 1

        if(self.blocked_left):
            self.x_velocity = 0
            self.x_acceleration = 0
            self.direction = Direction.RIGHT
            self.switch_timer = 500000
            print("HIT LEFT")

        if (self.blocked_right):
            self.x_velocity = 0
            self.x_acceleration = 0
            self.direction = Direction.LEFT
            self.switch_timer = 500000
            print("HIT RIGHT")

        if self.direction == Direction.LEFT:
            self.move_left()
        elif self.direction == Direction.RIGHT:
            self.move_right()
        else:
            self.slow()

    def handle_collisions(self, tilemap, **kwargs):
        super(NPC, self).handle_collisions(tilemap, **kwargs)

        tractors = pygame.sprite.spritecollide(self, self.tractor, False)

        for tractor in tractors:
            if tractor.enabled:
                self.y_acceleration = -2
                print("COLLIDE!")
                #Delet this
