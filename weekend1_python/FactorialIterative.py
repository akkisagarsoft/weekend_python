def factorial(num):
    fact = 1
    for i in range(1,num + 1):
        fact = fact*i
    return fact


if __name__ == '__main__':
    num = int(input("enter number to calculate factorial \n"))
    if num < 0:
        print("factorial cannot be created for negative numbers")
    elif num == 0:
        print("Factorial of 0 and 1 :" + str(num))
    else:
        print(factorial(num))


