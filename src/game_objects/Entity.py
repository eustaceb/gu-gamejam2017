from pygame.sprite import Sprite
import pygame


#This class represents every entity in the game
class Entity(Sprite):
    # A Rect object specifying the dimensions of the entity
    rect = None

    # An image representing the sprite proper
    image = None

    solid = True
    visible = True

    def __init__(self, rect, image, solid=True, visible=True):
        super(Entity, self).__init__()

        self.rect = rect
        self.image = pygame.transform.scale(image, rect.size)

        self.solid = solid
        self.visible = visible

    def update(self, **kwargs):
        pass

    def render(self, screen, camera):
        if self.image and self.rect and self.visible is True:
            screen.blit(self.image, (self.rect.x-camera.x, self.rect.y-camera.y))
