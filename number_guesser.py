import random

while True:
    top = input("What would you like the maximum number to be? ")
    if not top.isdigit():
        print("Please enter a number.")
        continue
    if int(top) < 1:
        print("Please enter a value greater than 0.")
        continue
    break

top = int(top)
r = random.randint(0, top)

guessed = False
print("You have 5 guesses to get this right. Good luck!")
for _ in range(5):
    user_guess = input("Make a guess: ")
    if not user_guess.isdigit():
        print("Please enter a number.")
        continue

    user_guess = int(user_guess)
    if user_guess < 0:
        print("Please enter a number greater than 0.")
        continue
    if user_guess == r:
        print("Well done! You guessed right!")
        guessed = True
        break
    elif user_guess < r:
        print("Your number is lower, try again.")
        continue
    elif user_guess > r:
        print("Your number is higher, try again.")
        continue

if guessed:
    print("Congrats! You guessed the number!")
else:
    print(f"You didn't guess the number. It was {r}")