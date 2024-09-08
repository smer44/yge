class yVariantItem:
    def __init__(self, name, *items):
        assert isinstance(name, str), f"first parameter of yVariantItem.__init__ must be a string"
        self.name = name
        self.items = list(items)
        self.chosen = 0

    def __repr__(self):
        return f"<?{type(self).__name__} '{self.name}': chosen={self.chosen}?>"

    def __str__(self):
        return repr(self)

    def next(self):
        """
        Select another component to be displayed.
        There must be at least 2 variants, or else
        it has no sence to call next??

        :return:
        """
        ln = len(self.items)
        assert ln > 1, 0 <= self.chosen < ln
        self.chosen+=1
        if self.chosen == ln:
            self.chosen = 0
        self.set_dirty_deep()

    def item(self):
        return self.items[self.chosen]

    def set_dirty(self):
        self.item().set_dirty()

    def set_dirty_deep(self):
        self.item().set_dirty_deep()

    def dirty(self):
        return self.item().dirty()

    def need_redraw(self):
        self.item().dirty_var()

    def redraw(self, display):
        self.item().redraw(display)

    def mouse_react(self,game, mouse_pos):
        self.item().mouse_react()

