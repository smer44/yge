import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyGame Text Styling Tutorial")

# Set up the font
font = pygame.font.Font(None, 74)


def draw_rect_text(surface, text, font, x, y, text_color, rect_color):
    main_text = font.render(text, True, text_color)
    text_rect = main_text.get_rect(topleft=(x, y-3))
    pygame.draw.rect(surface,rect_color,text_rect,2)
    surface.blit(main_text, (x, y))


def draw_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_width=4):
    #lets store the outline result on the surface:
    main_text = font.render(text, True, text_color)
    text_rect = main_text.get_rect(topleft=(x, y))
    outlineStoredSurface = pygame.Surface((text_rect.width + outline_width +outline_width, text_rect.height + outline_width+outline_width))

    for dx in range(0, outline_width + outline_width+1):
        for dy in range(0, outline_width+outline_width+1):
            if dx != 0 and dy != 0:
                outline_text = font.render(text, True, outline_color)
                outlineStoredSurface.blit(outline_text, ( dx,  dy))
    #main_text = font.render(text, True, text_color)

    surface.blit(outlineStoredSurface, (x-outline_width, y-outline_width))
    surface.blit(main_text, (x, y))

def draw_shadowed_text(surface, text, font, x, y, text_color, shadow_color, shadow_offset=(2, 2)):
    shadow_text = font.render(text, True, shadow_color)


    main_text = font.render(text, True, text_color)
    # shadow_text.set_alpha(shadowAlpha)
    surface.blit(shadow_text, (x + shadow_offset[0], y + shadow_offset[1]))
    surface.blit(main_text, (x, y))

# you can make blured shadow by use outline by shift method.


def draw_diagonal_gradient_rect(w,h, start_color, end_color):
    screen =pygame.Surface((w,h))
    for i in range(w):
        for j in range(h):
            # Calculate the ratio for the current position
            ratio = (i / w + j / h) / 2

            # Interpolate between the start and end colors
            r = start_color[0] + ratio * (end_color[0] - start_color[0])
            g = start_color[1] + ratio * (end_color[1] - start_color[1])
            b = start_color[2] + ratio * (end_color[2] - start_color[2])
            color = (int(r), int(g), int(b))

            # Draw the pixel at the current position
            screen.set_at(( i, j), color)
    return screen

def apply_surface_to_text(output_surface, text, font, color_surface, x, y):
    text_surface = font.render(text, True, (0,0,0))
    text_surface.blit(color_surface, (0, 0), special_flags=pygame.BLEND_RGB_MAX)
    output_surface.blit(text_surface, (x, y))




def draw_gradient_text(surface, text, font, x, y, start_color, end_color):
    text_surface = font.render(text, True, start_color)
    text_width, text_height = text_surface.get_size()
    gradient_surface = pygame.Surface((text_width, text_height), pygame.SRCALPHA)
    for i in range(text_height):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // text_height
        g = start_color[1] + (end_color[1] - start_color[1]) * i // text_height
        b = start_color[2] + (end_color[2] - start_color[2]) * i // text_height
        pygame.draw.line(gradient_surface, (r, g, b), (0, i), (text_width, i))
    text_surface.blit(gradient_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    surface.blit(text_surface, (x, y))

#TODO need to create surface for this stuff:
def draw_gradient_rect(screen, rect, start_color, end_color, horizontal=True):
    x, y, w, h = rect

    if horizontal:
        for i in range(w):
            # Calculate the color at this point
            ratio = i / w
            r = start_color[0] + ratio * (end_color[0] - start_color[0])
            g = start_color[1] + ratio * (end_color[1] - start_color[1])
            b = start_color[2] + ratio * (end_color[2] - start_color[2])
            color = (int(r), int(g), int(b))
            # Draw a vertical line at this point
            pygame.draw.line(screen, color, (x + i, y), (x + i, y + h))
    else:
        for i in range(h):
            # Calculate the color at this point
            ratio = i / h
            r = start_color[0] + ratio * (end_color[0] - start_color[0])
            g = start_color[1] + ratio * (end_color[1] - start_color[1])
            b = start_color[2] + ratio * (end_color[2] - start_color[2])
            color = (int(r), int(g), int(b))
            # Draw a horizontal line at this point
            pygame.draw.line(screen, color, (x, y + i), (x + w, y + i))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill the screen with black

    # Render and display the different styled texts
    draw_rect_text(screen , "Rect text", font,100, 50,(255, 255, 255), (110, 110, 255))
    draw_outlined_text(screen, "Outlined Text", font, 100, 150, (255, 255, 255), (110, 110, 255))
    draw_shadowed_text(screen, "Shadowed Text", font, 100, 250, (255, 255, 255), (150, 150, 150),(10,10))
    draw_gradient_text(screen, "Gradient Text", font, 100, 350, (255, 0, 0), (0, 0, 255))
    draw_gradient_rect(screen,(100, 450, 100, 50), (255, 255, 0),(128, 0, 255) ,False )

    #ahh, i need the size for that
    color_surface = draw_diagonal_gradient_rect(400,50,(0, 255, 255),(255, 0,0 ))
    apply_surface_to_text(screen, "Applied surface", font, color_surface, 100, 550)

    pygame.display.flip()
