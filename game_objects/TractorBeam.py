import pygame

from .Entity import Entity


class TractorBeam(Entity):
    player = None
    enabled = True
    capacity = 100
    recharging = False
    charge_rate = 0.5

    key_activate = pygame.K_LSHIFT

    def __init__(self, rect, player=None, **kwargs):
        self.player = player
        super(TractorBeam, self).__init__(rect, pygame.image.load("assets/alien_beam2.png"), **kwargs)


    def update(self, *args):
        key = pygame.key.get_pressed()

        self.enabled = False
        if key[self.key_activate]:
            if self.capacity > 1 and not self.recharging:
                self.enabled = True
                self.capacity -= 1
            elif self.capacity <= 1:
                self.recharging = True
        else:
            if(self.capacity < 100):
                self.capacity = min(100, self.capacity+self.charge_rate)

            if(self.recharging):
                if(self.capacity==100):
                    self.recharging = False

        if(self.player):
            self.rect.midtop = (self.player.rect.midbottom[0], self.player.rect.midbottom[1])

        super(Entity, self).update()

    def render(self, screen, camera):
        if(self.enabled):
            super(TractorBeam, self).render(screen, camera)
