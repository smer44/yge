import pygame

from yge.turnbased.sutil import remove_noholes
from yge.turnbased.yabstract import yDraw
from yge.turnbased.sutil import typecheck

class yGame:

    def __init__(self,root,w,h):
        msg = f"yGame: wrong arguments : {root=} , {w=} , {h=}"
        check = typecheck(msg, root,yDraw,w,(int|float), h, (int|float))
        if check:
            raise TypeError(check)
        self.root = root
        self.set_mode(w,h)
        self.clock = pygame.time.Clock()
        self.mouse_listeners = []
        self.visible = []

    def __str__(self):
        return "<|yGame:{self.root}|>"

    def set_mode(self,w,h):
        self.surface = pygame.display.set_mode((w, h))

    def mouse_react(self,mouse_pos):
        for listener in self.mouse_listeners:
            #get first component what would react on mouse_pos:
            if listener.rect().collidepoint(mouse_pos):
                listener.mouse_react(self,mouse_pos)

    def toggle_in_list(self,lst,item):
            #ml = self.mouse_listeners
            if item.pos_in_mouse_listeners is None:
                pos = len(lst)
                lst.append(item)
                return pos
                #item.pos_in_mouse_listeners = pos
            else:
                pos = item.pos_in_mouse_listeners
                remove_noholes(lst, pos)
                #item.pos_in_mouse_listeners = None
                return None

    def toggle_is_mouse_listener(self,item):
        item.pos_in_mouse_listeners=  self.toggle_in_list(self.mouse_listeners,item)

    #TODO - but visible item should render in order, while
    #order does/should not matter for mouse listener
    def toggle_is_visible(self,item):
        item.pos_in_visible =  self.toggle_in_list(self.visible,item)



    def add_deep(self,item):
        assert isinstance(item,yDraw)
        lst = self.visible
        pos = len(lst)
        lst.append(item)
        item.visible = pos
        lst = self.mouse_listeners
        pos = len(lst)
        lst.append(item)
        item.pos_in_mouse_listeners = pos


        if hasattr(item,'children'):
            for child in item.children:
                self.add_deep(child)



    def run(self):
        root = self.root
        surface = self.surface
        clock = self.clock
        loop = True
        while loop:
            clock.tick(60)
            root.draw(surface)
            pygame.display.update()

            for event in pygame.event.get():
                #print("event : " , event.type)
                if event.type == pygame.QUIT:
                    loop = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.mouse_react(mouse_pos)



