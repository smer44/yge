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
grid_spacing = 30  # Spacing between grid points
circle_radius = 20  # Initial radius of each circle



num_circles = len(range(0, image_width, grid_spacing)) * len(range(0, image_height, grid_spacing))

# Initialize the circles array to store the x-coordinate ranges
circles = np.zeros((num_circles, 2 * circle_radius, 2), dtype=int)

# Generate grid points and fill the circles array
circle_idx = 0
for x, y in [(x, y) for x in range(0, image_width, grid_spacing) for y in range(0, image_height, grid_spacing)]:
    for i in range(2 * circle_radius):
        y_offset = i - circle_radius
        x_span = int(np.sqrt(circle_radius**2 - y_offset**2)) if abs(y_offset) <= circle_radius else 0
        circles[circle_idx, i, 0] = max(x - x_span, 0)  # x_start
        circles[circle_idx, i, 1] = min(x + x_span, image_width - 1)  # x_end
    circle_idx += 1

# Prepare initial positions and movement directions for each circle
circle_positions = np.array([(x, y) for x in range(0, image_width, grid_spacing)
                                       for y in range(0, image_height, grid_spacing)])

original_positions = np.copy(circle_positions)

dx = np.random.randint(-20, 21, size=num_circles)  # Random horizontal movement
dy = np.random.randint(-15, -4, size=num_circles)  # Random vertical movement upwards

# Animation loop
running = True
clock = pygame.time.Clock()

current_num_circles = 0
while running:
    screen.fill((0, 0, 0))  # Clear screen
    result_surface = np.zeros((image_width, image_height, 3), dtype=np.uint8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle positions
    active_num_circles = min(current_num_circles, num_circles)
    circle_positions[:active_num_circles, 0] += dx[:active_num_circles]
    circle_positions[:active_num_circles, 1] += dy[:active_num_circles]

    current_num_circles+=1

    # Copy the circles from the original image to the result surface

    for i in range(num_circles):

        cx, cy = circle_positions[i]
        cx0,cy0 = original_positions[i]
        for j in range(2 * circle_radius):

            y_pos_original = cy0 + j - circle_radius
            #if i < active_num_circles:
             #   y_pos = cy + j - circle_radius
           # else:
            #    y_pos = y_pos_original
            y_pos = cy + j - circle_radius



            if 0 <= y_pos < image_height:

                x_start = max(circles[i, j, 0] +cx-circle_radius, 0)
                x_end = min(circles[i, j, 1] +cx-circle_radius, image_width - 1)
                x_start_original = max(circles[i, j, 0], 0)
                x_end_original =x_start_original +x_end-x_start

                if x_start < x_end and y_pos_original < 976:
                    result_surface[x_start:x_end, y_pos] = image_np[x_start_original:x_end_original, y_pos_original]

    # Convert the NumPy array to a Pygame surface
    result_surface_pygame = pygame.surfarray.make_surface(result_surface)

    # Draw the resulting surface
    screen.blit(result_surface_pygame, (0, 0))
    pygame.display.flip()  # Update display
    clock.tick(60)  # Limit to 60 FPS

# Quit PyGame
pygame.quit()
