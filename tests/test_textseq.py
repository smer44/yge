from yge.turnbased.ytextsequence import yTextSequence
from yge.turnbased.ygame import yGame
from yge.turnbased.ybgscene import yBgScene
from yge.turnbased.yfillItem import yFillItem
import pygame
from pygame.font import Font

texts = """
This shows work of yTextSequence class
click with mouse on text to trigger the text change
also the text message will loop

""".splitlines()

texts = [t.strip() for t in texts]
texts = [t for t in texts if t]
pygame.init()
font = Font(None, 74)

w,h = 1920,1080

yte = yTextSequence("hello text", texts,font,(255,255,0),(w//2,h//2))
yte.loop = True
bg = yFillItem(0,0,0)

bgscene = yBgScene("bgscene",bg, yte)

yg = yGame(w,h ,bgscene)
yg.run()