# The main program
# Just a couple of imports
import sys
import time


# Asks for name 
name = input("What is your name? ")

# Welcome the user to the program and ask if they would like to play the quiz
print(f"Welcome to the ultimate gaming quiz {name}!")
print("Would you like to play a game? ")
print("Enter no to quit")
playing = input("> ")

if playing.lower() != "yes":
    quit()


# This is a loop that the quiz runs in
while True:
    print("\nIT'S ON LIKE DONKEY KONG!")
    time.sleep(1)
    score = 0


    QUESTION = input("In Minecraft, what material is commonly used to create torches? \na) Iron \nb) Gold \nc) Coal \nd) Diamond\n> ")

    if QUESTION.upper() == "C":
        print("\nCORRECT! \nNext Question")
        score += 1
        time.sleep(1)

        
    if QUESTION.upper() != "C":
        print("\nARE YOU EVEN A REAL GAMER?? ")
        score += 1


    QUESTION = input("Who of the following are shield operators? \na) Monty \nb) Caveria \nc) Recruit \nd) Rook \n>  ")

    if QUESTION.upper() == "D":
        print("\nYOU ARE QUITE A GENIUS HEY?")
        score += 1
        time.sleep(1)
    
    if QUESTION.upper() != "D":
        print("\nNOPE, GO PLAY SOME MORE SEIGE MATE!")
        time.sleep(1)
    
    QUESTION = input("\nWhat item is required to summon the Eye of Cthulhu in Terraria? \na) Demonite Ore \nb) Suspicious Looking Eye \nc) Moon Charm \nd) Shadow Scale \n> ")
    
    if QUESTION.capitalize() == "B":
        print("\nGOOD JOB! YOU KNOW YOUR STUFF")
        score += 1
        time.sleep(1)
    
    if QUESTION.capitalize() != "B":
        print("\nHEY GO PLAY SOME TERRARIA AND THEN COME BACK AND GET THIS RIGHT!")
        time.sleep(1)

    
    QUESTION = input("\nWhich character in Overwatch wields a rocket launcher and a jetpack? \na) Tracer \nb) Soldier: 76 \nc) Pharah \nd) Mei \n> ")
    
    if QUESTION.capitalize() == "C":
        print("\nHEY! IT'S SOMEONE ELSE WHO HAS PLAYED OVERWATCH!")
        score += 1
        time.sleep(1)
    
    if QUESTION.capitalize() != "C":
        print("\nI'M HIGHLY DOUBTING YOUR GAMING KNOWLEDGE RIGHT NOW HERE DUDE!")
        time.sleep(1)

    QUESTION = input("\nIn Fallout 4, what is the name of the robotic companion created by the Institute? \na) Curie \nb) Codsworth \nc) Dogmeat \nd) Strong \n> ")
    
    if QUESTION.capitalize() == "B":
        print("\nNICE YOU'VE PLAYED FALLOUT BEFORE!")
        score += 1
        time.sleep(1)
    
    if QUESTION.capitalize() != "B":
        print("\nOH COME ON, YOU DON'T LIKE POST NUCLEAR GAMES?!")
        time.sleep(1)
    
    total_percent = (score / 100) * 100

    print(f"You scored: {total_percent} on this quiz!")
    again = input("Would you like to play again? ")
    
    if again == "yes":
        pass
    else:
        sys.exit(1)
