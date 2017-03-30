import pygame

from pygame.sprite import Sprite


class Tile(Sprite):

    rect = None
    image = None

    def __init__(self, rect, image):
        super(Tile, self).__init__()
        self.rect = rect
        self.image = image

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect

    def render(self, screen, camera):
        screen.blit(self.image, (self.rect.x-camera.x, self.rect.y-camera.y))
