from .PhysicsEntity import PhysicsEntity
from pygame import Rect, Surface
import math


class Bullet(PhysicsEntity):
    def __init__(self, origin_pos, target_pos, lifetime, bullet_image=None, base_velocity=5, **kwargs):
        #if bullet_image is None:
        bullet_image = Surface((5, 10))
        bullet_image.fill((255, 200, 0))
        print origin_pos, bullet_image.get_size()
        rect = Rect(origin_pos, bullet_image.get_size())
        self.lifetime = lifetime
        self.counter = 0
        distance = math.hypot(target_pos[0] - origin_pos[0], target_pos[1] - origin_pos[1])
        x_velocity = (target_pos[0] - origin_pos[0]) / distance * base_velocity
        y_velocity = (target_pos[1] - origin_pos[1]) / distance * base_velocity
        super(Bullet, self).__init__(rect=rect, image=bullet_image, gravity=0,
                                     x_velocity=x_velocity, y_velocity=y_velocity, **kwargs)

    def update(self, **kwargs):
        self.counter += 1
        super(Bullet, self).update(**kwargs)

    def gone(self):
        if self.counter > self.lifetime:
            return True
        return False
