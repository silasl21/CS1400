# Silas Loosli
# CS1400 - MWF 9:30
from random import randint
import pygame


class Critter:
    def __init__(self, screen, type, image):
        self.screen = screen
        # type is caught or killed
        self.type = type
        self.image = pygame.image.load(image)
        self.move_speed = [randint(-15, 15), randint(-15, 15)]
        self.position = [screen.get_width() // 2, screen.get_height() // 2]
        self.rect = self.image.get_rect(center=self.position)

    def draw(self):
        self.screen.blit(self.image, None)

    def move_critter(self):
        self.position[0] += self.move_speed[0]
        self.position[1] += self.move_speed[1]

    def check_bounce(self):
        if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
            self.move_speed[0] *= -1
        if self.rect.bottom >= self.screen.get_height() or self.rect.top <= 0:
            self.move_speed[1] *= -1

    def did_get(self, mouse_location):
        if self.rect.collidepoint(mouse_location):
            did_get = True
        else:
            did_get = False
        return did_get

    def make_critters_list(self, count, screen, images):
        good_critter_list = []
        bad_critter_list = []
        # count -- the number of critters in the list to return
        # images -- list of the critter images
        for i in range(count/2):
            good_critter_list.append(Critter(screen, "good", "wonk_parrot.png"))
            bad_critter_list.append(Critter(screen, "bad", "Angry_Bee.png"))

        critters_list = good_critter_list + bad_critter_list
        return critters_list
