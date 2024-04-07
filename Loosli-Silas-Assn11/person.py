from utility import NAMES, HOMETOWNS

class Person:
    def __init__(self, id, age):
        self.__id = id
        # Unique id ranging from 0 to the (len(NAMES) * len(HOMETOWNS)) - 1
        self.__age = age
        # this should be a random value from the range of values defined by AGE_RANGE


    def get_name(self):
        name = NAMES[self.__id - 1]
        return name

    def get_hometown(self):
        hometown = HOMETOWNS[self.__id]
        return hometown

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__id

    # Defines what gets printed out if the object is in a list
    def __repr__(self):
        return self.get_name() + " " + self.get_hometown() + " " + str(self.get_age())

    # Defines what gets printed out if you print out an object
    def __str__(self):
        return self.get_name() + " is from " + self.get_hometown() + " and is " + str(self.get_age()) + " years old."
