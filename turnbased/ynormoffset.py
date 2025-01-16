from yge.turnbased.yabstract import yOneToOnePlacer


class yNormOffsetPlacer(yOneToOnePlacer):
    '''
    Offsets original rectangle by given x,y coordinates
    what are given normalized to 0..1 in width and height of
    given rectangle
    '''

    def __init__(self,name,nx,ny):
        yOneToOnePlacer.__init__(self,name)
        self.nx =nx
        self.ny = ny

    def __place_inner__(self,rect):
        x,y,w,h = rect
        nx = int(self.nx * w)
        ny = int(self.ny * h)
        #return (x+nx, y+ny, w,h)
        return rect.move(nx,ny)