import pygame
import random
import math
from .Bullet import Bullet
from .Entity import Entity
from collections import deque
import pygame


class Turret(Entity):
    def __init__(self, image, world=None, player=None, bullet_image=None,
                 shoot_interval=700, range=500, bullet_lifetime=2000, **kwargs):
        self.bullet_image = bullet_image
        self.shoot_interval = shoot_interval  # in milliseconds
        self.player = player
        self.world = world
        self.range = range
        self.last_shot = 0
        self.bullet_lifetime = bullet_lifetime
        super(Turret, self).__init__(image=image, **kwargs)

    def set_world(self, world):
        self.world = world

    def set_player(self, player):
        self.player = player

    def update(self, **kwargs):
        if "tick" not in kwargs:
            return
        tick = kwargs["tick"]

        player_pos = (self.player.rect.center[0], self.player.rect.center[1])
        turret_pos = (self.rect.center[0], self.rect.center[1])
        distance = math.hypot((player_pos[0] - turret_pos[0]), (player_pos[1] - turret_pos[1]))
        if self.last_shot + self.shoot_interval < tick:  #Limit shooting to interval
            self.last_shot = tick
            if distance < self.range:  #If player is reachable within range
                # Choose a random target, one of the positions that delimit player
                targets = (self.player.rect.bottomleft, self.player.rect.bottomright, self.player.rect.center,
                           self.player.rect.topleft, self.player.rect.topright, self.player.rect.midtop,
                           self.player.rect.midbottom, self.player.rect.midleft, self.player.rect.midright)
                self.shoot(targets[random.randint(0, 8)], tick, self.bullet_lifetime)

    def shoot(self, target_pos, created_on, lifetime):
        self.world.bullets.add(Bullet(self.rect.midtop, target_pos, created_on, lifetime, bullet_image=self.bullet_image))
