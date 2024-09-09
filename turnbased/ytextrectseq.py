from yge.turnbased.ytext import yText
from yge.turnbased.yrect import yRect

class yTextRectSequence(yText,yRect):

    def __init__(self, name, texts, font, textcolor, left,top,width,height,rectcolor, border_width, visible=True):
        yText.__init__(self, name, texts[0], font, textcolor, (left, top),visible)
        yRect.__init_shallow__(self,left,top,width,height,rectcolor,border_width)
        self.texts = texts
        self.texts_pos = 0
        self.loop = False

    def next(self):
        self.texts_pos += 1
        if self.texts_pos >= len(self.texts):
            if self.loop:
                self.texts_pos = 0
                text = self.texts[0]
            else:
                text = ""
        else:
            text = self.texts[self.texts_pos]
        self.render(text)

    def mouse_react(self, game, mouse_pos):
        mx,my = mouse_pos
        if self.is_mouse_listener:
            if self.left <= mx <= self.left+self.width and \
                self.top <= my <= self.top + self.height:
                    self.next()
                    self.set_dirty_deep()

                    game.item.set_dirty()


    def __display__(self,display):
        yRect.__display__(self, display)
        yText.__display__(self, display)

    def __repr__(self):
        return f"<~yTextRectSequence {self.name}, {self.rect}, {self.left}, {self.top} ~>"

    def __str__(self):
        return repr(self)
