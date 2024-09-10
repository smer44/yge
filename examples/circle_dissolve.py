import pygame
import numpy as np
import random

# Initialize PyGame
pygame.init()

# Load the image
image_path = 'adventurer_girl.png'  # Replace with your image file path
image = pygame.image.load(image_path)
image_width, image_height = image.get_size()

# Setup display
screen = pygame.display.set_mode((image_width, image_height))
pygame.display.set_caption('Dissolve Effect')

# Define grid and circle parameters
grid_spacing = 20  # Spacing between grid points
circle_radius = 30  # Initial radius of each circle
circle_shrink_rate = 1  # How much the circle shrinks each frame
circle_fade_rate = 3  # How much the circle fades each frame

# Generate grid points
grid_points = [(x, y) for x in range(0, image_width, grid_spacing)
                      for y in range(0, image_height, grid_spacing)]

# Prepare circles with subsurfaces
circles = []
for x, y in grid_points:
    # Create a circular surface
    surface = pygame.Surface((2*circle_radius, 2*circle_radius), pygame.SRCALPHA)
    surface.blit(image, (0, 0), (x - circle_radius, y - circle_radius, 2*circle_radius, 2*circle_radius))
    alpha_surface = surface.copy()
    pygame.draw.circle(alpha_surface, (255, 255, 255, 0), (circle_radius, circle_radius), circle_radius)
    surface.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    circles.append({'surface': surface, 'x': x, 'y': y, 'radius': circle_radius, 'alpha': 255})

# Animation loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circles
    for circle in circles:
        if circle['radius'] > 0 and circle['alpha'] > 0:
            # Move the circle upwards randomly
            circle['x'] += random.randint(-5, 5)
            circle['y'] -= random.randint(1, 5)
            # Shrink the circle
            circle['radius'] -= circle_shrink_rate
            # Fade out the circle
            circle['alpha'] -= circle_fade_rate

            # Update the surface with the new radius and alpha
            surface = pygame.Surface((2*circle['radius'], 2*circle['radius']), pygame.SRCALPHA)
            surface.blit(image, (0, 0), (circle['x'] - circle['radius'], circle['y'] - circle['radius'], 2*circle['radius'], 2*circle['radius']))
            alpha_surface = surface.copy()
            pygame.draw.circle(alpha_surface, (255, 255, 255, 0), (circle['radius'], circle['radius']), circle['radius'])
            surface.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            surface.set_alpha(circle['alpha'])
            circle['surface'] = surface

    # Draw all circles
    for circle in circles:
        if circle['radius'] > 0 and circle['alpha'] > 0:
            screen.blit(circle['surface'], (circle['x'] - circle['radius'], circle['y'] - circle['radius']))

    pygame.display.flip()  # Update display
    clock.tick(10)  # Limit to 60 FPS

# Quit PyGame
pygame.quit()
