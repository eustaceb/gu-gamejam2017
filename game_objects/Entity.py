import pygame
from pygame.rect import Rect
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

    # Other properties
    gravity = 1
    falling = False
    solid = True
    visible = True

    def __init__(self, rect=None, image=None, x_velocity=0, y_velocity=0, gravity=1, falling=False,
                 solid=True, visible=True):
        super(Entity, self).__init__()

        self.rect = rect
        self.image = image

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.gravity = gravity
        self.falling = falling
        self.solid = solid
        self.visible = visible

    def update(self):
        if self.falling and (self.gravity != 0 and self.gravity is not None):
            self.yvel += self.gravity
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        #Generic Collision code or something

    def render(self, screen):
        if self.image and self.rect and self.visible is True:
           screen.blit(self.image, (self.rect.x, self.rect.y));