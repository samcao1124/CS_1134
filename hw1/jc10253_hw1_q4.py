def fibs(n):
    num1 = 1
    num2 = 1

    for i in range(n):
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3


