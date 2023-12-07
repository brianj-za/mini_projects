import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors, or q to quit: ").lower().strip()
    if user_input == "q":
        break
    elif user_input not in options:
        print("Please enter either rock, paper, or scissors.")
        continue

    # Play the game
    computer_choice = random.randint(0, 2)
    print(f"Computer picked {options[computer_choice]}.")

    if user_input == "rock" and options[computer_choice] == "scissors":
        print("Player wins!")
        user_wins += 1
    elif user_input == "paper" and options[computer_choice] == "rock":
        print("Player wins!")
        user_wins += 1
    elif user_input == "scissors" and options[computer_choice] == "paper":
        print("Player wins!")
        user_wins += 1
    elif user_input == options[computer_choice]:
        print("It's a draw!")
        continue
    else:
        print("Computer wins!")
        computer_wins += 1

print(f"Player score is {user_wins}, computer score is {computer_wins}.")
print("Goodbye!")