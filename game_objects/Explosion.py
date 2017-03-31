import random
import pygame
from pygame.sprite import Sprite
from PhysicsEntity import *

explosion_frames = None


class Explosion(Sprite):
    def __init__(self, rect):
        super(Explosion, self).__init__()
        if Explosion.explosion_frames == None:
            Explosion.explosion_frames = [pygame.image.load("./assets/explosion%d.png"%(x)).convert_alpha() for x in xrange(6)]
        self.image = Explosion.explosion_frames[0]
        self.rect = rect
        self.frame = 0

    def update(self, tilemap=None, entities=None, camera=None, **kwargs):
        camera.centerx += random.randint(-10,10)
        camera.centery += random.randint(-10,10)
        self.image = Explosion.explosion_frames[self.frame//3  ]
       
        self.frame += 1
        if self.frame >= len(Explosion.explosion_frames)*3:
            for g in self.groups():
                g.remove(self)
            entities.remove(self)

    def render(self, screen, camera=None):
        if camera:
            screen.blit(self.image, (self.rect.x-camera.x, self.rect.y-camera.y))
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        

Explosion.explosion_frames = None
