import random
number = random.randint(1, 100)
guesses = 0
name = str(input("Enter Your Name Here: "))
while True:
    guess = int(input("Enter Your Guess: "))
    if guess < 1:
        print("That Is Not A Valid Guess")
    elif guess > 100:
        print("That Is Not A Valid Guess")
    elif number > guess:
        print("Higher")
        guesses +=1
    elif number < guess:
        print("Lower")
        guesses +=1
    elif number == guess:
        print("Congrats " +name+ "! You Took ", +guesses, " Guesses To Get The Number!")
        break
    else:
        print("That Is Not A Valid Guess")