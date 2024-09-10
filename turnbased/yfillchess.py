from yge.turnbased.yitem import yItem
import pygame
from pygame import Surface
import datetime
import numpy as np
#for efficiency, use numpy for render


class yFillChess(yItem):

    def __init__(self,):
        super().__init__("yFillChess",True)

        self.color1 = (100,100,100)
        self.color2 = (150, 150, 150)
        self.xycell = 50
        self.image = None



    def __repr__(self):
        return f"<yFillChess>"

    def __str__(self):
        return f"<yFillChess>"

    def render(self,display):
        print("render start :" , datetime.datetime.now())
        #this last for one damn second!
        width = display.get_width()
        height = display.get_height()
        image = Surface((width,height))

        cell_size = self.xycell
        white = np.array(self.color1, dtype=np.uint8)
        black = np.array(self.color2, dtype=np.uint8)
        colors = [white, black]
        chessboard = np.zeros((width, height, len(white)), dtype=np.uint8)

        self.image = image
        yodd = False
        for y in range(0, height, cell_size):
                yodd = not yodd
                odd = yodd
                for x in range(0,width,cell_size):
                    odd = not odd
                    color = colors[odd]
                    chessboard[x:x + cell_size, y:y + cell_size] = color
        pygame.surfarray.blit_array(image, chessboard)

        print("render end :", datetime.datetime.now())

    def __display__(self, display):
        if not self.image:
            self.render(display)
        display.blit(self.image, (0,0))




