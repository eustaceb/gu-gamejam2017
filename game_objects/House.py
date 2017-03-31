import pygame
from pygame.rect import Rect

from .Entity import Entity


class House(Entity):
    def __init__(self, x, y, player=None, **kwargs):
        self.images = [pygame.image.load("assets/house_windows.png"),
                       pygame.image.load("assets/house_windows_damaged_1.png"),
                       pygame.image.load("assets/house_windows_damaged_2.png"),
                       pygame.image.load("assets/house_windows_damaged_3.png"),
                       pygame.image.load("assets/house_windows_damaged_4.png"),
                       pygame.image.load("assets/house_windows_damaged_final.png")]
        self.health = 5
        self.player = player
        self.destroyed = False

        self.tractor = pygame.sprite.Group(player.tractor_beam)
        super(House, self).__init__(rect=Rect(x,y,64,64), image=self.images[0], **kwargs)


    def set_images(self, images):
        self.images = images

    def update(self, tilemap=None, entities=None, **kwargs):
        super(House, self).update()

    def handle_collisions(self, tilemap):
        super(House, self).handle_collisions(tilemap)
        if not self.destroyed:
            collisions = pygame.sprite.spritecollide(self, self.player.bombs, True)
            if len(collisions) > 0:
                self.damage()

    def damage(self):
        if 0 < self.health <= len(self.images):
            self.image = self.images[len(self.images) - self.health]
        if self.health > 0:
            self.health -= 1
            if self.health <= 0:
                self.destroyed = True
                self.player.score += 5
