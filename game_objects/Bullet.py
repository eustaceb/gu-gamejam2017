from .PhysicsEntity import PhysicsEntity
from pygame import Rect, Surface
import math
import pygame


class Bullet(PhysicsEntity):
    def __init__(self, origin_pos, target_pos, lifetime, bullet_image=None, damage=1, base_velocity=5, **kwargs):

        x = target_pos[0] - origin_pos[0]
        y = target_pos[1] - origin_pos[1]
        direction = math.atan2(y,x)
        x_velocity = math.cos(direction) * base_velocity
        y_velocity = math.sin(direction) * base_velocity

        bullet_image = Surface((8, 8), pygame.SRCALPHA)
        bullet_image.fill((0, 0, 0, 0))
        pygame.draw.circle(bullet_image, (255, 200, 0), (4, 4), 4)

        rect = Rect(origin_pos, bullet_image.get_size())
        self.lifetime = lifetime
        super(Bullet, self).__init__(rect=rect, image=bullet_image, gravity=0,
                                     x_velocity=x_velocity, y_velocity=y_velocity, **kwargs)

    def update(self, **kwargs):
        self.lifetime -= 1
        super(Bullet, self).update(**kwargs)

    def gone(self, tick):
        return self.lifetime < 0
