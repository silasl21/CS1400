# Silas Loosli
# CS1400 - MWF 9:30

def make_number_pyramid(num_rows):  # Create a formal parameter for the number of rows from the caller of the function
    msg = ""  # Create a string variable that will be returned

    # find out how many digits are in the number of rows
    max_digits = len(str(num_rows))

    # adjust for the spaces in between numbers
    number_width = max_digits + 1

    # create a loop from zero to the number of rows
    for i in range(1, num_rows + 1):
        # create a string variable for the new row of text
        new_row = ""
        new_row += " " * (num_rows - i)

        # create a loop from 0 to the current row number
        for j in range(i):
            # create a conditional to add spacs dynamically based off of the max digits
            if j > 0:
                new_row += " "
                extra_spaces = " " * (max_digits - len(str(i)))
                new_row += extra_spaces

            # add the row number to the  row string
            new_row += f"{i}"
            # add the new row to the main string and add a new line
        msg += new_row + "\n"

    return msg


def main():
    num_rows = int(input("Enter how many rows you would like to print: "))
    final_message = make_number_pyramid(num_rows)
    print(final_message)


main()
