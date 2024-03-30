# Silas Loosli
# CS1400 - MWF 9:30
import time
import pygame
from critter import Critter, make_critters_list

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
    count = 10

    # Setup media here: #
    # images
    bg_image = pygame.image.load("background.jpg")
    catch_mouse = pygame.image.load("fishing_rod.png")
    kill_mouse = pygame.image.load("Arrow_Loaded_Crossbow.png")

    # music and sounds
    bg_music = pygame.mixer.Sound("Minecraft.mp3")   # assigned to list 0
    reel_sound = pygame.mixer.Sound("catch.mp3")   # assigned to list in position 1
    shoot_sound = pygame.mixer.Sound("bow_shoot.mp3")   # assigned to played list in position 2
    tool_good_sound = pygame.mixer.Sound("Small_xp.mp3")   # assigned to played list in position 3
    level_complete_sound = pygame.mixer.Sound("Large_xp.mp3")   # position 4
    bad_sound = pygame.mixer.Sound("Minecraft_oof.mp3")   # position 5

    # set up the game data #
    critters_list = make_critters_list(count, screen, ["wonk_parrot.png", "Angry_Bee.png"])

    # turn off the mouse
    pygame.mouse.set_visible(False)

    # Start the main loop #
    round_over = False
    running = True
    win = False
    mouse_type = 1
    bg_music.play(-1)
    init_start_time = time.time()
    while running:
        clicked = False
        # collect User Input/Events
        # this is so that the sounds only play once hopefully
        sounds = [False, False, False, False, False, False]
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed(3)[0]
        # if the user exits the program, break out of the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the game state #

        # add in sounds for each item:
        if clicked:
            if mouse_type == 1:
                pygame.mixer.Sound.play(reel_sound)
            else:
                pygame.mixer.Sound.play(shoot_sound)

        # move the critters
        screen.blit(bg_image, [0, 0])

        # handle the critters in critters_list
        for critter in critters_list:
            Critter.check_bounce(critter)

            # checking to see if the mouse got clicked
            if not round_over:
                if Critter.did_get(critter, clicked, mouse_pos, mouse_type) == [True, False]:
                    pygame.mixer.Sound.play(bad_sound)
                    round_over = True
                    win = False

                elif Critter.did_get(critter, clicked, mouse_pos, mouse_type) == [True, True]:
                    critters_list.remove(critter)
                    pygame.mixer.Sound.play(tool_good_sound)
                    mouse_type *= -1

                if len(critters_list) == 0:
                    round_over = True
                    win = True

            Critter.move_critter(critter)
            Critter.draw(critter)

        # background!
        # Update with blit
        # change the pointer-type
        if mouse_type == 1:
            mouse_image = catch_mouse
            draw_pos = [mouse_pos[0] - catch_mouse.get_width() // 1.5, mouse_pos[1] - catch_mouse.get_height() // 1.2]
        else:
            mouse_image = kill_mouse
            draw_pos = mouse_pos

        if round_over:
            bg_music.stop()
            # Print the corresponding message to notify the user of the situation
            if not win:
                if mouse_type == 1:
                    sad_message = ["caught", "bee"]
                else:
                    sad_message = ["killed", "bird"]
                final_message = pygame.font.SysFont("timesnewroman", 70).render(
                    f"You {sad_message[0]} a {sad_message[1]} :(", True, "red")
            else:
                pygame.mixer.Sound.play(level_complete_sound, 1, 2)
                final_message = pygame.font.SysFont("timesnewroman", 70).render(f"You caught the birds and killed the bees!", True, "green")

            # Set a game reset
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                round_over = False
                if win:
                    count += 10
                else:
                    count = 10
                critters_list = make_critters_list(count, screen, ["wonk_parrot.png", "Angry_Bee.png"])
                bg_music.play()

            # print the final message to the screen
            screen.blit(final_message, [SCREEN_WIDTH // 2 - final_message.get_width() // 2, SCREEN_HEIGHT // 2 - final_message.get_height() // 2])

        screen.blit(mouse_image, draw_pos)
        # update the display

        pygame.display.flip()
        clock.tick(CLOCK_DELAY)


main()
