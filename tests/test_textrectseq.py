from yge.turnbased.ytextrectseq import yTextRectSequence
from yge.turnbased.ygame import yGame
from yge.turnbased.ybgscene import yBgScene
from yge.turnbased.yfillItem import yFillItem
from yge.turnbased.yfillchess import yFillChess
import pygame
from pygame.font import Font


texts = """This shows work of yTextRectSequence class
click with mouse on the rectangle to trigger the text change,
the rectangle and text will be redrawn.
also the text message will loop

""".splitlines()
texts = [t.strip() for t in texts]
texts = [t for t in texts if t]

pygame.init()
font = Font(None, 74)

w,h = 1920,1080

yte = yTextRectSequence("yte test",
                        texts,
                        font,
                        (0,0,0),
                        0,
                        h-100,
                        w-20,
                        90,
                        (0,0,255),
                        0,
                        visible=True
                        )
yte.loop = True
#bg = yFillItem(255,255,255)

bg = yFillChess()
#bg = yFillItem(255,255,255)

bgscene = yBgScene("bgscene",bg, yte)

yg = yGame(w,h ,bgscene)
bg.__display__(yg.display)
print(yte)
yg.run()





