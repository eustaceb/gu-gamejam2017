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

    direction = Direction.LEFT
    player = None

    def __init__(self, rect, image, player=None, **kwargs):
        self.player = player
        self.tractor = Group(player.tractor_beam)
        super(NPC, self).__init__(rect, image, **kwargs)

    def update(self, tilemap=None, entities=None, **kwargs):
        if self.direction == Direction.LEFT:
            pass
            #self.move_left()
        elif self.direction == Direction.RIGHT:
            pass
            #self.move_right()
        else:
            self.slow()

        switch_direction = random.randint(0,100)
        if switch_direction == 0:
            if self.direction == Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                self.direction = Direction.LEFT
        elif switch_direction == 100:
            self.direction = Direction.STATIONARY

        super(NPC, self).update(tilemap, entities)

    def handle_collisions(self, tilemap):
        print("wut")
        super(NPC, self).handle_collisions(tilemap)

        tractors = pygame.sprite.spritecollide(self, self.tractor, True)

        for tractor in tractors:
            print(tractor)
            if tractor.enabled:
                print("WEWE")
                self.player.score += 10
                print(self.player.score)
                #Delet this
