# Silas Loosli
# CS1400 - MWF 9:30
from random import randint
import time

# Generate a random number
rand_num = randint(0, 10)

# Give the user a welcome message
print("Welcome new user!!!")
print("This is a test to see how true of an aggie you are: ")
input("Press enter if you wish to find your worth in the eyes of Big Blue")
print()
# Explain what the program is
print("Big Blue has selected an integer value (not decimal) from 0 to 10 (inclusive).")
print("Guess this numer to find out if you are truly an aggie.")

# get the user to guess what it is
print("So what is your guess, aggie?")
user_guess = int(input(":: "))

# Create a variable to determine how many guesses it took
num_guesses = 1

# print a good job first try message
if user_guess == rand_num:
    print("Exact match: Honored to play with you, True Aggie.")
    print("You must be the truest aggie that I have ever seen, you did that in the first try!")

# create a guessing loop

while True:
    print()
    if (user_guess == rand_num) and (num_guesses == 1):
        break

# if they're one off
    if (user_guess == rand_num + 1) or (user_guess == rand_num - 1):
        print("Off by 1: You are a worthy opponent, Big Blue.")

# If they're 2 off
    elif (user_guess == rand_num + 2) or (user_guess == rand_num - 2):
        print("Off by 2: You have much to learn, Hurd.")

# off by 3
    elif user_guess == rand_num + 3 or user_guess == rand_num - 3:
        print("Off by 3: Little Blue, your time will come")

# if they are off by more than 3
    elif user_guess != rand_num:
        print("Off by 3+: Keep working hard on the Quad.")
    else:
        print("Exact match: Honored to play with you, True Aggie.")
        break
# Add a number to the guess count
    num_guesses += 1

# Make the user retry if they got it wrong
    print("Try again, maybe you will still yet be a true aggie!")
    time.sleep(1.5)
    print()
    user_guess = int(input("What is your next guess, aggie? : "))

print()
if num_guesses > 3:
    print(f"Actually I might have to revoke that \"True Aggie\" badge, it took you {num_guesses} tries to get it right")

elif num_guesses > 1:
    print(f"Good job Aggie, it only took you {num_guesses} tries to get it right!")
