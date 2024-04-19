# Silas Loosli
# CS1400 MWF 9:30
import pygame

EMPTY = -1
VERTICAL = 0
HORIZONTAL = 1
DOWN_LEFT = 2
DOWN_RIGHT = 3
UP_RIGHT = 4
UP_LEFT = 5
VEHICLE = 6


class Cell:
    def __init__(self, screen, position, draw_factor: int, image_list):
        self.__screen = screen
        self.__state = -1
        self.__position = position
        self.__draw_rect = pygame.Rect(position[0] * draw_factor, position[1] * draw_factor, 10, 10)
        # Setting the different image lists for the different characters
        self.__image_list = image_list

    def draw_cell(self, player_number):
        self.__screen.blit(self.__image_list[player_number - 1][self.__state], self.__draw_rect)

    def get_position(self):
        return self.__position

    def set_state(self, state):
        self.__state = state
