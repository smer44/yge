from pygame import Rect

from yge.turnbased.yabstract import yOneToOnePlacer


class yNotGreaterThenImagePlacer(yOneToOnePlacer):


    def __init__(self, name, yimage):
        yOneToOnePlacer.__init__(self, name)
        self.yimage = yimage

    def __place_inner__(self,rect):
        x,y,w,h = rect
        yimage = self.yimage
        print(f"{yimage=}")


        #call if it is lazy image generator what does not have self.image initially:
        if yimage.lazy_image:
            if yimage.image is None:
                yimage.create_image()
        yimage_rect = yimage.image.get_rect()
        img_x,img_y,img_w,img_h = yimage_rect
        print(f"__place_inner__:{rect=} , {yimage_rect=}")
        w = min(w, img_w)
        h = min(h, img_h)
        return Rect(x, y, w, h)


