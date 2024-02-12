from questions import *

def print_header(filename):
    with open(filename, 'r') as file:
        print(file.read())

def exit_message():
    print("STRAY KIDS EVERYWHERE ALL AROUND THE WORLD,\nYOU MAKE STRAY KIDS STAY\n")
    print("(==Terminal app by sdikyarts. Not affiliated with JYP Ent.==)")

def main():
    print()
    print_header("textfiles/skz_logo.txt")
    print()
    
    while True:
        print("Wanna know which STRAY KIDS member are you?")
        quiz_start = input("Type Y to start, type N to quit: ")
        print()

        if quiz_start.lower() == "y":
            quiz_session = ask_questions()
            print(quiz_session)
            print()
            print()
            replay = input("Do you want to play again? (Y/N): ")
            if replay.lower() != "y":
                exit_message()
                break
        elif quiz_start.lower() == "n":
            exit_message()
            break
        else:
            print("Invalid input, please type only *y* or *n*")

main()