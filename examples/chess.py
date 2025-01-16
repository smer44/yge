import pygame
import numpy as np

# Initialize PyGame
pygame.init()

# Define the screen size
screen_width = 640+80
screen_height = 480+80
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Optimized Chessboard Pattern")

# Define the size of each square
cell_size = 80

# Colors for the chessboard pattern (Black and White) as NumPy arrays
white = np.array([255, 255, 255], dtype=np.uint8)
black = np.array([0, 0, 0], dtype=np.uint8)

# Function to create a chessboard pattern using NumPy
def create_chessboard_array():
    # Create an empty array with shape (height, width, 3) for RGB values
    #chessboard = np.zeros((screen_width,screen_height,3), dtype=np.uint8)
    #cell_board = np.zeros((screen_width//cell_size,screen_height//cell_size), dtype=np.uint8)
    #np.fill()
    black_cell = np.tile(black, (cell_size, cell_size,1))
    white_cell = np.tile(white, (cell_size, cell_size,1))
    cell_pair = np.stack((black_cell,white_cell), axis=0).reshape((cell_size*2, cell_size, 3))
    cell_pair2 = np.stack((white_cell, black_cell), axis=0).reshape((cell_size * 2, cell_size, 3))

    cell_quad = np.stack((cell_pair, cell_pair2), axis=1).reshape((cell_size * 2, cell_size * 2, 3))

    cell_width = screen_width//cell_size
    cell_height = screen_height//cell_size
    board = np.tile(cell_quad,(cell_width,cell_height,1))
    board = board[:screen_width,:screen_height]


    return board

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
