a =[]

n = int(input("Enter the number of elemnts \n"))
for i in range(1,n+1):
    b = int(input("Enter elemnt:"))
    a.append(b)
a.sort()
print("largest element of list " + str(a[n-1]))