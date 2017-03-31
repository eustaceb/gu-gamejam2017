import random

import pygame
import math
from pygame.rect import Rect

from game_objects.Bullet import Bullet
from .NPC import NPC

class Cthulhu(NPC):

    original = None
    shoot_timer = 0
    health = 100

    def __init__(self, x, y, **kwargs):
        image = pygame.image.load("assets/cthulhu_full.png")
        self.original = image
        self.shoot_timer = 0
        super(Cthulhu, self).__init__(image=image, rect=Rect(x, y, 259, 259), max_velocity=4, **kwargs)

    def update(self, **kwargs):

        player_pos = (self.player.rect.center[0], self.player.rect.center[1])
        turret_pos = (self.rect.center[0], self.rect.center[1])
        distance = math.hypot((player_pos[0] - turret_pos[0]), (player_pos[1] - turret_pos[1]))

        if self.shoot_timer == 0:  #Limit shooting to interval
            if distance < self.range:  #If player is reachable within range
                # Choose a random target, one of the positions that delimit player

                targets = []
                for x in range(0,random.randint(5,10)):
                    self.shoot((self.rect.centerx+random.random(0,10),self.rect.centery-random.random(0,10)),
                               self.bullet_lifetime)

    def shoot(self, target_pos, lifetime):
        self.world.bullets.add(Bullet(self.rect.center, target_pos, lifetime, bullet_image=self.bullet_image))
