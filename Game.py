while True:
	movement = input("What Direction Do you Want to Move? W = Move Forward,\nA = Move Left, S = Move Back,  D = Move Right, Spacebar = Jump. ")
	if movement == "w" or movement == "W":
		print("You Move Forward")
	elif movement == "a" or movement == "A":
		print("You Move Left")
	elif movement == "s" or movement == "S":
		print("You Move Back")
	elif movement == "d" or movement == "D":
		print("You Move Right")
	elif movement == " ":
		print("You Jump")
	else:
		print("That Is Not An Option")
		break
