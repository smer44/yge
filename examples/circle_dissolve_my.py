import pygame
import numpy as np
import random

# Initialize PyGame
pygame.init()

# Load the image
image_path = 'adventurer_girl.png'   # Replace with your image file path
image = pygame.image.load(image_path)
image_width, image_height = image.get_size()

# Convert the image to a NumPy array for processing
image_np = pygame.surfarray.array3d(image)

# Setup display
screen = pygame.display.set_mode((image_width, image_height))
pygame.display.set_caption('Dissolve Effect')

# Define grid and circle parameters
xgrid_spacing = 30  # Spacing between grid points
ygrid_spacing = 30  # Spacing between grid points
circle_radius = 24  # Initial radius of each circle

radius_shrink = 0.1 # radius fade each tick

xa_start = 0.2
xa_end = 0.8
x0 = int( xa_start*image_width)
x1 = int(xa_end*image_width)

ya_start = 0.05
ya_end = 0.95#1.0
y0 = int( ya_start*image_height)
y1 = int(ya_end*image_height)


x_grid_max = (x1-x0)//xgrid_spacing
y_grid_max = (y1-y0)//ygrid_spacing





circle_shape = np.zeros((circle_radius), dtype=int)

circle_radius_sq = circle_radius * circle_radius
# Generate grid points and fill the circles array:
for x in range(circle_radius):
    y = int(np.sqrt(circle_radius_sq-x*x))
    circle_shape[x] = y


circle_positions = np.array([(x, y) for x in range(x0, x1, xgrid_spacing)
                                       for y in range(y0, y1, ygrid_spacing)])




num_circles =  len(circle_positions)

circle_radiuses = np.full(num_circles,circle_radius)

print("num_circles = " , num_circles)
print(f"{circle_positions.shape=}")
print(f"{circle_shape.shape=}")
original_positions = np.copy(circle_positions)

dx = np.random.randint(-20, 21, size=num_circles)  # Random horizontal movement
dy = np.random.randint(-15, -4, size=num_circles)  # Random vertical movement upwards

print(f"{dx.shape=}")
print(f"{dy.shape=}")

# Animation loop
running = True
clock = pygame.time.Clock()

passive_circles = num_circles

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))  # Clear screen
    result_surface = np.zeros((image_width, image_height, 3), dtype=np.uint8)

    #move not passive circles:
    circle_positions[passive_circles:,0]+=dx[passive_circles:]
    circle_positions[passive_circles:, 1] += dy[passive_circles:]
    circle_radiuses[passive_circles:,]-=1
    #passive_circles
    #circle_positions[:, 0] += dx[:]
    #circle_positions[:, 1] += dy[:]
    passive_circles = max(passive_circles-1,0)

    #place circles in the output ndarray accorting to shifted positions:
    for cid in range(num_circles):
        # for (rx0,ry0),(rx,ry) in zip(original_positions, circle_positions):
        rx0, ry0 = original_positions[cid]
        rx, ry = circle_positions[cid]
        if not (0 <=ry <image_height and 0<=ry0 <image_height):
            continue
        current_radius = circle_radiuses[cid]

        y_start = max(ry - current_radius,0)
        y_end = min(ry + current_radius, image_height - 1)
        y_start_original= max(ry0 - current_radius,0)
        y_end_original = min(ry0 + current_radius, image_height - 1)

        circle_shape_0 = current_radius - max(current_radius - ry,current_radius- ry0,0)
        circle_shape_1 = current_radius - max(current_radius + ry-image_height,current_radius + ry0-image_height,0 )

        #circle_shape_0 = np.flip(circle_shape[:circle_shape_0])
        #circle_shape_1 = circle_shape[:circle_shape_1]


        #x_start = np.maximum(rx - circle_shape,0)
        #x_end  = np.minimum(rx + circle_shape,image_width - 1)

        #x_start_original = np.maximum(rx0 - circle_shape,0)
        #x_end_original = x_start_original + x_end - x_start

        #print("circle_shape_0 =" , circle_shape_0)
        for y_shape_pos in range(0,circle_shape_0):
            end_y = ry - y_shape_pos
            y_original = ry0 - y_shape_pos

            shape_offset = circle_shape[y_shape_pos] - circle_radius+current_radius
            if shape_offset < 0 :
                continue
            x_start = max(rx - shape_offset,0)
            x_end = min(rx + shape_offset,image_width-1)
            x_start_original = max(rx0 - shape_offset,0)
            x_end_original = min(rx0 + shape_offset,image_width-1)
            x_size = min(x_end-x_start,x_end_original-x_start_original)

            if x_size > 0:
                x_end = x_start+x_size
                x_end_original = x_start_original + x_size
                #print(f" arrays: {x_start=}, {x_end=}, {result_surface.shape=},{image_width=} {x_start_original=}, {x_end_original=},{image_np.shape=} ,{x_size=}")



                result_surface[x_start:x_end, end_y] = image_np[x_start_original:x_end_original, y_original]
        #now display the second half:
        for y_shape_pos in range(0,circle_shape_1):
            end_y = ry + y_shape_pos
            y_original = ry0 + y_shape_pos
            shape_offset = circle_shape[y_shape_pos]- circle_radius+current_radius
            if shape_offset < 0 :
                continue
            x_start = max(rx - shape_offset,0)
            x_end = min(rx + shape_offset,image_width-1)
            x_start_original = max(rx0 - shape_offset,0)
            x_end_original = min(rx0 + shape_offset,image_width-1)
            x_size = min(x_end-x_start,x_end_original-x_start_original)

            if x_size > 0:
                x_end = x_start+x_size
                x_end_original = x_start_original + x_size
                #print(f" arrays: {x_start=}, {x_end=}, {result_surface.shape=},{image_width=} {x_start_original=}, {x_end_original=},{image_np.shape=} ,{x_size=}")



                result_surface[x_start:x_end, end_y] = image_np[x_start_original:x_end_original, y_original]



    # Convert the NumPy array to a Pygame surface
    result_surface_pygame = pygame.surfarray.make_surface(result_surface)

    # Draw the resulting surface
    screen.blit(result_surface_pygame, (0, 0))
    pygame.display.flip()  # Update display
    clock.tick(60)  # Limit to 60 FPS

# Quit PyGame
pygame.quit()


























