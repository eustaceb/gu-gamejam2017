class Tile:
    def __init__(self, x, y, width, height, res):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.resource = res

    def get_pos(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_resource(self):
        return self.resource

    def get_image(self):
        return self.resource.get_image()