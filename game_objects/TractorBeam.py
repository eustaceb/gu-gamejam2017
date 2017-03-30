import pygame

from .Entity import Entity


class TractorBeam(Entity):
    player = None
    enabled = True

    key_activate = pygame.K_LSHIFT

    def __init__(self, rect, player=None, **kwargs):
        self.player = player
        super(TractorBeam, self).__init__(rect, pygame.image.load("assets/alien_beam.png"), **kwargs)


    def update(self, *args):
        key = pygame.key.get_pressed()

        if key[self.key_activate] and self.player.x_velocity==0:
            self.enabled = True
        else:
            self.enabled = False

        if(self.player):
            self.rect.midtop = (self.player.rect.midbottom[0], self.player.rect.midbottom[1]-50)

        super(Entity, self).update()

    def render(self, screen, camera):
        if(self.enabled):
            super(TractorBeam, self).render(screen, camera)
