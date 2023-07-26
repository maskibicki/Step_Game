import random
number = random.randint(1, 100)
counter=3
while True:
	code="Bannana"
	user = "Michael"
	inup = input("Welcome To The Game Selector! Please Sign In or Sign Up!")
	if inup == "Sign In" or inup == "Sign in" or inup == "sign in" or inup == "sign In":
		username = input("Enter Your Username. ")
		password = input("Enter Your Password. ")
		if password == code and username == user:
			counter=3
			game = input("What Game Do You Want? Calculator, Sigma Calculator, Or Guess The Number?\nType Calc For Calculator, Sigma For Sigma Calculator, And Guess For Guess The Number! ")
			if game == "calc" or game == "Calc":
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
			elif game == "sigma" or game == "Sigma":
				print("Sigma Calculator Launching...")
				n = int(input("Enter A Value For N. "))
				print((n*(n+1)/2))
			elif game == "guess" or game == "Guess":
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
	elif inup == "Sign Up" or inup == "Sign up" or inup == "sign up" or inup == "sign Up":
		name = input("Enter Your Username. ")
		confirm = input("Your Name Is " +str(name)+ "? Yes Or No? ")
		if confirm == "Yes" or confirm =="yes":
			password = input("Please Enter Your Password. ")
			same = input("Please Confirm Your Password. ")
			if password == same:
				print("Your Username and Password have Been Saved!")
				break
			else:
				print("Your Passwords Do Not Match. Please Restart.")
				break
		elif confirm == "No" or confirm == "no":
			print("Please Select A Different Username")
			break
		else:
			print("That Is Not An Answer Please Try Again")
			break
	else:
		print("That Is Not An Answer Please Try Again")
		break