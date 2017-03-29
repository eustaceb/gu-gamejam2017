from pygame.sprite import Sprite

#This class represents every entity in the game

class Entity(Sprite):
    # A Rect object specifying the dimensions of the entity
    rect = None

    # An image representing the sprite proper
    image = None

    # Velocities
    x_velocity = 0
    y_velocity = 0

    base_acceleration = 5
    max_velocity = 10

    # Other properties
    gravity = 1
    jump_velocity = 5
    jumping = False
    falling = False
    solid = True
    visible = True

    def __init__(self, rect=None, image=None, x_velocity=0, y_velocity=0, gravity=1, falling=False,
                 jumping=False, solid=True, visible=True):
        super(Entity, self).__init__()

        self.rect = rect
        self.image = image

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.gravity = gravity
        self.jumping = jumping
        self.falling = falling
        self.solid = solid
        self.visible = visible

    def update(self):
        if self.falling and (self.gravity != 0 and self.gravity is not None):
            self.yvel += self.gravity

        self.

        #Generic Collision code or something

    def render(self, screen):
        if self.image and self.rect and self.visible is True:
            self.screen.blit(self.image, self.rect);

    def jump(self):
        if self.jumping is False and self.falling is False:
            self.jumping = True
            self.y_velocity = -self.jump_velocity
