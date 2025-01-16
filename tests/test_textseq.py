from yge.turnbased.yabstract import ySamePlacer
from yge.turnbased.ynormoffset import yNormOffsetPlacer
from yge.turnbased.ynotcreaterthenimage import yNotGreaterThenImagePlacer
from yge.turnbased.ysametomany import ySameToManyPlacer
from yge.turnbased.ysolid import ySolid
from yge.turnbased.ytextsequence import yTextSequence
from yge.turnbased.ygame import yGame
from yge.turnbased.yframe import yFrame
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

place_mid = yNormOffsetPlacer("place_mid",0.5,0.5)
place_quoter = yNormOffsetPlacer("place_quoter",0.25,0.25)
place_same_to_many = ySameToManyPlacer("test_same_to_many_placer")




yte = yTextSequence("hello text", texts,font,(255,255,0))

place_not_greater = yNotGreaterThenImagePlacer("test_not_greater_placer", yte)

place_same_to_many

yte.loop = True
yte.placer = place_mid
place_mid.set_next_placer(place_not_greater)
bg = ySolid("TestBackground",0, 2, 200)
bg.placer = place_quoter

scene = yFrame("bgscene", bg, yte)
scene.placer =place_same_to_many

yg = yGame(scene,w,h)
#yg.placer = ySamePlacer()
yg.place()

yg.add_deep(scene)

print(f"{yg.mouse_listeners=}")
print(f"{yg.visible=}")
yg.run()