from yge.turnbased.ytext import yText

class yTextSequence(yText):

    def __init__(self,name,texts,font, color,topleft,visible=True):
        super().__init__(name, texts[0],font, color,topleft,visible)
        self.texts = texts
        self.pos = 0
        self.loop = False

    def next(self):
        self.pos+=1
        if self.pos >= len(self.texts):
            if self.loop:
                self.pos = 0
                text = self.texts[0]
            else:
                text = ""
        else:
            text = self.texts[self.pos]
        self.render(text)


    def mouse_react(self, game, mouse_pos):
        text_rect = self.rect
        if text_rect.collidepoint(mouse_pos):
            self.next()
            game.item.set_dirty_deep()



