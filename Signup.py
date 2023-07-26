counter=3
realname = "Michael"
inup = input("Welcome To The Calculator! Please Select Sign In Or Sign Up! ")
if inup == "Sign In" or inup == "Sign in" or inup == "sign in" or inup == "sign In":
	name = input("Enter Your Username. ")
	while True:
		code="Bannana"
		password = input("Enter Your Password. ")
		if password == code and name == realname:
			print("Calculator Launching...")
			break
		else:
			counter -= 1
			if counter == 0:
				print("Incorrect Too Many Times, Try Again Later")
				break
			else:
				print("Wrong Password. You Have ", +counter, " Tries Left.")
elif inup == "Sign Up" or inup == "Sign up" or inup == "sign up" or inup == "sign Up":
	name = input("Enter Your Username. ")
	confirm = input("Your Name Is " +str(name)+ "? Yes Or No? ")
	if confirm == "Yes" or confirm =="yes":
		password = input("Please Enter Your Password. ")
		same = input("Please Confirm Your Password. ")
		if password == same:
			print("Your Username and Password have Been Saved!")
		else:
			print("Your Passwords Do Not Match. Please Restart.")
	elif confirm == "No" or confirm == "no":
		print("Please Select A Different Username")
	else:
		print("That Is Not An Answer Please Try Again")
else:
	print("That Is Not An Answer Please Try Again")