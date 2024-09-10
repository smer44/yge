import numpy as np
import matplotlib.pyplot as plt
from yge.turnbased.brezenheim_single import bresenham_line


# Example usage:
x0, y0 = 10, 9
x1, y1 = 3, 10

x0, y0 = 9, 3
x1, y1 = 11, 10

line_points = bresenham_line(x0, y0, x1, y1)

# Plot the line using matplotlib
grid_size = (15, 15)
grid = np.zeros(grid_size)

for x,y in line_points:
    grid[y, x] = 1  # Set the pixel at each point

plt.imshow(grid, cmap='Greys', origin='lower')
plt.grid(True)
plt.show()
