# Silas Loosli
# CS1400 - MWF 9:30

# Add Import Statement(s) as needed
from chessboard import draw_chessboard
# End Add Import Statement(s)


def main():

    # Add Code to get input from user
    print("\nHello and welcome to the chessboard, just a few questions before we get started:")
    start_x = int(input("\tEnter the starting x-position: "))
    start_y = int(input("\tEnter the starting y-position: "))
    width = input("\tEnter a width for the chessboard: ")
    height = input("\tEnter a height for the chessboard: ")
    # End Add Code to get input from user

    if width == "" and height == "":
        draw_chessboard(start_x, start_y)
    elif height == "":
        draw_chessboard(start_x, start_y, width=int(width))
    elif width == "":
        draw_chessboard(start_x, start_y, height=int(height))
    else:
        draw_chessboard(start_x, start_y, int(width), int(height))


main()
