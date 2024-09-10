import numpy as np

import numpy as np
from yge.turnbased.brezenheim_vectors import  my_bresenham_line_vectors


def fill_gradient_array(array, axis, *args):
    """
    Fill the NumPy array with a gradient along the specified axis.

    :param array: NumPy array to fill, with shape (height, width, 3) for RGB values.
    :param axis: 'horizontal' or 'vertical', the direction of the gradient.
    :param args: Gradient color and position pairs, e.g. (color1, position1, color2, position2, ...).
                 Each color is an (R, G, B) tuple, and each position is a float from 0 to 1.
    """
    height, width, _ = array.shape

    # Parse the input gradients into separate color and position lists
    colors = np.array([args[i] for i in range(0, len(args), 2)])


    if axis == 'horizontal':
        axis_length = width
    elif axis == 'vertical':
        axis_length = height
    else:
        raise ValueError("Axis must be 'horizontal' or 'vertical'")
    positions = [int(args[i + 1] *axis_length)  for i in range(0, len(args), 2)]
    #fools protection:
    positions[0] = 0
    positions[-1] = axis_length

    for position_from_id in range(len(positions)-1):
        position_from = positions[position_from_id]
        position_to = positions[position_from_id+1]
        color_from = colors[position_from_id]
        color_to = colors[position_from_id+1]

        colors_in_range = my_bresenham_line_vectors(position_from, color_from, position_to-1, color_to)
        if axis == 'horizontal':
            array[:, position_from:position_to] = colors_in_range
        else:
            shape = colors_in_range.shape
            new_shape = (shape[0],1,shape[1])
            array[position_from:position_to,:] = colors_in_range.reshape(new_shape)
