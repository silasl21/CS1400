# Silas Loosli
# CS1400 - MWF 9:30
import time
import pygame
import player
import treasure
import enemy

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CLOCK_DELAY = 30
TITLE = "Tom and Jerry"

# Where do the changes appear?
def main():
    # Start with a welcome message:
    print("Welcome to cat and mouse")
    # Give the user choices for what they want the hardness to be
    print(f"Choose your difficulty:\n\tEasy (1)\n\tMedium (2)\n\tHard(3)")

    # Pygame initial setup
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # this is to be able to let the user put in the difficulty without pygame instantly starting up
    pygame.event.clear()
    pygame.event.wait()
    # difficulty choosing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        mouse_speed = 15
        cat_speed = 7
        num_cheeses = 10
        print("you selected easy")
    elif keys[pygame.K_2]:
        mouse_speed = 10
        cat_speed = 15
        num_cheeses = 10
        print("You selected medium")
    elif keys[pygame.K_3]:
        mouse_speed = 10
        cat_speed = 25
        num_cheeses = 10
        print("you selected hard")
    else:
        print("Well you didn't choose correctly so here's the hardest level")
        mouse_speed = 10
        cat_speed = 40
        num_cheeses = 100

    ####
    # Setup media/sound/images
    ####
    mouse_image = "Jerry.png"
    cat_image = "Tom.png"
    cheese_image = "Cheese.png"
    background_image = "background.jpg"

    # pictures
    background = pygame.image.load(background_image)

    # music
    bg_music = pygame.mixer.Sound("music.mp3")
    cheese_eat_sound = pygame.mixer.Sound("chomp.mp3")
    kill_sound = pygame.mixer.Sound("tom_laughing.mp3")
    win_sound = pygame.mixer.Sound("Winner.mp3")

    ####
    # Setup game data
    ####
    score = 0
    # create the actual objects needed
    cat = enemy.make_cat(cat_image, cat_speed, SCREEN_WIDTH, SCREEN_HEIGHT)
    mouse = player.make_mouse(mouse_image, mouse_speed, SCREEN_WIDTH, SCREEN_HEIGHT)

    # set up the treasure and determine where they will be placed
    cheese_list = []
    for i in range(num_cheeses):
        cheese_list.append(treasure.Cheese(screen, cheese_image, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Start the main loop
    game_over = False
    running = True
    timer_stop = False
    win = False
    elapsed = 0
    start_time = time.time()
    initial_time = time.time()
    bg_music.play(-1)
    while running:

        ####
        # Collect User Input/Events
        ####
        keys = pygame.key.get_pressed()
        # If the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # conditional for if the game is over and get replay value

        if game_over:

            # if the user presses space, reset the game
            if keys[pygame.K_SPACE]:
                game_over = False
                player.reset_mouse(mouse)
                enemy.reset_cat(cat)

                bg_music.play(-1)
                cheese_list = []
                for i in range(num_cheeses):
                    cheese_list.append(treasure.Cheese(screen, cheese_image, SCREEN_WIDTH, SCREEN_HEIGHT))
                start_time = time.time()
        else:
            # check for user input and make the corresponding movement
            if keys[pygame.K_UP]:
                player.move_mouse(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, 'y', -1)
            if keys[pygame.K_DOWN]:
                player.move_mouse(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, 'y', 1)
            if keys[pygame.K_RIGHT]:
                player.move_mouse(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, 1, 1)
            if keys[pygame.K_LEFT]:
                player.move_mouse(mouse, SCREEN_WIDTH, SCREEN_HEIGHT, -1, 1)

        ####
        # Update Game State
        ####

        screen.blit(background, [0, 0])

        # draw the items to the screen
        screen.blit(mouse.image, mouse.rect)
        screen.blit(cat.image, cat.rect)

        # Draw the num_cheeses and check for collisions
        for cheese in cheese_list:
            treasure.Cheese.draw(cheese)
            if mouse.rect.colliderect(cheese.rect):
                cheese_eat_sound.play()
                cheese_list.remove(cheese)
                score += 1

        ####
        # Update the Display
        ####

        if not game_over:
            win = False
            enemy.move_cat(cat, SCREEN_WIDTH, SCREEN_HEIGHT)

            # check for collision of cat and mouse
            if cat.rect.colliderect(mouse.rect):
                kill_sound.play()
                game_over = True
                score = 0
            # Check to see if the mouse has eaten all the cheese
            if len(cheese_list) == 0:
                game_over = True
                win = True
                win_sound.play()
            if game_over:
                timer_stop = True

        # basically end the game if the game is over
        else:
            bg_music.stop()
            # set a final time, needing to use this so that the loop doesn't increase the time indefinetely
            if timer_stop:
                stop_time = time.time()
                elapsed = round(stop_time - start_time, 2)
                timer_stop = False
            screen.blit(background, [0, 0])
            time_text = pygame.font.SysFont("timesnewroman", 60).render(f"Time: {elapsed} seconds ", True, "black")
            # if they win or loose, get a corresponding message for each
            if win:
                good_job = pygame.font.SysFont("timesnewroman", 70).render("Good Job!", True, "black")
                screen.blit(good_job, [SCREEN_WIDTH // 2 - good_job.get_width() // 2,
                                       SCREEN_HEIGHT // 2 - good_job.get_height() // 2])
            else:
                bad_job = pygame.font.SysFont("timesnewroman", 70).render("Better luck next time!", True, "black")
                screen.blit(bad_job, [SCREEN_WIDTH // 2 - bad_job.get_width() // 2, SCREEN_HEIGHT // 2 - bad_job.get_height() // 2])
            # place a time message underneath the entire message
            screen.blit(time_text, [SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2 + time_text.get_height()])
        score_text = pygame.font.SysFont("timesnewroman", 30).render(f"Score: {score}", True, "black")
        screen.blit(score_text, [SCREEN_WIDTH - (20 + score_text.get_width()), 20])

        # A little easter egg for kicks and giggles
        if score == 100:
            timer_stop = True
            if timer_stop:
                final_time = time.time()
                elapsed = round(final_time - initial_time, 2)
                timer_stop = False
            print("WELL DANG!! THAT'S SOME GOOD PLAYING!")
            print(f"and it only took you {elapsed} to get there!")
            score += 100011

        pygame.display.flip()
        clock.tick(CLOCK_DELAY)


main()
