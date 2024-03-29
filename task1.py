# Silas Loosli
# CS1400 - MWF 9:30
import pygame
import critter

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_DELAY = 30
TITLE = "The birds and the bees"


def main():
    # setup pygame
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Setup media here: #
    # images
    bg_image = pygame.image.load("background.jpg")

    # music and sounds
    bg_music = pygame.mixer.Sound("Minecraft.mp3")
    catch_sound = pygame.mixer.Sound("catch.mp3")

    # setup the game data #

    # turn off the mouse
    pygame.mouse.set_visible(False)

    # Start the main loop #
    game_over = False
    running = True
    catch = True
    while running:
        # collect User Input/Events
        mouse_pos = pygame.mouse.get_pos()
        # if the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the game state #
        # background!
        screen.blit(bg_image, [0, 0])
        # Update with blits

        # update the display
        pygame.display.flip()
        clock.tick(CLOCK_DELAY)

main()
