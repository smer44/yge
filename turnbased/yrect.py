from yge.turnbased.yitem import yItem
import pygame

class yRect(yItem):

    def __init__(self, name,left,top,width,height,color,border_width,visible=True):
        super().__init__(name,visible)
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.color = color
        self.border_width = border_width

    def xpos(self,x):
        self.left  = x
        self.set_dirty()

    def ypos(self,y):
        self.top  = y
        self.set_dirty()

    def __display__(self, display):
        #print(f'yRect.__display__ {self.rect=}')
        rect = (self.left, self.top, self.width, self.height)
        pygame.draw.rect(display, self.color, rect, self.border_width)




