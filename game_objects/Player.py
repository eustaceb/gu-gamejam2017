from pygame.rect import Rect

from game_objects.TractorBeam import TractorBeam
from .PhysicsEntity import PhysicsEntity
import pygame

# Wow its a playar
class Player(PhysicsEntity):

    health = 5
    tractor_beam = None
    score = 0

    rotation_angle = 0
    max_rotation = 15

    key_up = pygame.K_w
    key_down = pygame.K_s
    key_left = pygame.K_a
    key_right = pygame.K_d
    original_image = None

    def __init__(self, **kwargs):
        self.tractor_beam = TractorBeam(rect=Rect(0,0,64,64), player=self)

        if kwargs.get("gravity") is None:
            kwargs["gravity"] = 0

        super(Player, self).__init__(**kwargs)
        self.original_image = self.image

    def update(self, tilemap=None, entities=None, bullets=None, **kwargs):

        key = pygame.key.get_pressed()

        if key[self.key_up]:
            if not key[self.key_down]:
                self.move_up()
        elif key[self.key_down]:
            self.move_down()
        else:
            self.slowY()

        if key[self.key_left]:
            if not key[self.key_right]:
                self.move_left()
        elif key[self.key_right]:
            self.move_right()
        else:
            self.slowX()

        super(Player, self).update(tilemap, entities)

        self.rotation_angle = self.x_velocity/self.max_velocity * self.max_rotation

        if self.x_velocity != 0:
            self.image = pygame.transform.rotate(self.original_image, -self.rotation_angle)

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
            self.score -= amount

