# Silas Loosli
# CS1400 - MWF 9:30

import drawly
import math
import random
from random import randint


def setup():
    drawly.start("Window Title")
    drawly.set_speed(10)

def get_distance_point(distance, angle):
    x_pos = distance * math.cos(math.radians(angle))
    y_pos = distance * math.sin(math.radians(angle))
    return[x_pos, y_pos]

def reset():
    drawly.redraw()

def set_random_color():
    colors = ["red", "aquamarine", "darkgoldenrod", "blue", "orange", "pink", "brown", "azure4", "cadetblue", "chartreuse4"]
    drawly.set_color(random.choice(colors))

def draw_rectangle_pattern(center_x, center_y, offset, height, width, count, rotation):
    for i in range(0, 360, int(360/count)):
        set_random_color()
        x = center_x + get_distance_point(offset, i)[0]
        y = center_y + get_distance_point(offset, i)[1]
        drawly.rectangle(x, y, width, height, 1, rotation_angle=((-i) + rotation), rotation_point=drawly.RotationPoint.TOP_LEFT)
        drawly.draw()



def draw_circle_pattern(center_x, center_y, offset, radius, count):
    for i in range(0, 360, int(360/count)):
        set_random_color()
        x = center_x + get_distance_point((radius + offset), i)[0]
        y = center_y + get_distance_point((radius + offset), i)[1]
        drawly.circle(x, y, radius, 1)
        drawly.draw()


def draw_super_pattern(num = 5):
    a = 1
    b = 750
    c = 200
    for i in range(num):
        random_choice = randint(0,1)
        if random_choice == 0:
            draw_rectangle_pattern(randint(a, b), randint(a, b), randint(a, c), randint(a, c),
                                          randint(a, c), randint(a, c), randint(a, c))

        else:
            draw_circle_pattern(randint(a, b), randint(a, b), randint(a, c), randint(a, c),
                                          randint(a, c))


def done():
    drawly.done()
