from yge.turnbased.yabstract import yRectPlacer


class yPaddingPlacer(yRectPlacer):

    def __init__(self, left,top,right = None, bottom = None):
        yRectPlacer.__init__(self)
        self.left = left
        self.top = top
        self.right = left if right is None else right
        self.bottom = top if bottom is None else bottom

    def place(self, rect):
        x,y,w,h = rect
        return (x+self.left, y+self.top, w-self.left-self.right, h-self.bottom-self.top)


