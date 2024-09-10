import numpy as np


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
    #print(f"{dy0_sing=}")
    #print(f"{dys=}")
    #print(f"{sy=}")
    #err = dx - dy
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
    #print(f"{dys=}")
    #print(f"{sy=}")
    err = dx - dy
    assert err >= 0
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






