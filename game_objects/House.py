import pygame
from .PhysicsEntity import PhysicsEntity


class House(PhysicsEntity):
    def __init__(self, rect, image, player=None, **kwargs):
        self.images = []
        self.health = 5
        self.player = player
        self.destroyed = False
        super(House, self).__init__(rect, image, gravity=0, **kwargs)

    def set_images(self, images):
        self.images = images

    def update(self, tilemap=None, entities=None, **kwargs):
        super(House, self).update(tilemap, entities)

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
