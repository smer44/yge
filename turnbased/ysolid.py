from yge.turnbased.yabstract import yDraw, yOneToOnePlacer


class ySolid(yDraw):



    def __init__(self,name, *color):
        yDraw.__init__(self,name)
        self.color = color
        self.last_rect = None


    def draw(self,surface, special_flags=0):
        #print(f"{self}:draw: dest_rect={self.dest_rect}")
        self.last_rect = surface.fill(self.color,self.dest_rect,special_flags)
        return

    def rect(self):
        return self.last_rect

    def __repr__(self):
        return f"<ySolid:{self.name}:{self.color}>"

    def __str__(self):
        return f"<ySolid:{self.name}:{self.color}>"


    def mouse_react(self, game,mouse_pos):
        #ignore mouse react for now
        print(f"{self} ignores mouse reaction")
        pass
        #self.bg.mouse_react(game,mouse_pos)