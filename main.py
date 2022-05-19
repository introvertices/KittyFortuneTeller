from os import name, system
from time import sleep
from random import choice
import ascii_art as art

def main():
    ### SET UP
    answers = ["no"]
    clear()

    # Prompt the user for a question
    get_input()

    # Animate curtains and cat
    cat_animation(art.curtains)

    # Show last frame of animation and print answer
    clear()
    print(art.curtains[-1])
    print(choice(answers))

    # Prompt for another question
    redo = input("Would you like to ask another question? Y/N\n > ")
    if str(redo[0].upper()) == "Y":
        main()
    else:
        clear()
        print(input("Goodbye!"))







def get_input():
    thanks_responses = ["Hmm, let's see...","I wonder what the fates hold for you?","As you wish..."]

    # Print closed curtains
    clear()
    print(art.curtains[0])

    # Ask user for their question, this doesn't need to be stored
    input("Welcome! What is it your heart desires to know?\n > ")

    # clear screen, then thank user

    print(art.curtains[0])
    print(f"{choice(thanks_responses)}")


def cat_animation(ascii_art):
    ### Setup #########################################################################################
    clear()
    
    # How many times the screen should clear per second. Lower = slower
    framerate = 12                 

    # Loop to animate the artwork
    for i in ascii_art:
        print(i)     
        sleep(1/framerate)
        clear()

#!-- HELPERS
# Clears the screen for ~aesthetics~
def clear():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)


if __name__ == "__main__":
    main()