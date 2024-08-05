import random
number = random.randint(1,14)
live = 4
a=0
#guess = int(input("What is your guess?"))
for i in range (live):
    a+=1
    guess = int(input(f"What is your {a}.8 guess?"))
    if guess == number:
        print("Congrulations")
    elif guess < number:
        print("Wrong, Bigger")
    elif guess > number:
        print("Wrong, Smaller")
    