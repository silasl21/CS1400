# Silas Loosli
# CS1400 - MWF 9:30
import pygame
from random import randint


class Cheese:
    def __init__(self, screen, filename, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load(filename)
        self.position = [randint(self.image.get_width() // 2, screen_width - self.image.get_width() // 2), randint(self.image.get_height() // 2, screen_height - self.image.get_height() // 2)]
        self.rect = self.image.get_rect(center=self.position)
    # pass

    def draw(self):
        self.screen.blit(self.image, self.rect)

    # def check_collide(self):
    #     import player
    #     did_collide = False
    #     if self.rect.colliderect(player.mouse.rect):
    #         did_collide = True
    #     else:
    #         self.screen.blit(self.image, self.rect)
    #     return did_collide

# def create_random_cheese(filename, screen_height, screen_width):
#     cheese = Cheese()
#
#     # Assign a picture to the cheese
#     cheese.image = pygame.image.load(filename)
#
#     # define the initial starting position
#     cheese.start_x = randint(0, screen_width)
#     cheese.start_y = randint(0, screen_height)
#
#     # Rectangle for the cheese
#     cheese.rect = cheese.image.get_rect(center=[cheese.start_x, cheese.start_y])
#
#     return cheese
