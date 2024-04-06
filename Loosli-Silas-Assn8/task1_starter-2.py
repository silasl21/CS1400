# Silas Loosli
# CS1400 - MWF 9:30

import pattern

def main():
    # Setup target
    pattern.setup()

    # Play again loop
    play_again = True

    print("Welcome to Patterns!!!")
    print()

    while play_again:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("\t1) Rectangle")
        print("\t2) Circle")
        print("\t3) Super Pattern")
        mode = int(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle'
        if mode == 1:
            print("You chose Rectangle Pattern")
            #### Add Input Statement(s) as needed ####
            center_x = int(input("\tWhere would you like the center of the rectangle in the x direction to be: "))
            center_y = int(input("\tWhere would you like the center of the rectangle in the y direction to be: "))
            offset = int(input("\tWhat would you like the offset to be: "))
            height = int(input("\tWhat would you like the height of the rectangle to be: "))
            width = int(input("\tWhat would you like the width to be: "))
            count = int(input("\tHow many rectangles would you like in the pattern: "))
            rotation = int(input("\tWhat rotation would you like the rectangles to have: "))

            #### End Add Inputs Statement(s) ####

            # Draw a single rectangle pattern
            pattern.draw_rectangle_pattern(center_x, center_y, offset, height, width, count, rotation)

        # If they choose Circle
        elif mode == 2:
            print("You chose Circle Pattern")
            #### Add Input Statement(s) as needed ####
            center_x = int(input("\tWhere do you want the center of the circle in the x position: "))
            center_y = int(input("\tWhere do you want the center of the circle in the y position: "))
            offset = int(input("\tHow much offset do you want: "))
            radius = int(input("\tWhat do you want the radius of the circle to be: "))
            count = int(input("\tHow many circles do you want in the pattern: "))



            #### End Add Inputs Statement(s) ####

            # Draw a single circle pattern
            pattern.draw_circle_pattern(center_x, center_y, offset, radius, count)

        # If they choose super mode
        elif mode == 3:
            print("You chose Super Pattern")
            #### Add Input Statement(s) as needed ####
            num = (input("\tHow many patterns would you like: "))
            #### End Add Inputs Statement(s) ####

            # Draw super pattern
            if num == "":
                pattern.draw_super_pattern()
            else:
                pattern.draw_super_pattern(int(num))

        # Play again?
        print("Do you want to play again?")
        print("\t1) Yes, and keep drawings")
        print("\t2) Yes, and clear drawings")
        print("\t3) No, I am all done")
        response = int(input("Choose 1, 2, or 3: "))
        print()

        #### Add Statement(s) to clear drawings and play again ####
        if response == 1:
            continue
        if response == 2:
            pattern.reset()
            continue
        else:
            break

        #### End Add Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing! It's been real!")
    pattern.done()


main()
