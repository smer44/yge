from yitem import yItem
class yText(yItem):
    def __init__(self,name, text,font, color,topleft,visible=True):
        super().__init__(name,visible)
        self.font = font
        self.color = color
        self.render(text)
        self.update_pos(topleft)
        #self.update_pos(topleft)
        self.is_mouse_listener = True


    def render(self, text):
        """
        This draws the text image again and must be called if
        either text message or color has changed
        :param text:
        :param color:
        :return:
        """
        self.text = text
        self.image = self.font.render(text, True, self.color)


    def update_pos(self, topleft):
        self.rect = self.image.get_rect(topleft =topleft)


    def __display__(self,display):
        display.blit(self.image, self.rect.topleft)

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

    def __repr__(self):
        return f"<#TextItem {self.text}: topleft={self.rect.topleft}, visible = {self.visible}, text = {self.text}#>"

    def __str__(self):
        return repr(self)