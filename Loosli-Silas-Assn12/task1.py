# Silas Loosli
# CS1400 MWF 9:30

import pygame

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
    bg_music_1 = pygame.mixer.Sound("BG-music-1.mp3")
    bg_music_2 = pygame.mixer.Sound("BG-music-1.mp3")
    player_1_turn = pygame.mixer.Sound("turn-1.mp3")
    player_2_turn = pygame.mixer.Sound("turn-2.mp3")

    # images #
    # Player 1 images
    player_1_vehicle = pygame.image.load("blue-car.png")
    player_1_trail_straight = pygame.image.load("blue-straight.png")
    player_1_trail_corner = pygame.image.load("blue-corner.png")
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
    player_2_vehicle = pygame.image.load("red-car.png")
    player_2_trail_straight = pygame.image.load("red-straight.png")
    player_2_trail_corner = pygame.image.load("red-corner.png")
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

    bg_music_1.play()
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
