# Silas Loosli
# CS1400 MWF - 9:30
import pygame


class Mouse:
    pass


def make_mouse(filename, mouse_speed, screen_width, screen_height):
    mouse = Mouse()

    # give the enemy a picture of the mouse
    mouse.image = pygame.image.load(filename)

    # define the initial starting position
    mouse.start_x = screen_width // 2
    mouse.start_y = screen_height - (mouse.image.get_height() // 2)

    # create a rectangle
    mouse.rect = mouse.image.get_rect(center=[mouse.start_x, mouse.start_y])

    # set the speed of the mouse
    mouse.move_distance = mouse_speed

    return mouse


def move_mouse(mouse, screen_width, screen_height, direction, movement=0):
    # get the mouse to move in the specified direction
    if direction == "y":
        mouse.rect.y += mouse.move_distance * movement
    else:
        mouse.rect.x += mouse.move_distance * direction

    # make the mouse unable to move past the sides
    if mouse.rect.top < 0:
        mouse.rect.top = 0
    if mouse.rect.bottom > screen_height:
        mouse.rect.bottom = screen_height
    if mouse.rect.left < 0:
        mouse.rect.left = 0
    if mouse.rect.right > screen_width:
        mouse.rect.right = screen_width

def reset_mouse(mouse):
    mouse.rect = mouse.image.get_rect(center=[mouse.start_x, mouse.start_y])
