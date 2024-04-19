# Silas Loosli
# CS1400 - MWF 9:30
import time
import pygame
from cell import Cell, HORIZONTAL, VERTICAL, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT
from player import Player, UP, DOWN, LEFT, RIGHT

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CLOCK_DELAY = 30
TITLE = "LightCycle Runner"


def update_line_direction(previous_direction, current_direction):
    # Check to see if the line should be straight
    if previous_direction == current_direction:
        if previous_direction == RIGHT or previous_direction == LEFT:
            return HORIZONTAL
        if current_direction == DOWN or current_direction == UP:
            return VERTICAL

    # Check to see if it is curved
    else:
        # This one works now!!
        if previous_direction == DOWN and current_direction == LEFT or previous_direction == RIGHT and current_direction == UP:
            return DOWN_LEFT
        # This one works!
        elif previous_direction == UP and current_direction == LEFT or previous_direction == RIGHT and current_direction == DOWN:
            return UP_RIGHT
        # LAST ONE
        elif previous_direction == LEFT and current_direction == UP or previous_direction == DOWN and current_direction == RIGHT:
            return UP_LEFT
        # This one is correct
        elif previous_direction == LEFT and current_direction == DOWN or previous_direction == UP and current_direction == RIGHT:
            return DOWN_RIGHT
        else:
            return VERTICAL


def update_player(player, direction, game_grid):
    # get the position of the vehicle
    player_pos = [] + player[0].get_position()

    # modify the position as needed
    if direction == RIGHT:
        player_pos[0] += 1
    elif direction == LEFT:
        player_pos[0] -= 1
    elif direction == UP:
        player_pos[1] -= 1
    elif direction == DOWN:
        player_pos[1] += 1

    if 0 <= player_pos[0] < len(game_grid) and 0 <= player_pos[1] < len(game_grid[0]):

        # put the player at the front of the list
        player.insert(0, game_grid[player_pos[0]][player_pos[1]])

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
    bg_music_2 = pygame.mixer.Sound("media/sounds/BG-music-1.mp3")
    bg_music_1 = pygame.mixer.Sound("media/sounds/Arena.mp3")
    crash_sound = pygame.mixer.Sound("media/sounds/crash.wav")
    game_over_music = pygame.mixer.Sound("media/sounds/Disc_Wars.mp3")
    player_1_turn = pygame.mixer.Sound("media/sounds/turn-1.mp3")
    player_2_turn = pygame.mixer.Sound("media/sounds/turn-2.mp3")
    player_1_did_turn = False
    player_2_did_turn = False

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
    # Set up Game Data
    ####

    cell_size = 10
    game_grid = []
    num_rows = SCREEN_HEIGHT // cell_size
    num_cols = SCREEN_WIDTH // cell_size

    player_1_direction = UP
    player_2_direction = UP

    # create the players and their respective bits necessary
    player_1 = Player(screen, 1, cell_size, player_images)
    player_1_list = []
    player_2 = Player(screen, 2, cell_size, player_images)
    player_2_list = []

    # Get the grid set up
    for col in range(num_cols):
        # add an empty col list to the game grid
        game_grid.append([])
        for row in range(num_rows):
            game_grid[col].append(Cell(screen, [col, row], cell_size, player_trails))

    # add a player to the game grid, we'll figure out a second later
    player_1_list.append(game_grid[num_cols // 4][num_rows - 1])
    player_2_list.append(game_grid[num_cols // 2 + num_cols // 4][num_rows - 1])

    ####
    # Game Loop
    ####

    game_over = False
    running = True
    winner = None
    loading = True
    while running:
        ####
        # Get input/Events
        ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if loading:
                bg_music_2.play(-1)
                loading = False
                bg_music_1.stop()

        # player 1
        player_1_direction_prev = player_1_direction
        if keys[pygame.K_w]:
            player_1_direction = UP
            player_1_did_turn = True
        elif keys[pygame.K_a]:
            player_1_direction = LEFT
            player_1_did_turn = True
        elif keys[pygame.K_s]:
            player_1_direction = DOWN
            player_1_did_turn = True
        elif keys[pygame.K_d]:
            player_1_direction = RIGHT
            player_1_did_turn = True
        if player_1_did_turn and not loading:
            player_1_turn.play()
            player_1_did_turn = False

        # player 2
        player_2_direction_prev = player_2_direction
        if keys[pygame.K_UP]:
            player_2_direction = UP
            player_2_did_turn = True
        elif keys[pygame.K_LEFT]:
            player_2_direction = LEFT
            player_2_did_turn = True
        elif keys[pygame.K_DOWN]:
            player_2_direction = DOWN
            player_2_did_turn = True
        elif keys[pygame.K_RIGHT]:
            player_2_direction = RIGHT
            player_2_did_turn = True
        if player_2_did_turn and not loading:
            player_2_turn.play()
            player_2_did_turn = False

        ####
        # Update State of Components and game data
        ####
        if not game_over:
            # present the loading screen
            if loading:
                loading_screen_time = time.time() // 0.85
                if loading_screen_time % 2 == 0:
                    screen.blit(loading_image_1, [0, 0])
                else:
                    screen.blit(loading_image_2, [0, 0])
            else:

                # update the player
                # if the blue player hits anything
                if not update_player(player_2_list, player_2_direction, game_grid):
                    game_over = True
                    winner = 2
                    crash_sound.play()
                    game_over_music.play(-1)
                    continue
                if player_1_list[0] in player_1_list[1:] or player_1_list[0] in player_2_list:
                    game_over = True
                    winner = 2
                    crash_sound.play()
                    game_over_music.play(-1)
                    continue

                # update if the red player hits anything
                if not update_player(player_1_list, player_1_direction, game_grid):
                    game_over = True
                    winner = 1
                    crash_sound.play()
                    game_over_music.play(-1)
                    continue

                if player_2_list[0] in player_2_list[1:] or player_2_list[0] in player_1_list:
                    game_over = True
                    winner = 2
                    crash_sound.play()
                    game_over_music.play(-1)
                    continue

                # set the correct line image for behind the cars
                player_1_list[1].set_state(update_line_direction(player_1_direction_prev, player_1_direction))
                player_2_list[1].set_state(update_line_direction(player_2_direction_prev, player_2_direction))

        ####
        # Update the Display
        ####
        if not loading:
            screen.blit(background_image, [0, 0])

            # draw player 1 line
            for cell in range(len(player_1_list)):
                player_1_list[cell].draw_cell(1)

            # draw player 2 line
            for cell in range(len(player_2_list)):
                player_2_list[cell].draw_cell(2)

            # draw the players themselves:
            player_1.draw(player_1_list[0].get_position(), player_1_direction)
            player_2.draw(player_2_list[0].get_position(), player_2_direction)

        if game_over:
            # print a message to the screen of who won
            bg_music_2.stop()
            bg_music_2.stop()
            text_font = pygame.font.SysFont("timesnewroman", 100)
            msg = text_font.render("Game Over", True, "White")
            screen.blit(msg, [SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - msg.get_height()])
            winner_msg = text_font.render(f"Player {winner} wins!", True, "White")
            screen.blit(winner_msg, [SCREEN_WIDTH // 2 - winner_msg.get_width() // 2, SCREEN_HEIGHT // 2])
            if keys[pygame.K_RETURN]:
                game_over = False
                player_1_list, player_2_list = [], []
                player_1_direction, player_2_direction = UP, UP
                player_1_list.append(game_grid[num_cols // 4][num_rows - 1])
                player_2_list.append(game_grid[num_cols // 2 + num_cols // 4][num_rows - 1])
                bg_music_2.play(-1)
                game_over_music.stop()

        ###
        # Update the changes to the screen
        pygame.display.flip()

        ####
        # Define the refresh rate
        ####
        clock.tick(CLOCK_DELAY)

    pygame.quit()


main()
