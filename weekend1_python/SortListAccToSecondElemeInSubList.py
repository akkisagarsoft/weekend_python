a = [['X',21,34,12],['Y',3,4,65,65],['Z',98,76,21]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j][1]>a[j+1][1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp


print(a)

