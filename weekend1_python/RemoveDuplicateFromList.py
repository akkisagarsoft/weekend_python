a = []
n = int(input("Enter the number of elemnts \n"))
for i in range(1,n+1):
    elem = int(input("Enter elemnt:"))
    a.append(elem)
b = set()
non_duplicate = []
for x in a:
    if x not in b:
        non_duplicate.append(x)
        b.add(x)

print("Non-duplicate list: ",non_duplicate)