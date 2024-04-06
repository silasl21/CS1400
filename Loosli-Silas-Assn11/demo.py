from utility import NAMES, HOMETOWNS, AGE_RANGE
from time import sleep

def main():
    print(NAMES)
    thinking("Just a second")
    print(HOMETOWNS)
    thinking("Sorry, hold on")
    print(AGE_RANGE)
    thinking("All done")


def thinking(msg):
    print(msg, end="")
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

main()