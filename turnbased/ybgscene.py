from yge.turnbased.yscene import yScene

class yBgScene(yScene):

    def __init__(self,name, bg, *items):
        super().__init__(name,*items)
        self.bg = bg

    def set_dirty_deep(self):
        """
        yBgScene can be  redrawn only
        with background and all its
        components, what are visible
        :return:
        """
        self.dirty_var = True
        self.bg.set_dirty_deep()
        for items in self.items:
            items.set_dirty_deep()


    def redraw(self,display):

        if self.dirty_var:
            #print("yBgScene.redrawing")
            self.bg.redraw(display)
            for item in self.items:
                item.redraw(display)
            self.dirty_var = False