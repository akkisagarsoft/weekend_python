# iterative way
def naturalNoSum(num):

    if(num < 0):
        print("enter positive number")
    else:
        sum = 0
        while(num > 0):
            sum += num
            num = num-1
        print("the sum is :{}".format(sum))


# using recursion
def naturalSumRecur(num):
    if num <= 1:
        return num
    else:
       return num + naturalSumRecur(num-1)


if __name__ == '__main__':
    naturalNoSum(16)
    num =16
    if(num <0):
        print("enter a positive number")
    else:
        naturalSum =naturalSumRecur(num)
        print("the sum is: {}".format(naturalSum))