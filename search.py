while True:
    n = int(input("Enter A Value For N: "))
    k = int(input("Enter A Value For K: "))
    answer = n/(2**k)
    final = n-answer
    print("the amount of numbers that were eliminated was",+final,)
    print("The remaining amount of numbers left are",+answer,)
    break