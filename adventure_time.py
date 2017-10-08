# import time
# from threading import Thread
# from threading import Timer
# import sys
# import select
from datetime import datetime


def adventure_game():
    hero = input("Enter your name hero: ")
    start_game = input(f"Are you ready {hero} (y/n): ").lower()

    def beginning():
        if start_game == "y":
            challenge_one()
        else:
            print("not working")


    def challenge_one():
        simple_riddle = input("What goes up must come...: ").lower()
        if simple_riddle == "down":
            challenge_two()
        else:
            print("You have lost 5 health")


    def challenge_two():

        print("Halt! You have stumbled into Zaras lair! Queen of the Southern Moon! Watch Out...")
        print("I am Zara! Queen of the Southern Moon, you have entered my Dojo and for that, you must be punished")
        dt1 = datetime.now()
        test = input("enter hi in the time given: ").lower()
        dt2 = datetime.now()
        difference = dt2 - dt1  # this is a timedelta

        if difference.seconds > 4:
            print("Nah your time has expired I'm out anyways.")
        elif test == "hey" or test == "hi":
            challenge_three()
        elif test == "Go away" or test == "Bye":
            print("Cya dude.")

    def challenge_three():
        print("You have now entered the Chimeras Chambers, prepare yourself")







    beginning()

adventure_game()
