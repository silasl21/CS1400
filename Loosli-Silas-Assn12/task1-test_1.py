# Silas Loosli
# CS1400 MWF 9:30
import time
import pygame
from cell import Cell, EMPTY, HORIZONTAL, VERTICAL, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT
from player import Player, UP, DOWN, LEFT, RIGHT

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CLOCK_DELAY = 30
TITLE = "LightCycle Runner"


def update_player(player, direction, game_grid):
    # Get the position of the player
    player_pos = [] + player.get_position()

    # modify the position as needed
    if direction == RIGHT:
        player_pos[0] += 1
    elif direction == LEFT:
        player_pos[0] -= 1
    elif direction == UP:
        player_pos[1] -= 1
    elif direction == DOWN:
        player_pos[1] += 1

    if 0 <= player_pos[0] < len(game_grid) and 0 <= player_pos[1] < len(game_grid[0]) and game_grid[0][1].get_type() == EMPTY:

        # put the player at the front of the list
        player.set_position(player_pos)

        # throw a game over flag if a bike goes into the side
        return True
    else:
        return False


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

    # combining the lists together for easier access
    player_images = [player_1_images, player_2_images]
    player_trails = [player_1_trails, player_2_trails]

    background_image = pygame.image.load("media/images/grid.png")
    loading_image_2 = pygame.image.load("media/images/retro-title-2.jpg")
    loading_image_1 = pygame.image.load("media/images/retro-title-1.jpg")

    bg_music_1.play(-1)

    ####
    # Setup game data
    ####

    cell_size = 10
    game_grid = []
    player_1 = []
    player_2 = []
    num_rows = SCREEN_HEIGHT // cell_size
    num_cols = SCREEN_WIDTH // cell_size

    # setting up the rows and columns
    for col in range(num_cols):
        game_grid.append([])
        for row in range(num_rows):
            game_grid[col].append(Cell(screen, [col, row], cell_size, player_trails))

    # game_grid[num_cols // 3][num_rows - 1] = Player(screen, 1, [num_cols // 3, num_rows - 1], cell_size, player_images)
    # game_grid[(num_cols // 3) * 2][num_rows - 1] = Player(screen, 2, [(num_cols // 3) * 2, num_rows - 1], cell_size,
    #                                                       player_images)

    player_1 = Player(screen, 1, [num_cols // 3, num_rows - 1], cell_size, player_images)
    player_2 = Player(screen, 2, [(num_cols // 3) * 2, num_rows - 1], cell_size, player_images)

    # Setting up a loading screen
    loading = True
    start_time = time.time()

    # Start the main loop
    game_over = False
    running = True
    player_1_direction = UP
    player_2_direction = UP
    test = True
    while running:

        ####
        # Collect User Input/Events
        ####

        keys = pygame.key.get_pressed()

        # player 1
        if keys[pygame.K_w]:
            player_1_direction = UP
        elif keys[pygame.K_a]:
            player_1_direction = LEFT
        elif keys[pygame.K_s]:
            player_1_direction = DOWN
        elif keys[pygame.K_d]:
            player_1_direction = RIGHT

        # player 2
        elif keys[pygame.K_UP]:
            player_2_direction = UP
        elif keys[pygame.K_LEFT]:
            player_2_direction = LEFT
        elif keys[pygame.K_DOWN]:
            player_2_direction = DOWN
        elif keys[pygame.K_RIGHT]:
            player_2_direction = RIGHT

        # If the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # set up the loading screen
        if keys[pygame.K_RETURN]:
            loading = False
        ####
        # Update Game State
        ####
        if not game_over:
            # getting a screen that flashes with press enter to start
            if loading:
                loading_screen_time = time.time() // 0.85
                if loading_screen_time % 2 == 0:
                    screen.blit(loading_image_1, [0, 0])
                else:
                    screen.blit(loading_image_2, [0, 0])
            else:
                if not game_over:
                    game_over = not update_player(player_1, player_1_direction, game_grid)
                    game_over = not update_player(player_2, player_2_direction, game_grid)

                # draw the players



            ####
            # Update the Display
            ####
            if not loading:
                screen.blit(background_image, [0, 0])
                bg_music_1.stop()
                # put stuff here to make the bikes move
                for col in game_grid:
                    for item in col:
                        item.draw(1)
                player_1.draw(1)
                player_2.draw(2)



        # Update display
        pygame.display.flip()
        clock.tick(CLOCK_DELAY)


main()
