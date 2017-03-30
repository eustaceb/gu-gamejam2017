from pygame.rect import Rect

from game_objects.TractorBeam import TractorBeam
from .PhysicsEntity import PhysicsEntity
import pygame

# Wow its a playar
class Player(PhysicsEntity):

    health = 5
    tractor_beam = None
    key_up = pygame.K_w
    key_down = pygame.K_s
    key_left = pygame.K_a
    key_right = pygame.K_d
    
    def __init__(self, **kwargs):
        self.tractor_beam = TractorBeam(rect=Rect(0,0,64,64), player=self)

        super(Player, self).__init__(**kwargs)

    def update(self, tilemap, entities, bullets):

        self.slow()
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

        super(Player, self).update(tilemap, entities)

        bullet_collisions = pygame.sprite.spritecollide(self, bullets, True)
        collision_count = len(bullet_collisions)
        if collision_count > 0:
            self.damage(collision_count)

        self.tractor_beam.update()

    def render(self, screen, camera):
        self.tractor_beam.render(screen, camera)
        super(Player, self).render(screen, camera)

    def damage(self, amount):
        if self.health > 0:
            self.health -= amount

