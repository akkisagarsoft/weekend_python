def removeNth(string, n):
    first = string[:n]
    print(first)
    last = string[n+1:]
    print(last)
    return first+last


str = input("enter a String \n")
index = int(input("Enter the index of character"))

str = removeNth(str,index)
print(str)