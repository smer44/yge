import pygame
import sys

# Initialize PyGame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minimalist 2D Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Character properties
character_size = 50
character_x = 250
character_y = 300
#character_velocity_baze_x = 5
#character_velocity_y = 0
#character_gravity = 1
in_air = True

# Block properties
block_size = 100


class MovingBlock (pygame.Rect):

    def __init__(self,left,top,width,height,vx,vy):
        super().__init__(left,top,width,height)
        self.start_x = left
        self.start_y = top
        self.start_vx = vx
        self.start_vy = vy
        self.vx = vx
        self.vy = vy
        self.maxy = None
        self.maxx = None
        self.tick = self.tick_default

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vx = self.start_vx
        self.vy = self.start_vy



    def set_back_and_forth_y(self,miny,maxy,vy):
        self.miny = miny
        self.maxy = maxy
        self.vy = vy
        self.tick  = self.tick_back_and_forth


    def set_back_and_forth_x(self,minx,maxx,vx):
        self.minx = minx
        self.maxx = maxx
        self.vx = vx
        self.tick  = self.tick_back_and_forth

    def tick_default(self):
        self.x +=self.vx
        self.y +=self.vy

    def tick_back_and_forth(self):
        self.x += self.vx
        self.y += self.vy

        if self.maxy:
            if self.y > self.maxy or self.y < self.miny:
                self.vy = - self.vy
        if self.maxx:
            if self.x > self.maxx or self.x < self.minx:
                self.vx = - self.vx

    def set_controlled(self, walk_vx,jump_vy,gravity_vy):
        self.walk_vx = walk_vx
        self.jump_vy = jump_vy
        self.in_air = True
        self.gravity_vy = gravity_vy
        self.tick = self.tick_controlled

    def tick_controlled(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vx =- self.walk_vx
            self.x += self.vx
        if keys[pygame.K_d]:
            self.vx =  self.walk_vx
            self.x += self.vx
        if keys[pygame.K_w] and not self.in_air:
            #print("W pressed")
            self.in_air = True
            self.vy = -self.jump_vy
        self.vy += self.gravity_vy
        self.y += self.vy
        #self.tick_default()

    def intersect(self, rect):
        left1, top1, right1, bottom1 = self.left,self.top, self.right,self.bottom
        left2, top2, right2, bottom2 = rect.left,rect.left, rect.right,rect.bottom

        # Initialize intersection flag
        flag = 0

        # Check if there is no intersection at all
        if right1 < left2 or right2 < left1 or bottom1 < top2 or bottom2 < top1:
            return 0

        # Check if the second rectangle is fully inside the first rectangle
        if left1 <= left2 and right1 >= right2 and top1 <= top2 and bottom1 >= bottom2:
            flag |= 16

        # Check right edge intersection
        if right2 >= right1 and left2 <= right1:
            flag |= 1

        # Check top edge intersection
        if top2 <= top1 and bottom2 > top1:
            flag |= 2

        # Check left edge intersection
        if left2 <= left1 and right2 > left1:
            flag |= 4

        # Check bottom edge intersection
        if bottom2 >= bottom1 and top2 < bottom1:
            flag |= 8

        if flag :
            #print("is_intersect:", flag)
            #print(left1, top1, right1, bottom1)
            #print(left2, top2, right2, bottom2)
            pass

        return flag

    def correct_intersect(self,rect):
        is_intersect = rect.intersect(self)
        if is_intersect == 0:
            return
        assert is_intersect != 16 , "block must not be fully inside another block"


        if is_intersect & 2 :
            #print("on top")
            if self.vy > rect.vy:
                self.y = rect.left - self.height
                self.vy = min(self.vy,rect.vy)  # block.vy# block velocity y.
                self.x += rect.vx
                char.in_air = False
                return

        if is_intersect & 8:
            #print("on bottom")
            if self.vy < rect.vy:
                self.y = rect.bottom
                self.vy = max(self.vy, block.vy)
                return

        if is_intersect & 1:
            #print("on right")
            if self.vx < rect.vx:
                self.x = rect.right
                self.vx = max(self.vx, block.vx)
                return

        if is_intersect & 4:
            #print("on left")
            if self.vx > rect.vx:
                self.x =  rect.left - self.width
                self.vx = min(self.vx, block.vx)
                return






blocks = [
    MovingBlock(200, 500, block_size, block_size,0,0),
    MovingBlock(350, 400, block_size, block_size,0,0),
    MovingBlock(500, 300, block_size, block_size,0,0),
]

blocks[1].set_back_and_forth_y(70,600,-3)
blocks[2].set_back_and_forth_x(70,600,-3)


# Game loop
clock = pygame.time.Clock()

#block2_velocity_y = -3

char = MovingBlock(character_x, character_y, character_size, character_size,0,0)

char.set_controlled(5,15,1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Collision detection
    #character_rect = pygame.Rect(character_x, character_y, character_size, character_size)
    #print("char :", character_rect.left, character_rect.right, "block:", blocks[0].left,blocks[0].right)

    char.tick()

    #Move blocks:
#    block2= blocks[1]
#    block2.y += block2_velocity_y

#    if block2.y > 600 or block2.y < 50:
 #       block2_velocity_y = - block2_velocity_y


    for block in blocks:
        block.tick()
        char.correct_intersect(block)



    # Check if character is off the screen
    if char.bottom > SCREEN_HEIGHT:
        char.reset()


    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, char)
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block)

    pygame.display.flip()
    clock.tick(60)
