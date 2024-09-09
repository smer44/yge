from turnbased.yrect import yRect
from turnbased.yimage import yImage

class yGame:

    def __init__(self,w,h,**scenes):
        #self.scenes = scenes
        self.scenes_list = list(scenes.values())
        self.display = pygame.display.set_mode((w, h))

    def add(self,item,*items):
        self.scenes_list.append(item)
        self.scenes_list.extend(items)



    def set_size(self,w,h):
        self.display = pygame.display.set_mode((w, h))

    def draw_scenes(self):
        self.display.fill((255, 255, 255))  # Fill the screen with white
        for scene in self.scenes_list:
            scene.redraw(self.display)

    def set_update_scenes(self,update_fn):
        self.update_scenes = update_fn

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_scenes()
            self.draw_scenes()
            pygame.display.flip()









class Scene:

    def __init__(self,root,**items):
        self.root = root
        self.items = {id(item): item for item in items}



class Placer:

    def __init__(self):
        self.scale_fn = None
        self.move_fn = None

    def __call__(self,root, *items):
        if self.scale_fn:
            self.scale_fn(root, *items)
        if self.move_fn:
            self.move_fn(root, *items)

    def xyalign(self,xvalue,yvalue):
        self.args = xvalue,yvalue
        self.move_fn = self.exec_xyalign

    def ysplit(self,ystart=0.0,yend=1.0):
        self.args = ystart, yend
        self.move_fn = self.exec_ysplit

    def exec_ysplit(self, root, *items):
        ystart, yend = self.args
        n = len(items)
        step = (yend-ystart)/(n+1)
        yvalue = ystart
        for item in items:
            yvalue += step
            dy = (root.height - item.height) * yvalue
            item.top = root.top + dy
            #print(f"placed {item} at", item.rect.left)






    def exec_xyalign(self, root, item):
        xvalue,yvalue = self.args
        # assert item in self.items
        dx = (root.width - item.width) * xvalue
        dy = (root.height - item.height) * yvalue
        item.left = root.left + dx
        item.top = root.top + dy


    def xalign(self, value):
        self.args = value
        self.move_fn = self.exec_xalign

    def exec_xalign(self, root, item):

        value = self.args
        dx = (root.width -item.width) *value
        item.xpos(root.left+ dx)
        print(f"exec_xalign: {item}, {value=}")

    def yalign(self, value):
        self.args = value
        self.move_fn = self.exec_yalign

    def exec_yalign(self, root, item):
        value = self.args
        dy = (root.height  -item.height ) *value
        item.top = root.top + dy






class AbstractDynamicValue:

    def next(self):
        assert False, f"{self.type} : next must be implemented"




class BackForthValue(AbstractDynamicValue):

    def __init__(self, value, vmin, vmax,step,):
        self.v = value
        self.step = step
        self.vmin = vmin
        self.vmax = vmax

    def next(self):
        #print("next called")
        self.v += self.step
        if not self.vmin < self.v <self.vmax:
            self.step = -self.step
        return self.v





import pygame
import sys

def main():
    pygame.init()  # Initialize Pygame

    # Set up the display
    width, height = 800, 600
    game = yGame(width, height)

    #screen = pygame.display.set_mode((width, height))

    image_path = r"E:\2022workspaces\PycharmProjects\renpyProjects\rewind_test\game\images\tutorial_girl_tied_up.png"
    #image = pygame.image.load(image_path)
    #resized_image = pygame.transform.scale(image, (100, 50))



    child_rect3 = pygame.Rect(0, 0, 100, 50)  # Child rectangle

    parent_rect = yRect("rparent_rect",100, 100, 400, 300,  (0, 0, 255),  2)
    #rchild_rect = RectangleItem((255, 0, 0), child_rect, 0)
    child_rect = yImage(image_path,0, 0, 100, 50)

    child_rect2 = yRect("re_2",0, 0, 100, 50,(0,255,  0),  0)
    child_rect3 = yRect("re 3",0, 0, 100, 50,(255, 255, 0), 12)

    game.add(parent_rect, child_rect, child_rect2, child_rect3)

    xa = BackForthValue(400,200,600,400*0.001/2)
    ya = BackForthValue(0.5, 0, 1, 0.001)
    ya2 = BackForthValue(0.0, 0, 1, 0.001)

    running = True

    #place = Placer()
    #place.xyalign(1.0,0.1)

    x_place = Placer()
    #y_change_place.yalign( ya.v)

    y_multi = Placer()
    y_multi.ysplit(0.1,0.9)





    def game_update():
        #print("game_update")
        parent_rect.set_dirty()
        parent_rect.width = xa.next()
        #parent_rect.height = xa.next()
        # place(parent_rect, child_rect)

        # aligner is changed dynamically :
        x_place.xalign(ya.next())
        x_place(parent_rect, child_rect)

        x_place.xalign(1 - ya.v)
        x_place(parent_rect, child_rect2)

        # ya2

        x_place.xalign(ya2.next())
        x_place(parent_rect, child_rect3)

        y_multi(parent_rect, child_rect, child_rect2, child_rect3)

    game.update_scenes = game_update
    game.run()

main()