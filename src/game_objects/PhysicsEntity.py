from .Entity import Entity
import math
from pygame.sprite import spritecollide
from helpers import collision


class PhysicsEntity(Entity):
    # Velocities
    x_velocity = 0
    y_velocity = 0

    # Accelerations for simulating jerk wew
    x_acceleration = 0
    y_acceleration = 0

    base_acceleration = 0.5
    base_friction = 0.1

    max_velocity = 10
    max_acceleration = 2

    # Used for collision and stuff
    blocked_top = False
    blocked_bottom = False
    blocked_right = False
    blocked_left = False

    # Other properties
    gravity = 1
    jump_velocity = 5
    jumping = False
    falling = True

    def __init__(self, rect=None, image=None, x_velocity=0, y_velocity=0, max_velocity=10, gravity=1, falling=True,
                 jumping=False, *args, **kwargs):
        super(PhysicsEntity, self).__init__(rect=rect, image=image, *args, **kwargs)

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.max_velocity = max_velocity

        self.x_acceleration = 0
        self.y_acceleration = 0

        self.gravity = gravity
        self.jumping = jumping
        self.falling = falling

    def update(self, tilemap=None, entities=None, **kwargs):
        if(self.gravity != 0 and self.gravity is not None):
            if self.falling:
                self.y_velocity += self.gravity

        self.x_velocity += self.x_acceleration
        self.y_velocity += self.y_acceleration

        velocity = math.sqrt(math.pow(self.x_velocity, 2) + math.pow(self.y_velocity, 2))

        if velocity > self.max_velocity:
            direction = math.atan2(self.y_velocity, self.x_velocity)
            self.y_velocity = math.sin(direction)*self.max_velocity
            self.x_velocity = math.cos(direction)*self.max_velocity
        self.handle_collisions(tilemap, entities=entities)

        if (self.x_velocity > 0 and not self.blocked_right) \
                or (self.x_velocity < 0 and not self.blocked_left):
            self.rect.x += self.x_velocity

        if (self.y_velocity > 0 and not self.blocked_bottom) \
                or (self.y_velocity < 0 and not self.blocked_top):
            self.rect.y += self.y_velocity

    def handle_collisions(self, tilemap, entities=None, **kwargs ):
        if tilemap:
            collisions = []

            for x in tilemap:
                if x.collides:
                    collisions += spritecollide(self, x, False)

            self.blocked_top = False
            self.blocked_bottom = False
            self.blocked_right = False
            self.blocked_left = False

            newrect = self.rect.move(self.x_velocity, self.y_velocity)

            if collisions:
                for tile in collisions:
                    self.on_tile_collide(tile, entities ,**kwargs)
                    if collision.top(newrect, tile.rect):  # Moving down; Hit the top side of the wall
                        self.y_velocity = 0
                        self.y_acceleration = 0
                        self.rect.bottom = tile.rect.top

                        self.blocked_bottom = True

                    # For gravity
                    if collision.top(self.rect.move(0, 5), tile.rect):
                        self.jumping = False
                        self.falling = False
                        self.blocked_bottom = True
                    else:
                        self.falling = True

                    if collision.bottom(newrect, tile.rect):  # Moving up; Hit the bottom side of the wall
                        self.y_velocity = 0
                        self.y_acceleration = 0
                        self.jumping = False

                        if self.rect.top < tile.rect.bottom:
                            self.rect.top = tile.rect.bottom

                        self.blocked_top = True


                    if collision.left(newrect, tile.rect):  # Moving right; Hit the left side of the wall
                        self.x_velocity = 0
                        self.x_acceleration = 0

                        if self.rect.right > tile.rect.left:
                            self.rect.right = tile.rect.left

                        self.blocked_right = True

                    if collision.right(newrect, tile.rect):  # Moving left; Hit the right side of the wall
                        self.x_velocity = 0
                        self.x_acceleration = 0

                        if self.rect.left < tile.rect.right:
                            self.rect.left = tile.rect.right

                        self.blocked_left = True

    def move_up(self):
        self.y_acceleration = -self.base_acceleration

    def move_down(self):
        self.y_acceleration = self.base_acceleration

    def move_left(self):
        self.x_acceleration = -self.base_acceleration

    def move_right(self):
        self.x_acceleration = self.base_acceleration

    def slow(self):
        self.slowX()
        self.slowY()

    def slowY(self):
        if self.y_velocity > self.base_friction:
            self.y_acceleration = - self.base_friction
        elif self.y_velocity < -self.base_friction:
            self.y_acceleration = self.base_friction
        else:
            self.y_acceleration = 0
            self.y_velocity = 0

    def slowX(self):
        if self.x_velocity > self.base_friction:
            self.x_acceleration = - self.base_friction
        elif self.x_velocity < -self.base_friction:
            self.x_acceleration = self.base_friction
        else:
            self.x_acceleration = 0
            self.x_velocity = 0

    def on_tile_collide(self, tile,entities, **kwargs):
        pass

