import pygame
from pygame.rect import Rect

from .NPC import NPC

class Cthulhu(NPC):

    def __init__(self, x, y, **kwargs):
        image = pygame.image.load("assets/cthulhu_full.png")
        self.original = image
        super(Cthulhu, self).__init__(image=image, rect=Rect(x, y, 259, 259), max_velocity=4, **kwargs)
