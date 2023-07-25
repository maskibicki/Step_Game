import random
number = random.randint(1, 100)
counter=3
while True:
	code="Bannana"
	user = "Michael"
	print("Welcome To The Game Selector! Please Sign In!")
	username = input("Enter Your Username. ")
	password = input("Enter Your Password. ")
	if password == code and username == user:
		counter=3
		game = input("What Game Do You Want? Calculator, Sigma Calculator, Or Guess The Number? Type Calc For Calculator, Sigma For Sigma Calculator And Guess For Guess The Number! ")
		if game == "calc":
			print("Calculator Launching...")
			num1 = int(input("Enter Your First Number. "))
			num2 = int(input("Enter Your Second Number. "))
			operation = input("Enter +,-,*, /, or ^. ")
			if operation == "+":
				print(num1 + num2)
			elif operation == "-":
				print(num1 - num2)
			elif operation == "*":
				print(num1 * num2)
			elif operation == "^":
				print(num1**num2)
			elif operation == "/":
				if(num2==0):
					print("Undefined")
				else:
					print(num1 / num2)
			else:
				print("Invalid Operator. Please Try Again.")
		elif game == "sigma":
			print("Sigma Calculator Launching...")
			n = int(input("Enter A Value For N. "))
			print((n*(n+1)/2))
		elif game == "guess":
			print("Guess The Number Launching...")
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
		else:
			print("Invalid Game")
	else:
		counter -= 1
		if counter == 0:
			print("Incorrect Too Many Times, Try Again Later")
			break
		elif counter == 1:
			print("Wrong Password Or Username. You Have ", +counter, " Try Left.")
		else:
			print("Wrong Password Or Username. You Have ", +counter, " Tries Left.")