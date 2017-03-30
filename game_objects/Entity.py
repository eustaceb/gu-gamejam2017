import math
from pygame.sprite import Sprite


#This class represents every entity in the game
class Entity(Sprite):
    # A Rect object specifying the dimensions of the entity
    rect = None

    # An image representing the sprite proper
    image = None

    # Velocities
    x_velocity = 0
    y_velocity = 0

    # Accelerations for simulating jerk wew
    x_acceleration = 0
    y_acceleration = 0

    base_acceleration = 1
    base_friction = 0.1

    max_velocity = 10
    max_acceleration = 2

    # Other properties
    gravity = 1
    jump_velocity = 5
    jumping = False
    falling = False
    solid = True
    visible = True

    def __init__(self, rect=None, image=None, x_velocity=0, y_velocity=0, gravity=1, falling=False,
                 jumping=False, solid=True, visible=True):
        super(Entity, self).__init__()

        self.rect = rect
        self.image = image

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.gravity = gravity
        self.jumping = jumping
        self.falling = falling
        self.solid = solid
        self.visible = visible

    def update(self):

        if self.falling and (self.gravity != 0 and self.gravity is not None):
            self.y_velocity += self.gravity

        self.x_velocity += self.x_acceleration
        self.y_velocity += self.y_acceleration

        velocity = math.sqrt(math.pow(self.x_velocity, 2) + math.pow(self.y_velocity, 2))

        if velocity > self.max_velocity:
            direction = math.atan2(self.y_velocity, self.x_velocity)
            self.y_velocity = math.sin(direction)*self.max_velocity
            self.x_velocity = math.cos(direction)*self.max_velocity

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def render(self, screen):
        if self.image and self.rect and self.visible is True:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_up(self):
        self.y_acceleration = -self.base_acceleration

    def move_down(self):
        self.y_acceleration = self.base_acceleration

    def move_left(self):
        self.x_acceleration = -self.base_acceleration

    def move_right(self):
        self.x_acceleration = self.base_acceleration

    def slow(self):
        if(self.y_velocity > self.base_friction):
            self.y_acceleration = - self.base_friction
        elif(self.y_velocity < -self.base_friction):
            self.y_acceleration = self.base_friction
        else:
            self.y_acceleration = 0

        if (self.x_velocity > self.base_friction):
            self.x_acceleration = - self.base_friction
        elif (self.x_velocity < self.base_friction):
            self.x_acceleration = self.base_friction
        else:
            self.x_acceleration = 0

