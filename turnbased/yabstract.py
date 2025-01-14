
class yDraw:
    '''
    Abstract class of anything what can draw on to pygame display
    it can have a name,
    or be currently visible/invisible, listen to the mouse or not.
    If it gets visible/invisible, or mouse listener/not,
    it updates list of reference to components for given ygame
    "dirty" mechanics should be excluded by now, since
    even if child is updated, all parents and all children should be
    redrawn in general case if you do not use region clipping,
    but it is complicated and not nessesary in turn based 2d logic now.
    '''

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        #will need to have reference to the game it participates:
        #self.game = None
        #positions in lists of visible items or mouse listeners in given game:
        self.pos_in_visible = None
        self.pos_in_mouse_listeners = None

    def toggle_visible(self):
        #toggle visibility should always be deep.
        self.game.toggle_visible(self)

    def toggle_is_mouse_listener(self):
        #mouse listener is always shallow
        self.game.toggle_is_mouse_listener(self)

    def draw(self, surface,*args,**kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} is subclass of yDraw and  does not implement __draw__ method")

    def mouse_react(self, game, mouse_pos):
        raise RuntimeError(f"{self.__class__}.mouse_react not implemented")

    def __repr__(self):
        return f"<{type(self).__name__} '{self.name}': visible={self.pos_in_visible}, is_mouse_listener={self.pos_in_mouse_listeners}>"

    def __str__(self):
        return f"<{self.__class__.__name__}>"



class yImage(yDraw):
    '''
    Stands for PyGame surface, on what something is draw.
    Creates field .image in some way and blits it into given display.
    '''
    def __init__(self,name, area = None):
        yDraw.__init__(self, name)
        #area what is selected from given image
        self.area = None
        self.image = None

    def draw(self, surface, dest_rect=None, special_flags=0):
        surface.blit(self.image, dest_rect,self.area, special_flags )


class yLazyImagePattern(yDraw):
    '''
    Image, what calls create method before displaying with surface.blit,
    if self.image is None
    '''
    def __init__(self,name, area = None):
        yDraw.__init__(self, name)
        self.area = None
        self.image = None
        if not hasattr(self,"create_image") or not callable(self.create_image):
            raise NotImplementedError(f"{self.__class__.__name__} is subclass of yLazyImagePattern does not implement create_image method")

    def draw(self, surface, dest_rect=None, special_flags=0):
        if not self.image:
            self.create_image(surface.get_width(),surface.get_height())
        if dest_rect is None:
            dest_rect = (0,0)
        surface.blit(self.image, dest_rect,self.area, special_flags )