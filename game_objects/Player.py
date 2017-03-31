from pygame.rect import Rect

from game_objects.TractorBeam import TractorBeam
from .PhysicsEntity import PhysicsEntity
from .Bomb import Bomb
import pygame

# Wow its a playar
class Player(PhysicsEntity):

    health = 5
    tractor_beam = None
    score = 0

    last_bomb = 0
    rotation_angle = 0
    max_rotation = 15

    key_up = pygame.K_w
    key_down = pygame.K_s
    key_left = pygame.K_a
    key_right = pygame.K_d
    key_bomb = pygame.K_SPACE
    original_image = None

    def __init__(self, **kwargs):
        self.tractor_beam = TractorBeam(rect=Rect(0,0,64,64), player=self)

        if kwargs.get("gravity") is None:
            kwargs["gravity"] = 0

        super(Player, self).__init__(**kwargs)
        self.original_image = self.image
        self.bombs = pygame.sprite.Group()
        self.bomb_interval = 1000

    def update(self, tilemap=None, entities=None, bullets=None, current_tick=0, **kwargs):

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

        if key[self.key_bomb]:
            self.bomb(current_tick)

        super(Player, self).update(tilemap, entities)

        self.rotation_angle = self.x_velocity/self.max_velocity * self.max_rotation

        if self.x_velocity != 0:
            center = self.rect.center
            self.image = pygame.transform.rotate(self.original_image, -self.rotation_angle)
            self.rect.center = center

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

    def bomb(self, current_tick):
        if self.bomb_interval + self.last_bomb < current_tick:
            rect = Rect(self.rect.midbottom, (16, 16))
            self.bombs.add(Bomb(image=None, rect=rect))
            self.last_bomb = current_tick
