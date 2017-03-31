import random

import pygame
from pygame.rect import Rect

from game_objects.NPC import NPC


class Villager(NPC):

    def __init__(self, x, y, **kwargs):
        races = ["white", "brown", "yellow"]
        colours = ["blue", "green", "pink", "red"]
        image = pygame.image.load("assets/block_guy_"+random.choice(races)+"_"+random.choice(colours)+".png")
        self.hitsound = pygame.mixer.Sound("assets/sounds/yellgroan.wav")
        super(Villager, self).__init__(image=image, rect=Rect(x, y, 32, 32), max_velocity=random.randint(7,9),**kwargs)
