class yScene:

    def __init__(self,name,*items):
        assert isinstance(name, str)
        self.name = name
        self.dirty_var = True
        self.items = list(items)
        self.is_mouse_listener = True
        self.visible = True

    def __repr__(self):
        return f"<!{type(self).__name__} '{self.name}': dirty={self.dirty_var}, visible={self.visible}!>"

    def __str__(self):
        return repr(self)

    def toggle_deep(self):
        for item in self.items:
            item.toggle_deep()

    def toggle_children(self):
        for item in self.items:
            item.toggle()

    def toggle(self):
        self.visible = not self.visible


    def set_dirty_children(self):
        self.dirty_var = True
        for item in self.items:
            item.set_dirty()


    def set_dirty_deep(self):
        self.dirty_var = True
        for item in self.items:
            item.set_dirty_deep()

    def set_dirty(self):
        self.dirty_var = True

    def dirty(self):
        return self.dirty_var

    def redraw(self, display):
        if self.visible and self.dirty():
            for item in self.items:
                item.redraw(display)

    def mouse_react(self,game, mouse_pos):
        if self.is_mouse_listener:
            for item in self.items:
                item.mouse_react(game,mouse_pos)