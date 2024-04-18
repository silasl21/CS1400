# Silas Loosli
# CS1400 MWF 9:30
import pygame

# Direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


# player 1 has a blue color, player 2 has a red color
class Bike:
    def __init__(self, screen, player_number, position, draw_factor: int, player_image_list):
        self.__screen = screen
        self.__draw_rect = pygame.Rect(position[0] * draw_factor, position[1] * draw_factor, 10, 10)
        self.__player_number = player_number
        # Setting the different image lists for the different characters
        self.__image_list = player_image_list[player_number - 1]
        self.__state = -1
        self.__position = position

    def draw(self):
        # self.__screen.blit(self.__image_list[], self.__draw_rect) -- this is only needed if this function
        # also draws the background, but it doesn't
        if self.__state != -1:
            self.__screen.blit(self.__image_list[self.__state], self.__position)
