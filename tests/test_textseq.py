from yge.turnbased.ysolid import ySolid
from yge.turnbased.ytextsequence import yTextSequence
from yge.turnbased.ygame import yGame
from yge.turnbased.ycontainer import yFrame
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
#TODO - distinguish component, what size is controlled from above (from parent)
#and what size is controlled from bottom to up ( it controlls parent size)
yte = yTextSequence("hello text", texts,font,(255,255,0))
yte.loop = True
bg = ySolid(0, 0, 0)

scene = yFrame("bgscene", bg, yte)

yg = yGame(scene,w,h)

yg.add_deep(scene)
print(f"{yg.mouse_listeners=}")
print(f"{yg.visible=}")
yg.run()