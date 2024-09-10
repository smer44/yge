import pygame
import numpy as np
from yge.turnbased.ynpgradientrender import fill_gradient_array

# Initialize PyGame
pygame.init()

# Define the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA )
pygame.display.set_caption("Optimized Chessboard Pattern")

# Define the size of each square
cell_size = 20

# Colors for the chessboard pattern (Black and White) as NumPy arrays
white = np.array([255, 255, 255], dtype=np.uint8)
black = np.array([0, 0, 0], dtype=np.uint8)

# Function to create a chessboard pattern using NumPy

import numpy as np

import numpy as np

def create_chessboard_array():
    # Create an empty array with shape (height, width, 3) for RGB values
    chessboard = np.zeros((screen_width,screen_height,3), dtype=np.uint8)

    # Fill the array with the chessboard pattern
    for y in range(0, screen_height, cell_size):
        for x in range(0, screen_width, cell_size):
            # Determine the color for the current square
            color = white if ((x // cell_size) + (y // cell_size)) % 2 == 0 else black
            # Set the color for the square
            chessboard[x:x + cell_size, y:y + cell_size,:] = color

    return chessboard

# Main game loop
running = True
chessboard_array = create_chessboard_array()


def interpolate_color(color1, color2, t):
    """Interpolate between two RGBA colors based on t (between 0 and 1)."""
    return (1 - t) * np.array(color1) + t * np.array(color2)


def fill_gradient_array_float(array, axis, *args):
    """
    Fill the NumPy array with a gradient along the specified axis.

    :param array: NumPy array to fill, with shape (height, width, 4) for RGBA values.
    :param axis: 'horizontal' or 'vertical', the direction of the gradient.
    :param args: Gradient color and position pairs, e.g. (color1, position1, color2, position2, ...).
                 Each color is an (R, G, B, A) tuple, and each position is a float from 0 to 1.
    """
    height, width, _ = array.shape

    # Parse the input gradients into separate color and position lists
    colors = [args[i] for i in range(0, len(args), 2)]
    positions = [args[i + 1] for i in range(0, len(args), 2)]

    if axis == 'horizontal':
        axis_length = width
        # Loop through each pixel along the specified axis
        for i in range(axis_length):
            # Calculate the normalized position along the axis (from 0 to 1)
            norm_pos = i / (axis_length - 1)

            # Find the two gradient stops between which the current pixel falls
            for j in range(len(positions) - 1):
                if positions[j] <= norm_pos <= positions[j + 1]:
                    # Interpolate between the two colors based on the position
                    t = (norm_pos - positions[j]) / (positions[j + 1] - positions[j])
                    color = interpolate_color(colors[j], colors[j + 1], t)
                    array[:, i] = color
    elif axis == 'vertical':
        axis_length = width
        # Loop through each pixel along the specified axis
        for i in range(axis_length):
            # Calculate the normalized position along the axis (from 0 to 1)
            norm_pos = i / (axis_length - 1)

            # Find the two gradient stops between which the current pixel falls
            for j in range(len(positions) - 1):
                if positions[j] <= norm_pos <= positions[j + 1]:
                    # Interpolate between the two colors based on the position
                    t = (norm_pos - positions[j]) / (positions[j + 1] - positions[j])
                    color = interpolate_color(colors[j], colors[j + 1], t)
                    array[i, :] = color
    else:
        raise ValueError("Axis must be 'horizontal' or 'vertical'")
# Example usage:
width, height = 640, 480
# Modify the array to have 4 channels for RGBA
array = np.zeros((height, width, 4), dtype=np.uint8)

# Fill the array with a horizontal gradient that includes different alpha values
# Gradient from red with full opacity at position 0.0, to green with 50% opacity at position 0.5,
# to blue with full transparency at position 1.0.
fill_gradient_array(array, 'vertical',
                    (255, 0, 0, 255), 0.0,  # Red, fully opaque
                    (0, 255, 0, 128), 0.5,  # Green, 50% transparent
                    (0, 0, 255, 0), 1.0)  # Blue, fully transparent

# Or for a vertical gradient with alpha channels
# fill_gradient_array(array, 'vertical',
#                     (255, 255, 0, 255), 0.0,  # Yellow, fully opaque
#                     (0, 255, 255, 0), 1.0)    # Cyan, fully transparent


# Example usage:
width, height = 640, 480
array = np.zeros(( width,height, 4), dtype=np.uint8)

# Fill the array with a horizontal gradient
# Gradient from red at position 0.0, to green at position 0.5, to blue at position 1.0
fill_gradient_array(array, "v", (255, 0, 0,200), 0.0, (0, 255, 255,255), 0.5, (0, 255, 0,0), 1.0)

# Or for a vertical gradient
# fill_gradient_array(array, 'vertical', (255, 255, 0), 0.0, (0, 255, 255), 1.0)


# Main game loop
running = True

def make_surface_rgba(array):
    """Returns a surface made from a [w, h, 4] numpy array with per-pixel alpha
    """
    shape = array.shape
    if len(shape) != 3 and shape[2] != 4:
        raise ValueError("Array not RGBA")

    # Create a surface the same width and height as array and with
    # per-pixel alpha.
    surface = pygame.Surface(shape[0:2], pygame.SRCALPHA, 32)

    # Copy the rgb part of array to the new surface.
    pygame.pixelcopy.array_to_surface(surface, array[:,:,0:3])

    # Copy the alpha part of array to the surface using a pixels-alpha
    # view of the surface.
    surface_alpha = np.array(surface.get_view('A'), copy=False)
    surface_alpha[:,:] = array[:,:,3]

    return surface


gradient_surface = make_surface_rgba(array)

while running:
    # Check for events like quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    #screen.blit(chessboard_array, (0, 0))
    pygame.surfarray.blit_array(screen, chessboard_array)
    # Create a surface from the array and blit it to the screen
    screen.blit(gradient_surface,(0,0))

    # Update the display
    pygame.display.flip()

# Quit PyGame
pygame.quit()
