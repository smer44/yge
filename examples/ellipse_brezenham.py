import matplotlib.pyplot as plt
import numpy as np
def bresenham_ellipse(rx, ry):
    # Initialize variables
    x, y = 0, ry

    ry2 = ry*ry
    rx2 = rx*rx

    rx2_times2 = rx2 + rx2
    ry2_times2 = ry2 + ry2

    dx = ry2_times2 * x
    dy =  rx2_times2 * y
    p1 = ry2 - rx2 * ry + rx2//4

    points = []

    # First region
    while dx < dy:
        points.append((x, y))
        x += 1
        dx += ry2_times2
        if p1 < 0:
            p1 += dx + ry2
        else:
            y -= 1
            dy -= rx2_times2
            p1 += dx - dy + ry2
    return points

# Example usage:
rx, ry = 10, 5  # radii
points = bresenham_ellipse(rx, ry)
for point in points:
    print(point)



scale = 79
grid_size = (2*scale+2,2*scale+2)
grid = np.zeros(grid_size)

x0,y0 = 1*scale,1*scale
rx = scale//2
ry = scale//6

#first region:
for x,y in bresenham_ellipse(rx,ry):
    grid[y+y0, x+x0] = 1
    grid[-y + y0, x + x0] = 1
    grid[-y + y0, -x + x0] = 1
    grid[y + y0, -x + x0] = 1
    #grid[x + y0, y + x0] = 1


#second region:
for y,x in bresenham_ellipse(ry,rx):
    grid[y+y0, x+x0] = 0.5
    grid[-y + y0, x + x0] =  0.5
    grid[-y + y0, -x + x0] =  0.5
    grid[y + y0, -x + x0] =  0.5



plt.imshow(grid, cmap='Greys', origin='lower')

plt.grid(True)
plt.show()

