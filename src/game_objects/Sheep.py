import pygame
from pygame.rect import Rect

from NPC import NPC


class Sheep(NPC):

    def __init__(self, x, y, **kwargs):
        image = pygame.image.load("assets/sheep.png")
        self.original = image
        super(Sheep, self).__init__(image=image, rect=Rect(x, y, 32, 32), max_velocity=3, **kwargs)

    def render(self, screen, camera):
        if(self.x_velocity > 0):
            center = self.rect.center
            self.image = pygame.transform.flip(self.original, True, False)
            self.rect.center = center
        else:
            center = self.rect.center
            self.image = self.original
            self.rect.center = center

        super(Sheep, self).render(screen, camera)