
while True:
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

	