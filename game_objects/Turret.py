import pygame
import random
import math
from .Bullet import Bullet
from .Entity import Entity
from collections import deque
import pygame


class Turret(Entity):
    def __init__(self, image, player=None, bullet_image=None,
                 shoot_interval=1000, range=500, bullet_lifetime=5000, **kwargs):
        self.bullet_image = bullet_image
        self.shoot_interval = shoot_interval  # in milliseconds
        self.counter = 0
        self.player = player
        self.range = range
        self.shots = deque()
        self.bullet_lifetime = bullet_lifetime
        super(Turret, self).__init__(image=image, **kwargs)

    def set_player(self, player):
        self.player = player

    def update(self):
        player_pos = (self.player.rect.center[0], self.player.rect.center[1])
        turret_pos = (self.rect.center[0], self.rect.center[1])
        distance = math.hypot((player_pos[0] - turret_pos[0]), (player_pos[1] - turret_pos[1]))
        if distance < self.range: # If player is reachable within range
            if self.counter >= self.shoot_interval: # Limit shooting to interval
                self.counter = 0
                # Choose a random target, one of the positions that delimit player
                targets = (self.player.rect.bottomleft, self.player.rect.bottomright, self.player.rect.center,
                           self.player.rect.topleft, self.player.rect.topright, self.player.rect.midtop,
                           self.player.rect.midbottom, self.player.rect.midleft, self.player.rect.midright)
                self.shoot(targets[random.randint(0, 8)], self.bullet_lifetime)
        if len(self.shots) > 0: # Pop one by one, no need to iterate over the whole list due to freq updates
            if self.shots[0].gone():
                self.shots.popleft()

    def shoot(self, target_pos, lifetime):
        self.shots.append(Bullet(self.bullet_image, self.rect.midtop, target_pos, lifetime))  # Spawn bullet and add to list
