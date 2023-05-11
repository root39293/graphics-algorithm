import pygame

def mid_point_algorithm(screen, x1, y1, x2, y2, color, pixel_size):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        err = dx / 2
    else:
        err = -dy / 2

    while True:
        pygame.draw.rect(screen, color, (x1, y1, pixel_size, pixel_size))

        if x1 == x2 and y1 == y2:
            break

        e2 = err

        if e2 > -dx:
            err -= dy
            x1 += sx

        if e2 < dy:
            err += dx
            y1 += sy

def translation(points, dx, dy, color, pixel_size, screen):
    translated_points = []
    for point in points:
        translated_x = point[0] + dx
        translated_y = point[1] + dy
        translated_points.append((translated_x, translated_y))
    mid_point_algorithm(screen, translated_points[0][0], translated_points[0][1],
                  translated_points[1][0], translated_points[1][1], color, pixel_size)
    return translated_points

def draw_grid(screen, width, height, cell_size, color, font):
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, height))
        number_surface = font.render(str(x), True, color)
        screen.blit(number_surface, (x, 0))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, color, (0, y), (width, y))
        number_surface = font.render(str(y), True, color)
        screen.blit(number_surface, (0, y))
