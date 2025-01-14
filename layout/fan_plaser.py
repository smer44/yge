import math

def fan_placer(center_x, center_y, radius, angle_mid, angle_step, num_points):
    """
    Generates points in a fan-like pattern on a 2D grid.

    :param center_x: X-coordinate of the center.
    :param center_y: Y-coordinate of the center.
    :param radius: Radius of the fan.
    :param angle_mid: Maximum angle (in degrees) of the fan.
    :param angle_step: Maximum angle (in degrees) of the fan.
    :param num_points: Number of points to generate.
    :return: A list of tuples representing the (x, y) coordinates of the points.
    """

    # Convert max_angle to radians for computation
    if num_points == 0:
        return []

    angle_div =  angle_step * (num_points-1)/2
    if angle_div >= 180:
        angle_div = 180 - 5
        angle_step = angle_div/(num_points-1)*2

    angle_begin = angle_mid  - angle_div

    points = []
    for i in range(num_points):
        angle =  math.radians(angle_begin)
        angle_begin+=angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))

    return points

points = fan_placer(100,100,70,-90,20,30)


#display with pygame:
import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Array of Points as Circles')

black = (0, 0, 0)
red = (255, 0, 0)
circle_radius = 5
running = True
while running:
    screen.fill(black)  # Fill the screen with white color
    for point in points:
        pygame.draw.circle(screen, red, point, circle_radius)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()