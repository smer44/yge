from yge.turnbased.yabstract import yImage, yLazyImagePattern

import pygame
from pygame import Surface
import datetime
import numpy as np
#for efficiency, use numpy for render


class yFillChess(yLazyImagePattern):

    def __init__(self,name):
        super().__init__(name)

        self.color1 = (100,100,100)
        self.color2 = (150, 150, 150)
        self.xycell = 50


    def create_image(self,width,height):
        print("render start :" , datetime.datetime.now())
        #this last for one damn second!
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



