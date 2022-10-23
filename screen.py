import os

class Clear:
    '''Class to manage terminal commands'''
    def clear():
        '''This function clears the terminal window'''
        os.system('cls' if os.name == 'nt' else 'clear')