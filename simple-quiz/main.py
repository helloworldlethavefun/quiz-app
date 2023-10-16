# This is the really simple quiz

# Imports
import os
import platform
import sys
import time
from colorama import Fore

# Variables

is_sure = ""
is_running = False
score = 0
name = ""
quiz_answers = {"1": "c", 
                "2": "b", 
                "3": "b", 
                "4": "c", 
                "5": "b", 
                "6": "a", 
                "7": "b", 
                "8": "a"}

# Functions

def clear():
    user_os = platform.system()
    if user_os == "Darwin" or "Linux":
        os.system("clear")
    elif user_os == "Windows":
        os.system("cls")

def quiz(is_running):
    if is_running == True:
        while is_running:
            print("Let the quiz begin!")
            clear()
            print("Question 1. In Minecraft, what material is commonly used to create torches?")
            print("a) Iron \nb) Gold \nc) Coal \nd) Diamond")
            answer = input("> ")
            if answer.lower() == quiz_answers["1"]:
                score =+ 1
                print(Fore.GREEN + "Correct! The recipe is 1 coal above a stick in the crafting grid")
                time.sleep(1)
            else:
                print(Fore.RED + "Incorrect! The correct answer is c) Coal")
                time.sleep(1)
            clear()
            print(Fore.WHITE + "Next Question")
            time.sleep(1)
            print("Which of the following characters are shield operators in seige? ")
            print("a) Monty \nb) Caveria \nc) Recruit \nd) Rook")
            answer = input("> ")
            if answer.lower() == quiz_answers["2"]:
                print()

    else:
        sys.exit(1)


def main():
    # The main code

    name = input("What is your name? ")

    clear()

    print("------------------------------------------------------------------")
    print(f"        Welcome to the ultimate gaming quiz {name}     ")
    print("------------------------------------------------------------------")

    ready = input(f"So {name}, are you ready for the ultimate gaming quiz? ")

    if ready.lower().strip() == "yes":
        print("Sweet, so what are we wating for!")
        is_running = True
        quiz(is_running)
    elif ready.lower().strip() == "no":
        is_sure = input("Are you sure? ")
        if is_sure.lower().strip() == "yes":
            sys.exit(1)
        elif is_sure.lower().strip() == "no":
            print("Too bad throwing you into it? ")
            is_running = True
            quiz(is_running)

            
    else:
        print("Sorry that is not a valid answer! Please rerun the program")
        sys.exit(1)

if __name__ == "__main__":
    main()