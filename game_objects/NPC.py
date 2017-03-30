import random

from enum import Enum

from .PhysicsEntity import PhysicsEntity


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    STATIONARY = 2


# A villager that lives in the village
class NPC(PhysicsEntity):

    direction = Direction.LEFT

    def update(self):
        if self.direction == Direction.LEFT:
            self.move_left()
        elif self.direction == Direction.RIGHT:
            self.move_right()
        else:
            self.stop()

        switch_direction = random.randint(0,1000)
        if switch_direction == 0:
            if self.direction == Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                self.direction = Direction.LEFT
        elif switch_direction == 1000:
            self.direction = Direction.STATIONARY

        if(not self.blocked_bottom):
            falling = True

        super(NPC, self).update()