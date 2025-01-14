
class sContainer:

    def __init__(self):
        self.children = []


    def add(self,obj):
        self.children.append(obj)

    def deep_children(self):
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            stack.extend(node.children[::-1])


class sRect(sContainer):

    stype = 1

    def __init__(self,x,y,w,h,
                 background= (0,0,0),
                 corner_radius = 0,
                 vertical = True,
                 xpad = 0,
                 ypad = 0,
                 itemGap = 0,
                 ):
        #padding ( around)
        #itemGap (betwen items
        # move this to a placer?
        #minSize
        #size relative to parent (top down influence)
        #there can be also bottom up influence


        sContainer.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background = background
        self.corner_radius = corner_radius
        self.vertical = vertical
        self.xpad = xpad
        self.ypad= ypad
        self.itemGap = itemGap

    def rect(self):
        return (self.x,self.y, self.w, self.h)


