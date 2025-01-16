from yge.turnbased.yabstract import yDraw


class yContainer(yDraw):
    def __init__(self, name,*children):
        yDraw.__init__(self,name)
        self.children = list(children)
        #TODO - also can have placer of children


    def draw(self, surface):
        for child in self.children:
            child.draw(surface)

    def place(self,rect):
        assert hasattr(self, 'placer') and self.placer is not None, f"{self}: has no placer"
        assert hasattr(self.placer, 'place_start'), f"{self}.place called: placer has no method place_start"
        assert hasattr(self.placer, 'place_next'), f"{self}.place called: placer has no method place_next"
        assert callable(self.placer.place_start), f"{self}.place called: placer.place_start is not callable"
        assert callable(self.placer.place_next), f"{self}.place called: placer.place_next is not callable"
        placer = self.placer
        placer.place_start(rect)
        for child in self.children:
            child.place(placer.place_next())



