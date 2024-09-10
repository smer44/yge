import numpy as np

def my_bresenham_dots_single(x0, y0, x1, y1):
    print(f"my_bresenham_line_vectors: {x0, y0, x1, y1 =}")
    dx = abs(x1 - x0)
    dy0_sing = y1 - y0
    dy0 = abs(dy0_sing)
    if dx > dy0:
        return __my_bresenham_dots_single_big_dx__(x0, y0, x1, dx, dy0, dy0_sing)

    sx = 1 if x0 < x1 else -1

    sy0 = 1 if dy0_sing > 0 else -1
    sy0 = sy0 * int(dy0 / max(dx, 1))
    all_d = dx*sy0
    dys = dy0_sing-all_d
    dy = abs(dys)
    assert dy < dx
    sy = 1 if dys > 0 else -1
    err = dx - dy
    points_len = dx + 1
    points = np.zeros(shape=(points_len), dtype=np.int32)
    for n in range(points_len):
        points[n] = y0
        x0 += sx
        y0 +=sy0
        ed =  err+err
        if ed < dx:

            err += dx
            y0 += sy
        err-= dy
    return points


def __my_bresenham_dots_single_big_dx__(x0, y, x1, dx,dy,dys):
    """
    Bresenham method, making only one y value for each x,
    havin y as single value
    :param x0:
    :param y:
    :param x1:
    :param dx:
    :param dy:
    :param dys:
    :return: numpy array with y - values
    """
    sx = 1 if x0 < x1 else -1
    sy = 1 if dys > 0 else -1

    err = dx- dy
    assert err >= 0
    points_len = dx + 1
    points = np.zeros(shape=(points_len), dtype=np.int32)

    for n in range(points_len):
        points[n] = y
        x0 += sx
        ed = err + err
        if ed < dx:
            err +=dx
            y+=sy
        err -= dy
    return points


def bresenham_line(x0, y0, x1, y1):

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
        #print(f"{x0,y0=}")
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