print('''Are You Ready To challenge Computer In Rock,Paper,Scissors Game''')
import random

options = ["Rock", "Paper", "Scissors"]
while True:
    ready = input("would you like to play(Yes/No)? ")
    if ready == "Yes":
        user_choice = input("Enter a Choice(Rock,Paper,Scissors): ")
        comp_choice = random.choice(options)
        if user_choice == "Paper":
            if comp_choice == "Rock":
                print("Computer Choice is-", comp_choice)
                print(f"Paper covers Rock,You Win")
            elif comp_choice == "Scissors":
                print("Computer Choice is-", comp_choice)
                print("Scissors cuts Paper, You lose")
            else:
                print("Computer Choice is-", comp_choice)
                print("Tie")
        elif user_choice == "Rock":
            if comp_choice == "Paper":
                print("Computer Choice is-", comp_choice)
                print(f"Paper covers Rock,You lose")
            elif comp_choice == "Scissors":
                print("Computer Choice is-", comp_choice)
                print("Rock break Scissors, You Win")
            else:
                print("Computer Choice is-", comp_choice)
                print("Tie")
        elif user_choice == "Scissors":
            if comp_choice == "Rock":
                print("Computer Choice is-", comp_choice)
                print(f"Rock break Scissorsk,You lose")
            elif comp_choice == "Paper":
                print("Computer Choice is-", comp_choice)
                print("Scissors cuts Paper, You Win")
            else:
                print("Computer Choice is-", comp_choice)
                print("Tie")
    else:
        print("Thanks,For Playing Rock,Paper,Scissors Game")
        break
