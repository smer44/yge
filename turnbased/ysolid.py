from yge.turnbased.yabstract import yDraw

class ySolid(yDraw):

    def __init__(self, *color):
        #super().__init__(str(color),True)
        self.color = color
        self.last_rect = None

    def draw(self,surface, dest_rect=None, special_flags=0):
        #print(f"ySolid.draw : {self.color}")
        self.last_rect = surface.fill(self.color,dest_rect,special_flags)
        return

    def rect(self):
        return self.last_rect

    def __repr__(self):
        return f"<ySolid:{self.color}>"

    def __str__(self):
        return f"<ySolid:{self.color}>"


    def mouse_react(self, game,mouse_pos):
        #ignore mouse react for now
        print(f"{self} ignores mouse reaction")
        pass
        #self.bg.mouse_react(game,mouse_pos)