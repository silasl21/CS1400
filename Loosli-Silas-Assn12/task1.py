import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CLOCK_DELAY = 30
TITLE = "Crashtopolis"


def main():

    # Pygame initial setup
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ####
    # Setup media/sound/images
    ####


    ####
    # Setup game data
    ####


    # Start the main loop
    game_over = False
    running = True
    while running:

        ####
        # Collect User Input/Events
        ####

        # If the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ####
        # Update Game State
        ####


        ####
        # Update the Display
        ####
    


        # Update display
        pygame.display.flip()
        clock.tick(CLOCK_DELAY)


main()
