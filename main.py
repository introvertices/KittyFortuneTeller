from os import name, system
from time import sleep
from random import randint
import ascii_art as art

def main():
    ### SET UP
    clear()

    # Prompt the user for a question
    get_input()

    # Animate curtains and cat
    for i in range(1,len(art.curtains)):
        clear()
        print(art.curtains[i][0])     
        sleep(art.curtains[i][1])

    # Show last frame of animation and print answer
    clear()
    answer = randint(0,len(art.answers)-1)
    print(art.answers[answer][0])

    # Prompt for another question
    redo = input("\033[1;32;40mWould you like to ask another question? Y/N\n \033[1;37;40m> ")
    if str(redo[0].upper()) == "Y":
        main()
    else:
        clear()
        print(input("Goodbye!"))







def get_input():

    # Print closed curtains
    clear()
    print(art.curtains[0][0])

    # Ask user for their question, this doesn't need to be stored
    input("\033[1;32;40mWelcome! What is it your heart desires to know?\n \033[1;37;40m> ")


#!-- HELPERS
# Clears the screen
def clear():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)


if __name__ == "__main__":
    main()