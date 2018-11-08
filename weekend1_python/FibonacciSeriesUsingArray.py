fib = [0,1]
def fibonacci(num):


        while len(fib) < num+1:
            fib.append(0)


        if num <= 1:
            return num;
        else:
            if fib[num-1] == 0:
                fib[num-1] = fibonacci(num-1)

            if fib[num-2] == 0:
                fib[num-2] = fibonacci(num-2)

            fib[num] = fib[num-2] + fib[num-1]
        return fib[num]



fibonacci(9)
for i in range(len(fib)):
    print(fib[i])

