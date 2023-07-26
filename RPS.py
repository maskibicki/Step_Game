import random
number = random.randint(1, 3)
while True:
    print("Enter Your Choice:")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    choice = int(input("Your Choice (1/2/3): "))
    if choice == 1 and number == 2:
        print("Player Chooses Rock")
        print("Computer Chooses Paper")
        print("Computer Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 2 and number == 3:
        print("Player Chooses Paper")
        print("Computer Chooses Scissors")
        print("Computer Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 3 and number == 1:
        print("Player Chooses Scissors")
        print("Computer Chooses Rock")
        print("Computer Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 1 and number == 3:
        print("Player Chooses Rock")
        print("Computer Chooses Scissors")
        print("Player Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 2 and number == 1:
        print("Player Chooses Paper")
        print("Computer Chooses Rock")
        print("Player Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 3 and number == 2:
        print("Player Chooses Scissors")
        print("Computer Chooses Paper")
        print("Player Wins!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 3 and number == 3:
        print("Player Chooses Scissors")
        print("Computer Chooses Scissors")
        print("Tie!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 2 and number == 2:
        print("Player Chooses Paper")
        print("Computer Chooses Paper")
        print("Tie!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    elif choice == 1 and number == 1:
        print("Player Chooses Rock")
        print("Computer Chooses Rock")
        print("Tie!")
        again = input("Would You Like To Play Again? (y/n) ")
        if again == "y" or again == "Y":
            print("Restarting...")
            number = random.randint(1, 3)
        else:
            break
    else:
        print("Error")
        break