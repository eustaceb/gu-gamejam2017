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
        self.power = 10000.0

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
                distance = math.sqrt(distance)
                vx = c.rect.centerx - self.rect.centerx
                vx /= distance
                vy = c.rect.centery - self.rect.centery
                vy /= distance

                c.max_velocity = 200
                c.y_velocity = vx * 10
                c.x_velocity = -abs(vy * 10.0)
                c.x_acceration = 0
                c.y_acceleration = 0
                c.falling = True
                print(vx,vy)
                

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
