import random

def user_choice():
    choice1 = input("Enter R for rock, S for scissors, P for paper: ").upper()
    match choice1:
        case "R":
            choice1 = "rock"
        case "S":
            choice1 = "scissors"
        case "P":
            choice1 = "paper"
    return choice1

options = ["rock", "scissors", "paper"]

def main():
    computer_choice = random.choice(options)
    user = user_choice()
    if computer_choice == user:
        print("Draw!")
    elif (computer_choice == "rock" and user == "scissors") or (computer_choice == "paper" and user == "rock") or (computer_choice == "scissors" and user == "paper"):
        print("Computer chosen: " + computer_choice)
        print("You lose!")
    else:
        print("Computer chosen: " + computer_choice)
        print("You win!")

while True:
    trigger = input("Do you want to continue? [Y/N]?").upper()
    if trigger == "Y":
        main()
    else:
        break
