# Silas Loosli
# CS1400 - MWF 9:30
import math
from math import tan, pi

input("Welcome to the Polygon Calculator! Press enter to get started! ")
print()
# - Create a blank list for number of sides and length
lengths = []
num_sides = []


# - Enter the length and number of sides for polygon 1
num_sides.append(int(input("Enter the number of sides for polygon 1: ")))
lengths.append(float(input("Enter the length of each side for polygon 1: ")))

# - Enter the length and number of sides for polygon 2
num_sides.append(int(input("Enter the number of sides for polygon 2: ")))
lengths.append(float(input("Enter the length of each side for polygon 2: ")))

# - Enter the length and number of sides for polygon 3
num_sides.append(int(input("Enter the number of sides for polygon 3: ")))
lengths.append(float(input("Enter the length of each side for polygon 3: ")))

# - Enter the length and number of sides for polygon 4
num_sides.append(int(input("Enter the number of sides for polygon 4: ")))
lengths.append(float(input("Enter the length of each side for polygon 4: ")))

# - Calculate the area of each polygon

polygon_1_area = round((num_sides[0] * math.pow(lengths[0], 2) / (4 * tan(pi / num_sides[0]))), 5)

polygon_2_area = round((num_sides[1] * math.pow(lengths[1], 2) / (4 * tan(pi / num_sides[1]))), 5)

polygon_3_area = round((num_sides[2] * math.pow(lengths[2], 2) / (4 * tan(pi / num_sides[2]))), 5)

polygon_4_area = round((num_sides[3] * math.pow(lengths[3], 2) / (4 * tan(pi / num_sides[3]))), 5)


# - Tell the user what the area of each polygon is
print("The area of polygon 1 is", polygon_1_area)
print()
print("The area of polygon 2 is", polygon_2_area)
print()
print("The area of polygon 3 is", polygon_3_area)
print()
print("The area of polygon 4 is", polygon_4_area)
print()
print()
# - Thank the user for using the program:
print("Thank you for using Polygon Calculator (TM) by Silas Loosli. If you would like to contact customer support for this program, please don't.")