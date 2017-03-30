import pygame
def alpha_convert(image):
    for x in xrange(image.get_width()):
        if image.get_at((x,0))[3] != 255 or image.get_at((x,image.get_height()-1))[3] != 255: return image.convert_alpha()
    for y in xrange(image.get_height()):
        if image.get_at((0,y))[3] != 255 or image.get_at((image.get_width()-1,y))[3] != 255: return image.convert()
    return image.convert() 

class Resource:
    def __init__(self, resource_id, name, filename, resource_type):
        self.id = resource_id
        self.name = name
        self.image = alpha_convert(pygame.image.load(filename))
        self.type = resource_type

    def get_id(self):
        return self.id

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


