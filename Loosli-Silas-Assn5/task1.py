# Silas Loosli
# CS1400 - MWF 9:30

print("Hello and welcome to the Fronkian Calendar Leap Year Calculator!")
print("This is the brain child of Silas Loosli because of a certain CS class.")

# Get the year from the user
year = int(input("\tEnter a 4 digit year to test if it is a leap year in the Fronkian Calendar: "))


# Make sure the user inputs a correct value
while year < 1000 or year > 9999:
    print("That is not a four digit year")
    year = int(input("\tEnter a four digit year: "))

# Inserting a blank line so I don't forget for user experience
print()

# Calculate the values of the first 2 numbers as well as the second and third numbers
first_2_digits = year // 100
third_digit = (year - first_2_digits * 100) // 10
fourth_digit = (year - first_2_digits * 100) - third_digit * 10


# Set conditions for cases
case_1 = (year % 9 == 0) and third_digit != fourth_digit
case_2 = first_2_digits == third_digit + fourth_digit and third_digit % 2 == 0 and third_digit < fourth_digit

# Print out a final message
if case_1 or case_2:
    print(f"Thank you for using the Fronkian Calendar Leap Year Calculator.\n\tThe year you selected, {year}, is a leap year! Happy leap year!")
else:
    print(f"Thank you for using the Fronkian Calendar Leap Year Calculator.\n\tThe year you selected, {year}, is not a leap year. Womp Womp.")
