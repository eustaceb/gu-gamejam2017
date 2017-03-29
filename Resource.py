import pygame


class Resource:
    def __init__(self, resource_id, name, filename, resource_type):
        self.id = resource_id
        self.name = name
        self.image = pygame.image.load(filename)
        self.type = resource_type

    def get_id(self):
        return self.id

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type
