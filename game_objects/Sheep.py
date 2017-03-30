from NPC import NPC


class Sheep(NPC):

    def __init__(self):
        image = pygame.image.load("assets/sheep.png")
        super(Sheep, self).__init__(image=image, rect="")