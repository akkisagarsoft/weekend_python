def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))


if __name__ == '__main__':
    num = int(input("Enter a number to calculate fibonacci \n"))
    if num < 0:
        print("enter a positive number")
    else:
        for i in range(num):
            print(fibonacci(i))

