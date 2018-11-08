def fibonacci(num):
    n1 = 0
    n2 = 1
    if num > 1:
        for i in range(1,num+1):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth

fibonacci(15)
