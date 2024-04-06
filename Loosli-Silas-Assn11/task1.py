from utility import NAMES, HOMETOWNS, AGE_RANGE
from person import Person
from random import randint
from time import sleep

def main():
    print("Welcome to the Peopleinator")
    input("\tHit Enter to Begin")
    print()
    thinking("Creating People List")
    print()

    ##### Create and Display the People List #####
    people_list = create_people_list()

    print("People List")
    for i in people_list:
        print(i)
    print()

    ##### Create and Display the Hometown List #####
    input("Hit Enter to group by Hometown")
    thinking("\tProcessing")
    print()
    hometown_list = create_hometown_list(people_list)

    print("Hometown List")
    for i in hometown_list:
        print(i)
    print()

    ##### Create and Display the Age List #####
    input("Hit Enter to group by Age")
    thinking("\tProcessing")
    print()
    age_list = create_age_list(people_list)

    print("Age List")
    for i in age_list:
        print(i)
    print()

    ##### Display a Person object by entering an id. Use the original people_list #####
    print("Find a person by their id")
    while True:
        person_id = input("Enter an id from 0 to " + str(len(HOMETOWNS) * len(NAMES) - 1) + " (Enter without number to end): ")
        if person_id == "": # Stop when the user just hits enter
            break

        print(get_person_by_id(people_list, int(person_id)))
    print()

    ##### Thank You Message #####
    print("Thanks for using Peopleinator")

def create_people_list():
    return []

def create_hometown_list(people_list):
    return []

def create_age_list(people_list):


    return []

def get_person_by_id(people_list, person_id):
    return people_list["?"]["?"]

def thinking(msg):
    print(msg, end="")
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

main()