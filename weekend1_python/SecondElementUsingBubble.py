arr =[]

n = int(input("Enter the number of elemnts \n"))
for i in range(1,n+1):
    b = int(input("Enter elemnt:"))
    arr.append(b)
for i in range(0,len(arr)):
    for j in range(len(arr)-i-1):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("second largest element: ",arr[n-2])