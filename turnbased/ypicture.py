import pygame

from yge.turnbased.yabstract import yImage


class yPicture(yImage):

    path = "image/"
    ext = ".png"

    def __init__(self, name):
        yImage.__init__(self, name)
        #self.load()

    def load(self):
        self.image =  pygame.image.load(self.full_file_name()).convert_alpha()

    def full_file_name(self):
        return f"{self.path}{self.name}{self.ext}"

