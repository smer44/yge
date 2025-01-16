from yge.turnbased.ycontainer import yContainer


class yFrame(yContainer):
    '''
    Frame has a background and some items on it - other items are inherited from yItem
    and are drawn after background is drawn.
    All components should be inside background instance.
    '''
    def __init__(self,name, bg, *items):
        super().__init__(name,*items)
        self.bg = bg

    def draw(self,screen):
        self.bg.draw(screen)
        yContainer.draw(self,screen)


    def place(self,rect):
        self.bg.place(rect)
        yContainer.place(self,rect)


    def rect(self):
        return self.bg.rect()

    def mouse_react(self, game,mouse_pos):
        self.bg.mouse_react(game,mouse_pos)