# Silas Loosli
# CS1400 - MWF 9:30

import drawly


def draw_chessboard(start_x, start_y, width=250, height=250):
    drawly.start("Chessmate!")
    drawly.set_speed(10)
    draw_rectangle(start_x, start_y, width, height, True)
    draw_all_rectangles(start_x, start_y, width, height)
    drawly.done()


def draw_rectangle(start_x, start_y, width, height, border=False):
    drawly.set_color("black")
    # conditional to place a border if the border value is true
    if border:
        drawly.rectangle(start_x, start_y, width, height, 1)
    else:
        drawly.rectangle(start_x, start_y, width, height)
    drawly.draw()


def draw_all_rectangles(start_x, start_y, width, height):
    rectangle_y = start_y
    for row in range(1, 9):
        # set the x-position to the beginning of the square
        rectangle_x = start_x

        # if it is an even row, add 1/8 the width to the start_x
        if row % 2 == 0:
            rectangle_x += width / 8

        # start a loop for the columns (there are 4)
        for column in range(4):
            draw_rectangle(rectangle_x, rectangle_y, width/8, height/8)

            # add 2/8 the width of the chessboard to the rectangle x-coordinate
            rectangle_x += (2 * width) / 8

        # move the y position to the next line
        rectangle_y += height / 8
