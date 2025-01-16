from yge.turnbased.ygame import yGame
from yge.turnbased.ypicture import yPicture

def test_mouse_react(obj, game,mouse_pos):
    text_rect = obj.rect()

    if text_rect.collidepoint(mouse_pos):
        print(f" !!!! test_mouse_react OF THE TEST !!! {mouse_pos=}, {text_rect=}")

p = yPicture("mc_descengind_staircase")

print(p)

w,h = 1920,1080

yg = yGame(p,w,h)
yg.add_deep(p)
p.load()
p.mouse_react = lambda game,mouse_pos : test_mouse_react(p,game,mouse_pos)
yg.run()




