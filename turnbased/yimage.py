from yge.turnbased.yitem import yItem
import pygame

class yImage(yItem):

    def __init__(self,path,top,left,width,height,visible = True):
        super().__init__(path, visible)
        self.reload(path)
        self.rescale(width,height)
        self.pos(top,left)


    def rescale(self, width, height):
        #print(f'yImage.rescale, topleft = {self.rect.topleft}')
        self.image = pygame.transform.scale(self.loaded_image, (width, height))
        self.width = width
        self.height = height
        self.set_dirty()


    def pos(self,top,left):
        self.top = top
        self.left = left
        self.set_dirty()

    def xpos(self,x):
        #print(f'xpos called {x}')
        self.left  = x
        self.set_dirty()

    def ypos(self,y):
        self.top  = y
        self.set_dirty()

    def reload(self, path):
        self.name  = path
        self.loaded_image = pygame.image.load(path)
        self.rect = self.loaded_image.get_rect()
        self.set_dirty()



    def __display__(self, display):
        #print(f'yImage.__display__ ')
        display.blit(self.image, (self.left,self.top))

