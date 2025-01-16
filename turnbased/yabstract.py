
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
    lazy_image = False
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        #will need to have reference to the game it participates:
        #self.game = None
        #positions in lists of visible items or mouse listeners in given game:
        self.pos_in_visible = None
        self.pos_in_mouse_listeners = None
        self.placer = None

    def toggle_visible(self):
        #toggle visibility should always be deep.
        self.game.toggle_visible(self)

    def toggle_is_mouse_listener(self):
        #mouse listener is always shallow
        self.game.toggle_is_mouse_listener(self)

    def place(self, rect):
        '''
        Places given yDraw inside given rect, using
        :param surface:
        '''
        assert hasattr(self, 'placer') and self.placer is not None, f"{self}: has no placer"
        assert hasattr(self.placer, 'place'), f"{self}: placer {self.placer} has no method place"
        assert callable(self.placer.place), f"{self}: placer {self.placer} has no method place"
        self.dest_rect = self.placer.place( rect)


    def check_placer(self,placer):
        return isinstance(placer, self.placer_type)

    def set_placer(self,placer):
        assert self.check_placer(placer), f"{self} : trying to set wrong placer type {placer}"
        self.placer = placer


    def draw(self, surface,*args,**kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} is subclass of yDraw and  does not implement __draw__ method")

    def mouse_react(self, game, mouse_pos):
        raise RuntimeError(f"{self.__class__}.mouse_react not implemented")

    def __repr__(self):
        return f"<{type(self).__name__} '{self.name}': visible={self.pos_in_visible}, is_mouse_listener={self.pos_in_mouse_listeners}>"

    def __str__(self):
        return f"<{self.__class__.__name__} : {self.name}>"



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

    def draw(self, surface,  special_flags=0):

        surface.blit(self.image, self.dest_rect,self.area, special_flags )

    def rect(self):
        return self.image.get_rect()




class yLazyImagePattern(yDraw):
    '''
    Image, what calls create method before displaying with surface.blit,
    if self.image is None
    '''
    lazy_image = True
    def __init__(self,name, area = None):
        yDraw.__init__(self, name)
        self.area = None
        self.image = None
        if not hasattr(self,"create_image") or not callable(self.create_image):
            raise NotImplementedError(f"{self.__class__.__name__} is subclass of yLazyImagePattern does not implement create_image method")

    def draw(self, surface, special_flags=0):
        if not self.image:
            self.create_image(surface.get_width(),surface.get_height())

        surface.blit(self.image, self.dest_rect,self.area, special_flags )


class yLazyImageGenFixedSize(yDraw):
    '''
    Image, what calls create method before displaying with surface.blit,
    if self.image is None
    '''
    lazy_image = True
    def __init__(self,name, area = None):
        yDraw.__init__(self, name)
        self.area = None
        self.image = None
        if not hasattr(self,"create_image") or not callable(self.create_image):
            raise NotImplementedError(f"{self.__class__.__name__} is subclass of yLazyImagePattern does not implement create_image method")

    def draw(self, surface, special_flags=0):
        if not self.image:
            self.create_image()
        surface.blit(self.image, self.dest_rect,self.area, special_flags )


class yOneToOnePlacer:

    def __init__(self,name):
        assert isinstance(name, str) , f"yOneToOnePlacer.__init__: wrong {name=}"
        self.name = name
        if not hasattr(self, "__place_inner__") or not callable(self.__place_inner__):
            raise NotImplementedError(
                f"{self.__class__.__name__} is subclass of yOneToOnePlacer does not implement __place_inner__ method")
        self.set_next_placer(None)

    def set_next_placer(self,nextPlacer):
        if nextPlacer is None:
            self.place = self.__place_inner__
        else:
            assert isinstance(nextPlacer, yOneToOnePlacer), f"<#yOneToOnePlacer : wrong placer set : {nextPlacer}"
            self.nextPlacer = nextPlacer
            self.place = self.place_chain




    def place_chain(self,rect):
        print(f"{self} : place_chain")
        own_result = self.__place_inner__(rect)
        return self.nextPlacer.place(own_result)


    def __str__(self):
        return f"<{self.__class__.__name__} : {self.name}>"



class yOneToManyPlacer:
    '''
    Abstraction of a placer, what gains as input one rect
    and returns multiple rects - used for a yContainer what has children.
    Usually, those rects are inside of given rect, but it is not necessary.
    '''
    def __init__(self, name, nextPlacer=None):
        assert isinstance(name, str)
        self.name = name

        if not hasattr(self, "__place_shallow_next__") or not callable(self.__place_shallow_next__):
            raise NotImplementedError(
                f"{self.__class__.__name__} is subclass of yOneToManyPlacer does not implement __place_shallow_next__ method")
        self.set_next_placer(nextPlacer)

    def set_next_placer(self, nextPlacer):
        if nextPlacer is None:
            self.place_next = self.__place_shallow_next__
        else:
            assert isinstance(nextPlacer, yOneToOnePlacer), f"<#yOneToManyPlacer : wrong placer set : {nextPlacer}"
            self.nextPlacer = nextPlacer
            self.place_next = self.place_chain_next

    def place_start(self,rect):
        raise NotImplementedError(f"{self} : place_start not implemented")

    def place_chain_next(self):
        print(f"{self} : place_chain")
        own_result = self.__place_shallow_next__()
        return self.nextPlacer.place(own_result)

    def __str__(self):
        return f"<{self.__class__.__name__} : {self.name}>"


class ySamePlacer(yOneToOnePlacer):

    def __place_shallow__(self,rect):
        return rect



