from .Entity import Entity
from pygame import Rect
import math


class Bullet(Entity):
    def __init__(self, bullet_image, origin_pos, target_pos, lifetime, base_velocity=5, **kwargs):
        rect = Rect(origin_pos, bullet_image.get_size())
        self.lifetime = lifetime
        self.counter = 0
        distance = math.hypot(target_pos[0] - origin_pos[0], target_pos[1] - origin_pos[1])
        x_velocity = (target_pos[0] - origin_pos[0]) / distance * base_velocity
        y_velocity = (origin_pos[1] - target_pos[1]) / distance * base_velocity
        super(Bullet, self).__init__(rect=rect, image=bullet_image, gravity=0,
                                     x_velocity=x_velocity, y_velocity=y_velocity, **kwargs)

    def update(self, **kwargs):
        self.counter += 1
        super(Bullet, self).update(**kwargs)

    def gone(self):
        if self.counter > self.lifetime:
            return False
        return True
