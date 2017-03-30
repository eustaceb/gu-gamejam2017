import random

import pygame
from pygame.rect import Rect

from game_objects.NPC import NPC


class Villager(NPC):

    def __init__(self, x, y):
        races = ["white", "brown", "yellow"]
        colours = ["blue", "green", "pink", "red"]
        image = pygame.image.load("assets/block_guy_"+random.choice(races)+"_"+random.choice(colours)+".png")
        super(Villager, self).__init__(image=image, rect=Rect(x,y,4,8))