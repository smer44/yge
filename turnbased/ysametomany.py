from yge.turnbased.yabstract import yOneToManyPlacer, yOneToOnePlacer


class ySamePlacer(yOneToOnePlacer):

    def __place_inner__(self,rect):
        return rect#.copy()


class ySameToManyPlacer(yOneToManyPlacer):
    '''
    Identity placer, what just repeat the rectangle given
    '''
    def __init__(self,name):
        yOneToManyPlacer.__init__(self,name)

    def place_start(self,rect):
        self.rect = rect

    def __place_shallow_next__(self):
        return self.rect.copy()






