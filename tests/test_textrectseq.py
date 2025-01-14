from yge.turnbased.ytextrectseq import yTextRectSequence
from yge.turnbased.ygame import yGame
from yge.turnbased.ycontainer import yFrame
from yge.turnbased.ysolid import ySolid
from yge.turnbased.yfillchess import yFillChess
import pygame
from pygame.font import Font

from yge.turnbased.ytextsequence import yTextSequence

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

yte = yTextSequence("yte test",
                        texts,
                        font,
                        (0,0,0),
                        )
yte.loop = True
#bg = yFillItem(255,255,255)

bg = yFillChess("chess test")


bgscene = yFrame("bgscene", bg, yte)

yg = yGame(bgscene, w,h )
#bg.__display__(yg.display)
print(f"{yte=}")
yg.run()





