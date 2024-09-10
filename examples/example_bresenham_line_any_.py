import numpy as np
import matplotlib.pyplot as plt


def bresenham_line_any(x0, y0, x1, y1):
    print(f" {x0, y0, x1, y1 =}")
    # Create a list to store the points of the line
    #points = []

    # Calculate the differences between the points
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    points_len = max(dx,dy)+1
    points = np.zeros(shape=(points_len, 2) ,dtype=np.int32)
    # Determine the direction of the increments
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    # Initialize the error term
    err = dx - dy

    for n in range(points_len):
        # Add the current point to the list of points
        print(f"{x0,y0=}")
        points[n,0]=x0
        points[n, 1] = y0

        # Calculate the error term for the next step
        e2 = err + err

        # Adjust the error term and move the point accordingly
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    #print(f"{len(points)=}, {x0, y0, x1, y1 =}")
    return points


# Example usage:
x0, y0 = 10, 9
x1, y1 = 3, 10

x0, y0 = 9, 3
x1, y1 = 11, 10

line_points = bresenham_line_any(x0, y0, x1, y1)

# Plot the line using matplotlib
grid_size = (15, 15)
grid = np.zeros(grid_size)

for x,y in line_points:
    grid[y, x] = 1  # Set the pixel at each point

plt.imshow(grid, cmap='Greys', origin='lower')
plt.grid(True)
plt.show()
