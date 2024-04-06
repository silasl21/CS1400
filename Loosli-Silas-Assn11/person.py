from utility import NAMES, HOMETOWNS

class Person:
    def __init__(self, id, age):
        pass


    def get_name(self):
        return "Name"

    def get_hometown(self):
        return "Hometown"

    def get_age(self):
        return "Age"

    def get_id(self):
        return "Id"

    # Defines what gets printed out if the object is in a list
    def __repr__(self):
        return self.get_name() + " " + self.get_hometown() + " " + str(self.get_age())

    # Defines what gets printed out if you print out an object
    def __str__(self):
        return self.get_name() + " is from " + self.get_hometown() + " and is " + str(self.get_age()) + " years old."
