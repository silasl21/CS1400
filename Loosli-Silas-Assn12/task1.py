# Silas Loosli
# CS1400 MWF 9:30
import time
import pygame
from media import images, sounds
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CLOCK_DELAY = 30
TITLE = "Lightcycle Runner"


def main():

    # Pygame initial setup
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ####
    # Setup media/sound/images
    ####
    # Sounds
    bg_music_1 = pygame.mixer.Sound("media/sounds/BG-music-1.mp3")
    player_1_turn = pygame.mixer.Sound("media/sounds/turn-1.mp3")
    player_2_turn = pygame.mixer.Sound("media/sounds/turn-2.mp3")

    # images #
    # Player 1 images
    player_1_vehicle = pygame.image.load("media/images/blue-car.png")
    player_1_trail_straight = pygame.image.load("media/images/blue-straight.png")
    player_1_trail_corner = pygame.image.load("media/images/blue-corner.png")
    player_1_images = [
        pygame.transform.rotate(player_1_vehicle, 0),
        pygame.transform.rotate(player_1_vehicle, 270),
        pygame.transform.rotate(player_1_vehicle, 180),
        pygame.transform.rotate(player_1_vehicle, 90)
    ]
    player_1_trails = [
        pygame.transform.rotate(player_1_trail_straight, 0),
        pygame.transform.rotate(player_1_trail_straight, 90),
        pygame.transform.rotate(player_1_trail_corner, 180),
        pygame.transform.rotate(player_1_trail_corner, 0),
        pygame.transform.rotate(player_1_trail_corner, 270),
        pygame.transform.rotate(player_1_trail_corner, 90),
    ]

    # player two images
    player_2_vehicle = pygame.image.load("media/images/red-car.png")
    player_2_trail_straight = pygame.image.load("media/images/red-straight.png")
    player_2_trail_corner = pygame.image.load("media/images/red-corner.png")
    player_2_images = [
        pygame.transform.rotate(player_2_vehicle, 0),
        pygame.transform.rotate(player_2_vehicle, 270),
        pygame.transform.rotate(player_2_vehicle, 180),
        pygame.transform.rotate(player_2_vehicle, 90)
    ]
    player_2_trails = [
        pygame.transform.rotate(player_2_trail_straight, 0),
        pygame.transform.rotate(player_2_trail_straight, 90),
        pygame.transform.rotate(player_2_trail_corner, 180),
        pygame.transform.rotate(player_2_trail_corner, 0),
        pygame.transform.rotate(player_2_trail_corner, 270),
        pygame.transform.rotate(player_2_trail_corner, 90),
    ]

    #combining the lists together for easier access
    player_images = [player_1_images, player_2_images]
    player_trails = [player_1_trails, player_2_trails]

    background_image = pygame.image.load("media/images/grid.png")
    loading_image_2 = pygame.image.load("media/images/retro-title-2.jpg")
    loading_image_1 = pygame.image.load("media/images/retro-title-1.jpg")

    bg_music_1.play()

    ####
    # Setup game data
    ####

    cell_size = 10
    game_grid = []
    player_1 = []
    player_2 = []
    num_rows = SCREEN_HEIGHT // cell_size
    num_cols = SCREEN_WIDTH // cell_size

    # Setting up a loading screen
    loading = True
    start_time = time.time()

    # Start the main loop
    game_over = False
    running = True
    while running:
        keys = pygame.key.get_pressed()
        ####
        # Collect User Input/Events
        ####

        # If the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_RETURN]:
            loading = False
        ####
        # Update Game State
        ####
        if running:

            if loading:
                loading_screen_time = time.time() // 2
                if loading_screen_time % 2 == 0:
                    screen.blit(loading_image_1, [0, 0])
                else:
                    screen.blit(loading_image_2, [0, 0])
            else:
                pass

        ####
        # Update the Display
        ####
            if not loading:
                bg_music_1.stop()
                # put stuff here to make the bikes move

                screen.blit(background_image, [0, 0])


        # Update display
        pygame.display.flip()
        clock.tick(CLOCK_DELAY)


main()
