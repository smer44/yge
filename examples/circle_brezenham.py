import matplotlib.pyplot as plt
import numpy as np
def brezenham_circle_one_eighth(r):

    x0 = 0
    y0 = r
    d = 3-2*r
    yield(x0,y0)
    while y0 >= x0:
        if d <=0:
            x0+=1
            d = d+4*x0+4
            #makes rhombus shape soft conrens:
            #d = d + 4 * x0 + 4
        else:
            x0 += 1
            y0 -= 1
            d = d + 4 * (x0-y0)+4
        yield(x0,y0)

for x,y in brezenham_circle_one_eighth(8):
    print(x,y)


scale = 1*20
grid_size = (20*scale,20*scale)
grid = np.zeros(grid_size)

x0,y0 = 10*scale,10*scale
r = 8 * scale
for x,y in brezenham_circle_one_eighth(r):
    grid[y+y0, x+x0] = 1
    grid[x + y0, y + x0] = 1

    grid[-y + y0, x + x0] = 0.9
    grid[-x + y0, y + x0] = 0.9

    grid[-y + y0, -x + x0] = 0.8
    grid[-x + y0, -y + x0] = 0.8

    grid[y + y0, -x + x0] = 0.7
    grid[x + y0, -y + x0] = 0.7

plt.imshow(grid, cmap='Greys', origin='lower')

plt.grid(True)
plt.show()

