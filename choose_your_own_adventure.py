name = input("Type your name: ")

print(f"Welcome {name} to your adventure.")

answer = input("You are on a dirt road. It has come to an end. You can go left or right. Which way would you like to "
               "go? ").lower().strip()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type walk or swim. ")

    if answer == "swim":
        print("You swam across and was eaten by a crocodile. You lose.")
        quit()
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lose.")
        quit()
elif answer == "right":
    answer = input("You come to a bridge. It looks rickety. Do you want to cross it, or move back? ")
    if answer == "back":
        print("You get lost and lose.")
        quit()
    elif answer == "cross":
        print("You reach the castle and win!")
        quit()
    pass
else:
    print("Not a valid answer. You lose.")
    quit()

