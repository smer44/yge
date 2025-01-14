
class BoxPlacer:

    def __call__(self,obj):
        itemAmount = len(obj.children)
        if itemAmount > 0:
            yield from self.place(obj.rect(),itemAmount,obj.vertical,obj.xpad, obj.ypad, obj.itemGap  )


    def place(self,rect,itemAmount,vertical, xpad,ypad, itemGap):
        x,y,w,h = rect
        x = x+xpad
        y = y+ypad
        w = w-xpad - xpad
        y = h-ypad - ypad
        xmax= x+w
        ymax = y + h
        step = w // itemAmount
        if vertical:
            for n in range(itemAmount):
                ynext = y + step
                yield (x,y+itemGap,xmax,ynext - itemGap)
                y = ynext
        else:
            for n in range(itemAmount):
                xnext = x + step
                yield (x+itemGap,y,xnext-itemGap,ymax)
                x = xnext
