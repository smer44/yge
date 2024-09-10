import pygame
import numpy as np

# Initialize PyGame
pygame.init()

# Define the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Optimized Chessboard Pattern")

# Define the size of each square
cell_size = 20

# Colors for the chessboard pattern (Black and White) as NumPy arrays
white = np.array([255, 255, 255], dtype=np.uint8)
black = np.array([0, 0, 0], dtype=np.uint8)

# Function to create a chessboard pattern using NumPy
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

while running:
    # Check for events like quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a surface from the array and blit it to the screen
    pygame.surfarray.blit_array(screen, chessboard_array)

    # Update the display
    pygame.display.flip()

# Quit PyGame
pygame.quit()
