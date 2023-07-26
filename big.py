num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
if num1 > num2:
    print("Your First Number, "+str(num1)+ " Is Bigger Than Your Second Number " +str(num2))
elif num2 > num1:
    print("Your Second Number, "+str(num2)+ " Is Bigger Than Your First Number " +str(num1))
else:
    print("Both Numbers Are Equal")