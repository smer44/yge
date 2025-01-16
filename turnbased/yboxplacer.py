from pygame import Rect

from yge.turnbased.yabstract import  yOneToManyPlacer

direction_to_right = 0
direction_to_bottom = 1
direction_to_left = 2
direction_to_top = 3



class yBoxPlacer(yOneToManyPlacer):

    def __init__(self,name,amount,direction, spacing ):
        yOneToManyPlacer.__init__(self,name)
        self.amount = amount
        assert 0 <= direction <= 3
        self.direction = direction

        self.spacing = spacing
        #self.place_functions = [None,None, self.place_to_right,None][self.direction]

    def __place_shallow_next__(self):
        return self.__place_distinguish__()

    def place_start(self,rect):
        x, y, w, h = rect
        n = self.amount
        sp = self.spacing
        # if it is horizontal direction:
        if self.direction %2 == 0:
            pos = float(x)
            pos_end = x+w
            dim = w
            backup_pair = y,h
            self.__place_distinguish__ = self.place_horizontal
        else:
            pos = float(y)
            pos_end = y+h
            dim = h
            backup_pair = x, w
            self.__place_distinguish__ = self.place_vertical

        #if direction is reversed:
        if self.direction > 1:
            pos, pos_end = pos_end, pos

        child_size = (dim - sp * (n - 1)) / n
        #store parameters:
        self.pos = pos
        self.backup_pair = backup_pair
        self.child_size = child_size
        self.step = child_size + sp
        if self.direction > 1:
            self.step = -self.step


    def place_horizontal(self):
        pos = self.pos
        y,h = self.backup_pair
        child_size = self.child_size
        step = self.step
        r = Rect(pos, y, child_size, h)
        self.pos = pos + step
        return r

    def place_vertical(self):
        pos = self.pos
        x,w = self.backup_pair
        child_size = self.child_size
        step = self.step
        r = Rect(x,pos, w, child_size)
        self.pos = pos + step
        return r


