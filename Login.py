counter=3
print("Welcome To The Calculator! Please Sign In!")
name = input("Enter Your Username. ")
while True:
	code="Bannana"
	password = input("Enter Your Password. ")
	if password == code:
		print("Calculator Launching...")
		break
	else:
		counter -= 1
		if counter == 0:
			print("Incorrect Too Many Times, Try Again Later")
			break
		else:
			print("Wrong Password. You Have ", +counter, " Tries Left.")