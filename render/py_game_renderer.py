
import pygame

from yge.layout.box_plaser import BoxPlacer


class PyGameRenderer:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background_color = (0, 0, 0)
        self.items = []
        self.box_placer = BoxPlacer()

    def add(self,obj):
        self.items.append(obj)
    def draw_items(self):
        surface = self.screen
        for node in self.items:
            for obj in node.deep_children():
                if obj.stype == 1 : # if rect:
                    self.draw_rounded_rect(surface, obj)
                    for inner_rect in self.box_placer(obj):
                        pygame.draw.rect(surface, (0,255,255), inner_rect)







    def draw_rounded_rect(self, surface, obj):
        rect = ()
        pygame.draw.rect(surface, obj.background, obj.rect(), border_radius=obj.corner_radius)



    def run(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill(self.background_color)
            self.draw_items()
            pygame.display.flip()

    def quit(self):
        pygame.quit()


from yge.layout.geom import sRect

obj = sRect(100,100,200,300, (255,0,0,),8)
#xywh is not stored in the component - ?


re  = PyGameRenderer()
re.add(obj)

re.run()
re.quit()



