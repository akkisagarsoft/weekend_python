def prime(n, m):
   for num in range(n, m+1):
    if num > 1:
     for i in range(2, num):
               if(num % i) == 0:
                   break
               else:
                   print(num)


prime(20,50)

# if __name__ == "__main__":
#     n = int(input("Enter first number of interval \n"))
#     m = int(input("Enter second number of interval \
#
# n"))
# prime(n,m)
