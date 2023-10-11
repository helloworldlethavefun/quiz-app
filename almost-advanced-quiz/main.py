# This is the simple version of the quiz. It's a basic cli with a little bit of file/db handling

# All of the imports
#import cs50
import platform
import os
import sys

# Variables
# This function defines some global variables for the program to use

def varis():
    global score
    global name
    global questions_used
    global user_os
    score = 0
    name = ""
    questions_used = []
    user_os = ""

# Functions

# This is just a quick function to clear the users screen
def clear():
    user_os = platform.system()
    if user_os == "Darwin" or "Linux":
        os.system("clear")
    elif user_os == "Windows":
        os.system("cls")
    else:
        print("Sorry there was an error trying to clear your screen")
        sys.exit(2)

# The "Intro" to the the program
def start():
    clear()
    
    name = input("What is your name? ")

    clear()

    print("------------------------------------------------------")
    print("     Wecome to the ultimate gaming quiz", name, "     ")
    print("------------------------------------------------------")

# This creates the connection to the sql-lite db
def setup_sql_conn():
    pass

# This pulls the question from the sql db
def fetch_question():
    pass

# Main function

def main():
    start()

if __name__ == "__main__":
    varis()
    main()