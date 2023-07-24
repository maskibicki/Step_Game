counter=3
inup = input("Welcome To The Calculator! Please Select Sign In Or Sign Up! ")
if inup == "Sign In" or "Sign in":
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
elif inup == "Sign Up" or "Sign up":
	name = input("Enter Your Username. ")
	confirm = input("Your Name Is", +name, "? Yes Or No")
	if confirm == "Yes" or "yes":
		password = input("Please Enter Your Password. ")
		same = input("Please Confirm Your Password. ")
		if password == same:
			print("Your Username and Password have Been Saved!")
		else:
			print("Your Passwords Do Not Match. Please Restart.")
	elif confirm == "No" or "no":
		print("Please Select A Different Username")
	else:
		print("That Is Not An Answer Please Try Again")
else:
	print("That Is Not An Answer Please Try Again")