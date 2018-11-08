import cmath
def quardEqu(a,b,c):
    d = (b*b) - (4*a*c)
    # find two solution
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return sol1,sol2;

if __name__ == '__main__':
    a = int(input("Enter a's value: \n"))
    b = int(input("Enter a's value: \n"))
    c = int(input("Enter a's value: \n"))
solutions =  quardEqu(a,b,c)
for i in solutions:
    print(i)