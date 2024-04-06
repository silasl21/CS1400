# Silas Loosli
# CS1400 - MWF 9:30
from time import sleep
import random


class Animal:
    pass


animal_1 = Animal()
animal_2 = Animal()
animal_3 = Animal()
animal_list = []

"""animal_1.type = "platypus"
animal_1.number = 10
animal_1.sound = "grgr"
animal_list.append(animal_1)
animal_2.type = "bear"
animal_2.number = 5
animal_2.sound = "roar"
animal_list.append(animal_2)
animal_3.type = "eagle"
animal_3.number = 20
animal_3.sound = "caw"
animal_list.append(animal_3)
name = "Silas"""

# Welcome the user to the program
print("Welcome my young pupil to the lab of wonders and inators!\nWould you like to hear about my latest inator?")
# ask if the user would like to see the latest inator
user_input = input("\t(Y/N): ")
if user_input == "Y" or user_input == "y":
    sleep(0.5)
    print("Sweet, it is just over here! Follow me!")
else:
    sleep(1)
    print("Ok fine, looks like I have a tough crowd. I'll show it to you either way. Follow me.")
print()
sleep(0.5)
print("Oh what was your name again, pupil?")
name = input("\tEnter your name: ")
sleep(0.5)
print(f"\nWow, {name}! That is a very lovely name!")
sleep(1)
# Show off the machine and tell the user what it does and how to use it
print("\n**Dr Doofenlittle whips a sheet off of a glass cylinder with electronics whirring**")
sleep(1)
print("\nIt is called the animal-combine-inator, and it is my latest creation!")
sleep(0.5)
print("The way it works is you think of 3 different animals you have seen recently, the amount, and what they say.")
sleep(2)
print("\nOk let's test it out: \nCould you give me an animal, the number you saw, and what sound it makes?")

# Start collecting input for the animals

animal_1.type = input("\tEnter an animal: ")
animal_1.number = int(input(f"\tEnter the number of {animal_1.type}s you saw: "))
animal_1.sound = input("\tEnter the sound it makes: ")
animal_list.append(animal_1)
sleep(1)
# 2nd animal
print("Ok, now for the second animal")
sleep(0.5)
animal_2.type = input("\tEnter an animal: ")
animal_2.number = int(input(f"\tEnter the number of {animal_2.type}s you saw: "))
animal_2.sound = input("\tEnter the sound it makes: ")
animal_list.append(animal_2)
# 3rd animal
sleep(1)
print("And finally, the third animal")
sleep(0.5)
animal_3.type = input("\tEnter an animal: ")
animal_3.number = int(input(f"\tEnter the number of {animal_3.type}s you saw: "))
animal_3.sound = input("\tEnter the sound it makes: ")
animal_list.append(animal_3)

# Print a funny message if the animal is a platypus
if animal_1.type == "platypus" or animal_2.type == "platypus" or animal_3.type == "platypus":
    print("\nHuh, I knew a platypus once, I didn't like him very much...\n")

# Start the machine and explain what it is doing
print(f"Thank you, {name}.\nNow we can get this machine started.")
input("Press enter to start the machine. ")
sleep(1)
print("\n**Machine powers up, starts whirring**")
print(f"{name} starts hearing", str(animal_1.sound) + "s, " + str(animal_2.sound) +
      "s, and " + str(animal_3.sound) + "s")
# machine starts talking
sleep(1)
print("\n\t~~STARTING ANIMAL-COMBINE-PROCESS~~")
print("\nNow we see what you put in!")
sleep(2)
print("\n\t~~USER INPUT~~")
sleep(.5)
print(f"\t~~TOTAL NUMBER OF ANIMALS SEEN: {animal_list[0].number + animal_list[1].number + animal_list[2].number}~~")
sleep(.5)
print(f"\t~~TYPES OF ANIMALS SEEN: {animal_list[0].type.upper()}S, {animal_list[1].type.upper()}S, {animal_list[2].type.upper()}S~~")
sleep(1)
print(f"\t~~{animal_list[0].type.upper()}S SAID {animal_list[0].sound.upper()}~~")
sleep(1)
print(f"\t~~{animal_list[1].type.upper()}S SAID {animal_list[1].sound.upper()}~~")
sleep(1)
print(f"\t~~{animal_list[2].type.upper()}S SAID {animal_list[2].sound.upper()}~~")
sleep(2)

# Show that the Animal-Combine-Inator finished its work
print("\nAh it looks like the Animal-Combine-Inator has finished!")
print("\n\t~~PLEASE PRESS ENTER TO VIEW FINAL FORM~~")
input()

# Scramble the letters in the names and the sounds as well as get the average number of animals
rand_type = list(animal_list[0].type + animal_list[1].type + animal_list[2].type)
random.shuffle(rand_type)
rand_type = "".join(rand_type)

rand_sound = list(animal_list[0].sound + animal_list[1].sound + animal_list[2].sound)
random.shuffle(rand_sound)
rand_sound = "".join(rand_sound)

avg_num = (animal_list[0].number + animal_list[1].number + animal_list[2].number) // 3

# Start a processing timer for kicks and giggles
for i in range(5):
    print(".")
    sleep(1.5)

# Print the final form through the computer and then have the doctor comment on it
print(f"\n\t~~CONGRATULATIONS ON CREATING {avg_num} NEW {rand_type}S THAT ALL SAY {rand_sound}~~".upper())
sleep(2)
print(f"Wow, that is some cool animal, a {rand_type}... I couldn't have hoped it would work out better myself.")

# Give a perry the platypus Easter Egg
if animal_1.type == "platypus" or animal_2.type == "platypus" or animal_3.type == "platypus":
    sleep(5)
    print("\n\t~~ERROR~~")
    print("What's wrong??")
    sleep(2)
    print("NO!")
    sleep(1)
    print("It can't be!")
    sleep(2)
    print(f"\nPerry the {rand_type}!!")
    sleep(2)
    print("\n\t~~SIMULATION TERMINATED~~")
