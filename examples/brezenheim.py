import numpy as np
import matplotlib.pyplot as plt

def my_bresenham_line(x0, y0, x1, y1):
    print(f" {x0, y0, x1, y1 =}")
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    points_len = max(dx, dy) + 1
    points = np.zeros(shape=(points_len, 2), dtype=np.int32)
    #points[-1,0] = x1
    #points[-1, 1] = y1
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    if dx >= dy:
        __brezenham_loop__(points, points_len, x0,y0, dx, dy,sx,sy, 0,1)
    else:
        __brezenham_loop__(points, points_len, y0, x0, dy, dx, sy, sx, 1, 0)

    return points

def __brezenham_loop__(points, points_len, x,y, dx, dy,sx,sy, xpos,ypos):
    err = dx- dy
    for n in range(points_len):
        points[n, xpos] = x
        points[n, ypos] = y
        print(f"{x,y=}")
        # Calculate the error term for the next step
        e2 =  err + err
        if e2 < dx:
            err += dx
            y += sy

        err -= dy
        x += sx

def my_bresenham_line_vectors(x0, y0, x1, y1):
    print(f" {x0, y0, x1, y1 =}")
    #dxs = x1 - x0
    dx = abs(x1 - x0)
    dy0_sing = y1-y0
    dy0 = np.abs(dy0_sing)
    if np.all(dx >=dy0):
        return my_bresenham_line_vectors_big_dx(x0,y0,x1,dx,dy0,dy0_sing)


    y = np.copy(y0)

    sx = 1 if x0 < x1 else -1

    #ystep = np.round(dy/max(dx,1)).astype(int)

    sy0 = np.sign(dy0_sing) * np.round(dy0/max(dx,1)).astype(int)

    #sy[2] = -3
    all_d = dx*sy0
    dys = dy0_sing-all_d
    dy = np.abs(dys)
    assert all(dy < dx)
    sy = np.sign(dys)
    print(f"{dy0_sing=}")
    print(f"{dys=}")
    print(f"{sy=}")
    err = dx - dy
    #now, dx > dys2
    err = dx-dy

    points_len = dx + 1
    points = np.zeros(shape=(points_len, len(y0)), dtype=np.int32)

    for n in range(points_len):
        points[n] = y
        x0 += sx

        y +=sy0

        ed =  err+err
        indices = ed < dx

        err[indices] += dx
        y[indices] += sy[indices]
        err-= dy







    return points

def my_bresenham_line_vectors_big_dx(x0, y0, x1, dx,dy,dys):
    #print(f"my_bresenham_line_vectors_big_dx: {x0, y0, x1, y1 =}")
    y = np.copy(y0)

    #points[-1,0] = x1
    #points[-1, 1] = y1
    sx = 1 if x0 < x1 else -1

    #ystep = np.round(dy/max(dx,1)).astype(int)

    sy = np.sign(dys)

    #sy[2] = -2
    print(f"{dys=}")
    print(f"{sy=}")
    err = dx - dy

    points_len = dx + 1
    points = np.zeros(shape=(points_len, len(y)), dtype=np.int32)

    for n in range(points_len):
        points[n] = y
        x0 += sx
        ed =  err+err
        indices = ed < dx
        err[indices] += dx
        y[indices] += sy[indices]
        err-= dy
    return points

def myrange(a,b,step=1):
    if a <= b:
        return range(a,b+1,step)
    return range(a, b-1, -step)


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
