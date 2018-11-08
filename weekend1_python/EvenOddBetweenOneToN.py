
def evenOdd(num):
    for i in range(1,num+1):
        if i % 2 == 0:
            print("This is a even no: " + str(i))
        else:
            print("This is a odd no: " + str(i))


if __name__ == '__main__':
    n = int(input("Enter a number till you want to find even odd \n"))
    evenOdd(n)