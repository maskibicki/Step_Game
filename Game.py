while True:
	movement = input("What Direction Do you Want to Move? W = Move Forward, A = Move Left, S = Move Back,  D = Move Right, Spacebar = Jump. ")
	if movement == "w":
		print("You Move Forward")
	elif movement == "a":
		print("You Move Left")
	elif movement == "s":
		print("You Move Back")
	elif movement == "d":
		print("You Move Right")
	elif movement == " ":
		print("You Jump")
	else:
		print("That Is Not An Option")
		break
