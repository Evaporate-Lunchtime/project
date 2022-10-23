import sys
from graphics import Splash
from screen import Clear
class Menu:

    def __init__(self):
        
        while True:
            '''Menu'''
            decision = input("[Y] for Yes or [N] for no: ").lower()
            if decision == "y":
                break
            elif decision == "n":
                Clear.clear()
                Splash.owl("Aw! Too bad. I really wanted to play. Oh well. See you another time.")
                sys.exit()
            else:
                print("You must enter either [Y] or [N].")