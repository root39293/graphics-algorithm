from pygame_util import initialize_pygame, process_events, update_screen
from midpoint import mid_point_algorithm, translation, draw_grid

def main():
    screen_width, screen_height = 500, 500
    pixel_size = 2
    cell_size = 50
    grid_color = (100, 100, 100)
    font_size = 20
    screen, clock, font = initialize_pygame(screen_width, screen_height, font_size)
    x1 = int(input("x1 좌표 입력: "))
    y1 = int(input("y1 좌표 입력: "))
    x2 = int(input("x2 좌표 입력: "))
    y2 = int(input("y2 좌표 입력: "))
    tx = int(input("tx 좌표 입력: "))
    ty = int(input("ty 좌표 입력: "))

    mid_point_algorithm(screen, x1, y1, x2, y2, (255, 255, 255), pixel_size)

    points = [(x1, y1), (x2, y2)]
    translated_points = translation(points, tx, ty, (255, 0, 0), pixel_size, screen)
    draw_grid(screen, screen_width, screen_height, cell_size, grid_color, font)

    running = True
    while running:
        process_events()
        update_screen()

if __name__ == "__main__":
    main()
