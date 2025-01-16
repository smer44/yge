from yge.turnbased.yabstract import yLazyImagePattern, yLazyImageGenFixedSize


class yText(yLazyImageGenFixedSize):
    def __init__(self,name, text,font, color,):
        yLazyImagePattern.__init__(self,name)
        self.font = font
        self.textcolor = color
        self.text = text
        #self.render(text)
        #self.update_pos(topleft)
        #self.update_pos(topleft)
        self.is_mouse_listener = True


    def create_image(self):
        '''
        For now, width and height are ignored.
        :param width:
        :param height:
        :return:
        '''
        text = self.text
        self.image = self.font.render(text, True, self.textcolor)
        #self.set_dirty()


    #def update_pos(self, topleft):
    #    self.rect = self.image.get_rect(topleft =topleft)


    def __repr__(self):
        return f"<TextItem |{self.text[:20]}|>"

    def __str__(self):
        return f"<TextItem |{self.name}|>"


class yTextMouseReact(yText):
    def mouse_react(self, game,mouse_pos):
        if not self.visible:
            print(" -- !! mouse_react in yText is not visible :", self)
            return
        text_rect = self.rect
        if text_rect.collidepoint(mouse_pos):
            #print(" -- !! mouse_react in yText :", self.name, " pressed ", text_rect, "mouse_pos:", mouse_pos)
            print(" -- !! mouse_react in yText :", self)
            game.item.bg.next()
            game.item.set_dirty_deep()