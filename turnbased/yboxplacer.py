from yge.turnbased.yabstract import  yOneToManyPlacer

direction_to_left = 0
direction_to_right = 2
direction_to_top = 1
direction_to_bottom = 3

class yBoxPlacer(yOneToManyPlacer):

    def __init__(self,amount,direction, spacing ):
        yOneToManyPlacer.__init__(self)
        self.amount = amount
        self.direction = direction
        self.spacing = spacing
        self.place_functions = [None,None, self.place_to_right,None][self.direction]

    def __place_shallow__(self,rect):
        return self.place_functions(rect)


    def place_to_right(self, rect):
        x, y, w, h = rect
        n = self.amount
        sp = self.spacing
        xx = float(x)
        xmax = x+w
        size = (w - sp*(n-1))/n
        isize = int(size)
        step = size + sp
        ret = []
        while xx < xmax:
            ret.append( (int(xx),y,isize, h))
            xx += step
        return ret


ypa = yBoxPlacer(3,direction_to_right, 100)

x = ypa.place_to_right((0,0,1920,1080))

print(x)





