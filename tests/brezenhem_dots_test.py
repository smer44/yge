import matplotlib.pyplot as plt
import numpy as np
from yge.turnbased.brezenheim_single import  my_bresenham_dots_single
from yge.turnbased.sutil import myrange

scale = 1*7


# Example usage:
#x0, y0 = np.array((0,0,0)), np.array((90,40,190))
#x1, y1 = np.array((30,30,30)), np.array((100,110,120))
x0, y0 = 10*scale, 1*scale
x1, y1 = 3*scale, 14*scale
line_points = my_bresenham_dots_single(x0, y0, x1, y1)




# Plot the line using matplotlib
grid_size = (20*scale,max(x0,x1)+1)
grid = np.zeros(grid_size)

colors = [1,0.5, 0.3,0.7]

for k,x in enumerate(myrange(x0,x1)):
    y = line_points[k]
    grid[y, x] = 1  # Set the pixel at each point
print(f" {line_points[-1]=}")
print(f" {y1=}")

plt.imshow(grid, cmap='Greys', origin='lower')
plt.grid(True)
plt.show()
