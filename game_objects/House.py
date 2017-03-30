import pygame
from .Entity import Entity


class House(Entity):
    def __init__(self, rect, image, player=None, **kwargs):
        self.images = []
        self.health = 50
        self.player = player
        self.destroyed = False
        self.tractor = pygame.sprite.Group(player.tractor_beam)
        super(House, self).__init__(rect, image, **kwargs)

    def set_images(self, images):
        self.images = images

    def update(self, tilemap=None, entities=None, **kwargs):
        super(House, self).update()

    def handle_collisions(self, tilemap):
        super(House, self).handle_collisions(tilemap)
        if not self.destroyed:
            tractors = pygame.sprite.spritecollide(self, self.tractor, False)
            for tractor in tractors:
                if tractor.enabled:
                    self.damage()
                    break

    def damage(self):
        if 0 < self.health/10 <= len(self.images):
            self.image = self.images[len(self.images) - self.health/10]
        if self.health > 0:
            self.health -= 1
            if self.health <= 0:
                self.destroyed = True
                self.player.score += 5
