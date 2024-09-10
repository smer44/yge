
import numpy as np
import matplotlib.pyplot as plt

from yge.turnbased.brezenheim_vectors import  my_bresenham_line_vectors
from yge.turnbased.sutil import myrange

scale = 1*7


# Example usage:
#x0, y0 = np.array((0,0,0)), np.array((90,40,190))
#x1, y1 = np.array((30,30,30)), np.array((100,110,120))
x0, y0 = 10*scale, np.array((9,4,19,14))*scale
x1, y1 = 3*scale, np.array((10,11,12,13))*scale
line_points = my_bresenham_line_vectors(x0, y0, x1, y1)




# Plot the line using matplotlib
grid_size = (20*scale,max(x0,x1)+1)
grid = np.zeros(grid_size)

colors = [1,0.5, 0.3,0.7]

for k,x in enumerate(myrange(x0,x1)):
    vy = line_points[k]
    #print(f" {vy=}")
    for n, y in enumerate(vy):
        grid[y, x] = colors[n]  # Set the pixel at each point
print(f" {line_points[-1]=}")
print(f" {y1=}")

plt.imshow(grid, cmap='Greys', origin='lower')
plt.grid(True)
plt.show()
