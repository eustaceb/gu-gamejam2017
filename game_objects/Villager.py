from enum import Enum

from . import Entity

# A villager that lives in the village
class Villager(Entity):

    direction = Direction.LEFT

    def update(self):
        if self.direction == Direction.LEFT:
            self.move_left()
        elif self.direction == Direction.RIGHT:
            self.move_right()
        else:
            self.stop()

        super(Villager, self).update()



class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    STATIONARY = 2