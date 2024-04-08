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


# Creates a list of people with unique IDS and randomly assigned ages
def create_people_list():
    people_list = []
    identifier = 0
    for i in range(len(NAMES)):
        people_list.append([])
        for j in range(len(HOMETOWNS)):
            people_list[i].append(Person(identifier, randint(AGE_RANGE[0], AGE_RANGE[1])))
            identifier += 1
    return people_list


# groups people by their hometowns and creates a list for each hometown
def create_hometown_list(people_list):
    hometown_list = [[] for i in range(len(HOMETOWNS))]

    for i in range(len(NAMES) * len(HOMETOWNS)):
        upper_list_search_id = i // len(HOMETOWNS)
        inner_list_search_id = i % len(HOMETOWNS)
        person = people_list[upper_list_search_id][inner_list_search_id]
        hometown = person.get_hometown()
        hometown_list[HOMETOWNS.index(hometown)].append(person)
    # basically, we have a list that starts at 0 and goes to whatever. The list will go through every value, then figure
    # out if it is part of a certain hometown. This should be every time it goes through the hometown list once.
    # for every hometown, there should be the length of names in that list.

    return hometown_list


# groups people by their ages and creates a list for each age group
def create_age_list(people_list):
    age_list = [[] for i in range(AGE_RANGE[1] - AGE_RANGE[0] + 1)]
    for sublist in people_list:
        for person in sublist:
            age = person.get_age()
            age_list[age - AGE_RANGE[0]].append(person)
    return age_list


# This is my inital attempt at getting someone based off of their id, worked for 1 list mostly, but not the other so time to retry
# retrieves a person from the list based on their ID
# def get_person_by_id(people_list, person_id):
#     total_people = len(NAMES) * len(HOMETOWNS)
#     if person_id < 0 or person_id >= total_people:
#         return None
#     else:
#         upper_list_search_id = person_id // len(NAMES)
#         inner_list_search_id = person_id % len(HOMETOWNS)
#         print(f"DEBUGGING: upper list search id  is {upper_list_search_id}, lower is {inner_list_search_id}")
#         return people_list[upper_list_search_id][inner_list_search_id]

# this was my second attempt, it seems to work. Hopefully it works for the rest of the lists you guys have
def get_person_by_id(people_list, person_id):
    total_people = len(NAMES) * len(HOMETOWNS)
    if person_id < 0 or person_id >= total_people:
        return None
    count = 0
    for sublist in people_list:
        for person in sublist:
            if count == person_id:
                return person
            count += 1
    return None  # Return None if person_id is not found

def thinking(msg):
    print(msg, end="")
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


main()
