from game_objects.PhysicsEntity import PhysicsEntity
from pygame.surface import Surface
import random
from Explosion import *

class Bomb(PhysicsEntity):

    def __init__(self, rect, image, player=None, **kwargs):
        image = Surface((rect.width, rect.height))
        image.fill((255, 100, 0))
        if Bomb.bombimage == None:
            Bomb.bombimage = pygame.image.load("./assets/bomb.png").convert_alpha()

        self.exploding = False
        
        super(Bomb, self).__init__(rect, Bomb.bombimage, **kwargs)

    def update(self, tilemap=None, entities=None, camera=None, **kwargs):
        super(Bomb, self).update(tilemap, entities, camera=camera)
    
    def on_tile_collide(self, tile,entities, **kwargs):
        self.x_velocity = 0
        self.y_velocity = 0
        self.exploding = True
        explosion = Explosion(pygame.Rect(self.rect.topleft,(128,128)))
        explosion.rect.center = self.rect.center
        entities.append(explosion)
        for g in self.groups():
            g.remove(self)

Bomb.bombimage = None
