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
        self.power = 50000.0

    def update(self, tilemap=None, entities=None, camera=None, **kwargs):
        camera.centerx += random.randint(-10,10)
        camera.centery += random.randint(-10,10)
        self.image = Explosion.explosion_frames[self.frame//3  ]
       
        self.frame += 1
        npcs = kwargs.get("npcs", None)
        if npcs:
            collisions = spritecollide(self, npcs, False)
            for c in collisions:
                if (c.dead) : continue
                c.dead = True
                distance = (c.rect.centerx - self.rect.centerx)**2 + (c.rect.centery-self.rect.centery)**2
                distance = max(1,distance)
                force = 1.0/distance
                c.max_velocity = 20
                x_dir = -1.0 if c.rect.centerx < self.rect.centerx else 1.0
                velocity_x = force * self.power * x_dir 
                velocity_y = force * self.power * -1.0
                #c.velocity_y = velocity_y
                #c.velocity_x = velocity_x
                c.acceleration_x = x_dir * 2.0
                c.acceleration_y = -2.0
                print("eh?")
                

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
