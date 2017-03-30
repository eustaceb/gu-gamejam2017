from game_objects.PhysicsEntity import PhysicsEntity
from pygame.surface import Surface


class Bomb(PhysicsEntity):
    def __init__(self, rect, image, player=None, **kwargs):
        image = Surface((rect.width, rect.height))
        image.fill((255, 100, 0))
        super(Bomb, self).__init__(rect, image, **kwargs)

    def update(self, tilemap=None, entities=None, **kwargs):
        super(Bomb, self).update(tilemap, entities)

