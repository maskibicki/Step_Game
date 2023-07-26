num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
num3 = int(input("Enter Your Third Number: "))
if num1 > num2 and num1 > num3:
    print("The Greatest Number Is "+str(num1))
    if num2 > num3:
        print("The Middle Number Is "+str(num2))
        print("The Least Number Is "+str(num3))
    else:        
        print("The Middle Number Is "+str(num3))
        print("The Least Number Is "+str(num2))
if num2 > num1 and num2 > num3:
    print("The Greatest Number Is "+str(num2))
    if num1 > num3:
        print("The Middle Number Is "+str(num1))
        print("The Least Number Is "+str(num3))
    else:        
        print("The Middle Number Is "+str(num3))
        print("The Least Number Is "+str(num1))
if num3 > num1 and num3 > num2:
    print("The Greatest Number Is "+str(num3))
    if num1 > num2:
        print("The Middle Number Is "+str(num1))
        print("The Least Number Is "+str(num2))
    else:        
        print("The Middle Number Is "+str(num2))
        print("The Least Number Is "+str(num1))