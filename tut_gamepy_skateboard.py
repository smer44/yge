import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Symbolic Image: Human on a Skateboard")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
lgray = (180, 180, 180)
blue = (0, 0, 255)

# Human and Skateboard parameters
head_radius = 20
body_width = 10
body_height = 55
arm_length = 40
leg_length = 60
skateboard_width = 120
skateboard_height = 10
wheel_radius = 10

# Position
center_x = width // 2
center_y = height*0.9
zpos = 0
z_limit = 300
x_limit0 = width*0.2
x_limit1= width*0.9
xpos = 0

# Function to draw the human

def zshift(x,y,z):
    return x -z*0.3, y -z*0.5

def draw_human(surface, x, y):
    x,y = zshift(x,y,zpos)
    y -= leg_length + skateboard_height+ wheel_radius+ wheel_radius+ wheel_radius
    # Head
    pygame.draw.circle(surface, black, (x, y - body_height - head_radius), head_radius)

    # Body
    pygame.draw.rect(surface, black, (x - body_width // 2, y - body_height, body_width, body_height))

    # Arms
    pygame.draw.line(surface, black, (x, y - body_height + 5), (x - arm_length, y - body_height + 30), 5)
    pygame.draw.line(surface, black, (x, y - body_height + 5), (x + arm_length, y - body_height + 30), 5)

    leg_correction = 10
    # Legs
    pygame.draw.line(surface, black, (x, y), (x - leg_length/2, y + leg_length + leg_correction ), 5)
    pygame.draw.line(surface, black, (x, y), (x + leg_length/2, y + leg_length + leg_correction), 5)

    draw_skateboard(surface,x,y+ leg_length + skateboard_height)


# Function to draw the skateboard
def draw_skateboard(surface, x, y):
    # Skateboard deck
    pygame.draw.rect(surface, gray, (x - skateboard_width // 2, y, skateboard_width, skateboard_height))

    # Wheels
    pygame.draw.circle(surface, blue, (x - skateboard_width // 3, y + skateboard_height + wheel_radius), wheel_radius)
    pygame.draw.circle(surface, blue, (x + skateboard_width // 3, y + skateboard_height + wheel_radius), wheel_radius)


# Main loop

# display floor statically:
def display_floor():
       floor_x0, floor_y = 100, center_y
       floor_x1, floor_y1 = zshift(floor_x0, floor_y, z_limit)
       pygame.draw.polygon(window, lgray, (
           (floor_x0, floor_y), (floor_x1, floor_y1), (floor_x1 + 600, floor_y1), (floor_x0 + 600, floor_y)))


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    window.fill(white)  # Fill the background with white

    # Draw the human on the skateboard
    #draw_skateboard(window, center_x, center_y + leg_length + skateboard_height)

    display_floor()
    draw_human(window, center_x, center_y)






# Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    speed = 10
    if keys[pygame.K_w]:  # Move back (up-left in projection)
        zpos=min (zpos +speed, z_limit)
    if keys[pygame.K_s]:  # Move back (up-left in projection)
        zpos=max (zpos -speed, 0)
    if keys[pygame.K_a]:  # Move left
        center_x = max(center_x - speed,x_limit0)
    if keys[pygame.K_d]:  # Move right
        center_x = min(center_x + speed, x_limit1)


    # Update the display
    pygame.display.flip()
    #

# Quit pygame
pygame.quit()
sys.exit()
