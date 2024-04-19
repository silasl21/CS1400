# Silas Loosli
# CS1400 MWF 9:30
import pygame

# Direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
LINE = 4


# player 1 has a blue color, player 2 has a red color
class Player:
    def __init__(self, screen, player_number, draw_factor: int, player_image_list):
        self.__screen = screen
        self.__player_number = player_number

        # Setting the different image lists for the different characters
        self.__image_list = player_image_list[self.__player_number - 1]
        self.__draw_factor = draw_factor

    def draw(self, position, direction):

        draw_rect = pygame.Rect(
            position[0] * self.__draw_factor - self.__image_list[direction].get_width() // 5,
            position[1] * self.__draw_factor - self.__image_list[direction].get_width() // 5,
            self.__draw_factor, self.__draw_factor)

        self.__screen.blit(self.__image_list[direction], draw_rect)
