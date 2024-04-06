# Silas Loosli
# CS1400 - MWF 9:30
import pygame


class Cat:
    pass


def make_cat(filename, cat_speed, screen_width, screen_height):
    cat = Cat()

    # Assign a picture to the enemy (tom)
    cat.image = pygame.image.load(filename)

    # define the initial starting position
    cat.start_x = screen_width // 2
    cat.start_y = screen_height // 2

    # Rectangle for the head
    cat.rect = cat.image.get_rect(center=[cat.start_x, cat.start_y])

    # define the speed
    cat.change_x = cat_speed - 2
    cat.change_y = cat_speed

    # return the cat object
    return cat


def move_cat(cat, screen_width, screen_height):
    # move the cat
    boing = pygame.mixer.Sound("boing.mp3")
    boing.set_volume(0.25)
    if cat.rect.right >= screen_width or cat.rect.left <= 0:
        cat.change_x *= -1
        boing.play()
    if cat.rect.top <= 0 or cat.rect.bottom >= screen_height:
        cat.change_y *= -1
        boing.play()
    cat.rect.x += cat.change_x
    cat.rect.y += cat.change_y



def reset_cat(cat):
    cat.rect = cat.image.get_rect(center=[cat.start_x, cat.start_y])
