# Silas Loosli
# CS1400 MWF 9:30
import pygame

EMPTY = -1
VERTICAL = 0
HORIZONTAL = 1
DOWN_LEFT = 2
DOWN_RIGHT = 3
UP_LEFT = 4
UP_RIGHT = 5

class Cell:
    def __init__(self, screen, player_number, position, draw_factor: int, image_list):
        self.__screen = screen
        self.__state = EMPTY
        self.__position = position
        self.__draw_rect = pygame.Rect(position[0] * draw_factor, position[1] * draw_factor, 10, 10)
        self.__player_number = player_number
        # Setting the different image lists for the different characters
        self.image_list = image_list[player_number - 1]
