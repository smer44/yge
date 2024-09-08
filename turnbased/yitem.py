class yItem:

    def __init__(self,name = None, visible=True):
        assert isinstance(name, str)
        self.name = name
        self.dirty_var = True
        self.visible = visible
        self.is_mouse_listener = True

    def __repr__(self):
        return f"<{type(self).__name__} '{self.name}': dirty={self.dirty_var}, visible={self.visible}>"

    def __str__(self):
        return repr(self)

    def set_dirty(self):
        #print(f"{self}.set_dirty")
        self.dirty_var = True

    def set_dirty_deep(self):
        #print(f"{self}.set_dirty_deep")
        self.dirty_var = True

    def dirty(self):
        return self.dirty_var

    def redraw(self, display):
        #print(f"  {self}: redraw called, visible: " , self.visible)
        if self.visible and self.dirty():
            self.__display__(display)
            self.dirty_var = False

    def toggle(self):
        self.visible = not self.visible
        self.set_dirty()

    def toggle_deep(self):
        self.visible = not self.visible
        self.set_dirty_deep()

    def __display__(self,display):
        raise RuntimeError(f"{self.__class__}.__display__ not implemented")

    def mouse_react(self, game, mouse_pos):
        if self.is_mouse_listener:
            raise RuntimeError(f"{self.__class__}.mouse_react not implemented")



