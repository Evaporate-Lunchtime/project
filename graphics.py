import time
from screen import Clear

class Splash:
    '''Prints out a welcoming splash screen'''
    def splash():  
        
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        time.sleep(0.1)
        Clear.clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("██░███░███░▄▄▄███░██████░▄▄▀███░▄▄▄░███░▄▀▄░██░▄▄▄██")
        time.sleep(0.1)
        Clear.clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("██░███░███░▄▄▄███░██████░▄▄▀███░▄▄▄░███░▄▀▄░██░▄▄▄██")
        print("██░█░█░███░▄▄▄███░██████░██████░███░███░█░█░██░▄▄▄██")
        time.sleep(0.1)
        Clear.clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("██░███░███░▄▄▄███░██████░▄▄▀███░▄▄▄░███░▄▀▄░██░▄▄▄██")
        print("██░█░█░███░▄▄▄███░██████░██████░███░███░█░█░██░▄▄▄██")
        print("██▄▀▄▀▄███░▀▀▀███░▀▀░███░▀▀▄███░▀▀▀░███░███░██░▀▀▀██")
        time.sleep(0.1)
        Clear.clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("██░███░███░▄▄▄███░██████░▄▄▀███░▄▄▄░███░▄▀▄░██░▄▄▄██")
        print("██░█░█░███░▄▄▄███░██████░██████░███░███░█░█░██░▄▄▄██")
        print("██▄▀▄▀▄███░▀▀▀███░▀▀░███░▀▀▄███░▀▀▀░███░███░██░▀▀▀██")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        
        print(" /\ /\\")
        time.sleep(0.1)
        print("( O,O )")
        time.sleep(0.1)
        print("(     ) To Awesome Number Guessing Game    ")
        time.sleep(0.1)
        print("--\"--\"-------------------------------------")
        time.sleep(0.1)
        print("")
        
    
    def win():
        Splash.owl("✴.·´¯`·.·★  🎀𝓨𝓞𝓤 𝓦𝓞𝓝🎀  ★·.·`¯´·.✴")
        
    
    def owl(phrase):
        print(" /\ /\\")
        print("( O,O )")
        print(f"(     ) {phrase}    ")
        print("--\"--\"-----------------------------------------------------------------\n")
        
    
