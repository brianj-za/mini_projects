print("Welcome to my computer quiz.")

playing = input("Do you want to play my quiz? ")

if playing.lower().strip() != "yes":
    quit()

print("Okay! Let's play!")

score = 0
answer = input("What does CPU stand for? ")
if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower().strip() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower().strip() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower().strip() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions of 4 correct!")