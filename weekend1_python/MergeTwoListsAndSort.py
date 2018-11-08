a = []
b = []
n = int(input("Enter the numbee of elements of first list \n"))
for i in range(1,n+1):
    c = int(input("Enter element:"))
    a.append(c)


m = int(input("Enter the numbee of elements of second list \n"))
for i in range(1,m+1):
    d = int(input("Enter element:"))
    b.append(d)
new = a+b
new.sort()
print("new list :",new)