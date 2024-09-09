import pygame
from yge.turnbased.yfillItem import yFillItem
from yge.turnbased.yvariantitem import yVariantItem
from yge.turnbased.ytext import yText
from yge.turnbased.yscene import yScene
from yge.turnbased.ygame import yGame
from yge.turnbased.ybgscene import yBgScene

print(pygame.K_w)
pygame.init()
font = pygame.font.Font(None, 74)

#pygame.font.init()

def display(ga):
    print("Key Pressed!")
    #new_text = font.render('Key  Pressed!', True, (0, 0, 255))
    #ga.display.blit(new_text, (200, 150))
    ga.item.items[0].toggle_children()

    ga.item.set_dirty_deep()
    print(f"display :{ga.item.items[0]} :: {ga.item.items[0].items}")




bg = yFillItem(255, 255, 255)

bg2 = yFillItem(100, 100, 100)

switch_bg = yVariantItem("bg",bg, bg2)



new_text = font.render('New game', True, (0, 0, 255))
new_text2 = font.render('Tutorial', True, (0, 255,0))

ta = yText('New game','New game', font, (0, 0, 255),(200, 150),True)
ta2 = yText('Tutorial','Tutorial', font,(0, 255,0), (200, 250),True)

menu = yScene("menu",ta, ta2)

main_scene = yBgScene("bg scene", switch_bg, menu)

ga  = yGame(800,600,main_scene)



ga.add_key_action(pygame.K_w, display, ga)
ga.run()


