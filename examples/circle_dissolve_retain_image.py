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
grid_spacing = 30  # Spacing between grid points
circle_radius = 30  # Initial radius of each circle
circle_shrink_rate = 1  # How much the circle shrinks each frame
circle_fade_rate = 5  # How much the circle fades each frame

# Generate grid points
grid_points = [(x, y) for x in range(0, image_width, grid_spacing)
               for y in range(0, image_height, grid_spacing)]

# Prepare circles with subsurfaces
circles = []
for x, y in grid_points:
    # Create a circular surface with transparency
    surface = pygame.Surface((2 * circle_radius, 2 * circle_radius), pygame.SRCALPHA)

    # Extract the circular area from the image
    for i in range(2 * circle_radius):
        for j in range(2 * circle_radius):
            distance = np.sqrt((i - circle_radius) ** 2 + (j - circle_radius) ** 2)
            if distance < circle_radius:
                img_x = x - circle_radius + i
                img_y = y - circle_radius + j

                # Ensure we don't go out of bounds
                if 0 <= img_x < image_width and 0 <= img_y < image_height:
                    surface.set_at((i, j), image.get_at((img_x, img_y)))

    circles.append({
        'surface': surface,
        'x': x,
        'y': y,
        'radius': circle_radius,
        'alpha': 255,
        'dx': random.randint(-10, 10),  # Random horizontal movement
        'dy': random.randint(-15, -5),  # Random vertical movement upwards
    })

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
            # Move the circle in a randomized direction
            circle['x'] += circle['dx']
            circle['y'] += circle['dy']

            # Shrink the circle
            circle['radius'] -= circle_shrink_rate

            # Fade out the circle
            circle['alpha'] -= circle_fade_rate

            # Update the surface with the new radius and alpha
            if circle['radius'] > 0:
                surface = pygame.Surface((2 * circle['radius'], 2 * circle['radius']), pygame.SRCALPHA)
                for i in range(2 * circle['radius']):
                    for j in range(2 * circle['radius']):
                        distance = np.sqrt((i - circle['radius']) ** 2 + (j - circle['radius']) ** 2)
                        if distance < circle['radius']:
                            img_x = circle['x'] - circle['radius'] + i
                            img_y = circle['y'] - circle['radius'] + j

                            # Ensure we don't go out of bounds
                            if 0 <= img_x < image_width and 0 <= img_y < image_height:
                                color = image.get_at((img_x, img_y))
                                surface.set_at((i, j), color)
                surface.set_alpha(circle['alpha'])
                circle['surface'] = surface

    # Draw all circles
    for circle in circles:
        if circle['radius'] > 0 and circle['alpha'] > 0:
            screen.blit(circle['surface'], (circle['x'] - circle['radius'], circle['y'] - circle['radius']))

    pygame.display.flip()  # Update display
    clock.tick(60)  # Limit to 60 FPS

# Quit PyGame
pygame.quit()
