from graphics import Splash
from player import Player
from random import randint
from screen import Clear
from menu import Menu
import os
import sys

def main():
    '''This is the main class of the game'''
    
    # This will print out a splash screen before starting the game.
    Clear.clear()
    Splash.splash()

    while True:
        '''This is the main game loop'''

        player = Player()
        player.name = input("Enter your name: ").lower()
        Clear.clear()
        
        Splash.owl(f"Hello {player.name.title()}!")
        print("I would like to play a guessing game with you. Wanna play?")
        Menu()
        Clear.clear()
        Splash.owl("I'm thinking of a number between 0 and 99.")
        print("Try to guess what number I'm thinking of. You have 10 guesses. Let's go!")
        number = randint(0, 99)
        
        guessesLeft = 10
        # print(number) For testing
        for i in range(guessesLeft):
            
            guess = ""
            while True:
                try:
                    guess = int(input("\nWhat's your guess? "))
                    break
                except:
                    Clear.clear()
                    Splash.owl("Oops! You have to use whole numbers!")
            Clear.clear()
            guessesLeft -= 1
            if guess == number:
                Splash.win()
                sys.exit()
            elif guessesLeft > 0:
                Splash.owl(f"Try again. You have {guessesLeft} guesses left.")
            else:
                Splash.owl("(つ◉益◉)つ yOU LOSe 💣🌟")
                sys.exit()
        
        
        
    

if __name__ == "__main__":
    main()