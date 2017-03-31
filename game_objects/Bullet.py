from .PhysicsEntity import PhysicsEntity
from pygame import Rect, Surface
import math
import pygame


class Bullet(PhysicsEntity):
    def __init__(self, origin_pos, target_pos, created_on, lifetime, bullet_image=None, base_velocity=5, **kwargs):

        x = target_pos[0] - origin_pos[0]
        y = target_pos[1] - origin_pos[1]
        distance = math.hypot(x, y)
        x_velocity = x / distance * base_velocity
        y_velocity = y / distance * base_velocity

        #if bullet_image is None:
        bullet_image = Surface((8, 8), pygame.SRCALPHA)
        bullet_image.fill((0, 0, 0, 0))
        pygame.draw.circle(bullet_image, (255, 200, 0), (4, 4), 4)
        #bullet_image = Surface((2, 8))
        #bullet_image.fill((255, 200, 0))
        #bullet_surface.blit(bullet_image, (4, 1))

        #rotation_angle = (180/math.pi) * math.atan2(y, x) + 90
        #bullet_image = pygame.transform.rotate(bullet_surface, -rotation_angle)

        rect = Rect(origin_pos, bullet_image.get_size())
        self.lifetime = lifetime
        self.created_on = created_on
        super(Bullet, self).__init__(rect=rect, image=bullet_image, gravity=0,
                                     x_velocity=x_velocity, y_velocity=y_velocity, **kwargs)

    def update(self, **kwargs):
        super(Bullet, self).update(**kwargs)

    def gone(self, tick):
        if tick - self.created_on > self.lifetime:
            return True
        return False
